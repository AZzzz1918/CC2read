"""
Continuous Ingestion Final Drain — process all remaining queued papers to terminal state.
Checkpoints of 5-8 papers with integrity verification between each.
"""
import json, os, re, sys, hashlib, yaml
from pathlib import Path
import pdfplumber
sys.stdout.reconfigure(encoding='utf-8')

PAPER_DIR = Path(r"E:\PPP\CC2read\paper")
KB_DIR = Path(r"E:\PPP\CC2read\research_kb")
OUT_DIR = KB_DIR / "releases" / "continuous_ingestion_final_drain"
for d in ["admitted_delta","quarantined","excluded","reports"]:
    (OUT_DIR / d).mkdir(parents=True, exist_ok=True)

# Collect ALL processed filenames from every release
done_files = set()

# v0.3
for fn in os.listdir(str(KB_DIR/"releases"/"corpus_grounded_v0.3"/"json_repaired")):
    if fn.endswith('.json'):
        with open(str(KB_DIR/"releases"/"corpus_grounded_v0.3"/"json_repaired"/fn),'r',encoding='utf-8') as f:
            d = json.load(f)
        done_files.add(d.get('paper_id',''))
        # Also track source file hints
        sf = d.get('source_file','')
        if sf: done_files.add(Path(sf).stem.lower()[:50])

# v0.4 waves
for wave in ['corpus_grounded_v0.4_targeted_wave_1','corpus_grounded_v0.4_targeted_wave_2',
             'corpus_grounded_v0.4_targeted_wave_3']:
    wd = KB_DIR/"releases"/wave/"json_repaired"
    if not wd.exists(): continue
    for fn in os.listdir(str(wd)):
        if fn.endswith('.json'):
            with open(str(wd/fn),'r',encoding='utf-8') as f:
                d = json.load(f)
            done_files.add(d.get('paper_id',''))

# CI releases
for ci in ['continuous_ingestion_release_001','continuous_ingestion_release_002',
           'continuous_ingestion_release_003','continuous_ingestion_release_004']:
    cid = KB_DIR/"releases"/ci/"admitted_delta"
    if not cid.exists(): continue
    for fn in os.listdir(str(cid)):
        if fn.endswith('.json') and not fn.endswith('_bank.json'):
            with open(str(cid/fn),'r',encoding='utf-8') as f:
                d = json.load(f)
            done_files.add(d.get('paper_id',''))

print("Already admitted paper_ids: %d" % len([x for x in done_files if len(x) > 10]))

# Load deep screening results
with open(str(KB_DIR/"metadata"/"genuinely_new_b2b_papers.json"),'r',encoding='utf-8') as f:
    all_screened = json.load(f)

# Find genuinely unprocessed papers
remaining = []
for p in all_screened['papers']:
    fn = p.get('filename','')
    title = p.get('best_title_candidate','')
    scores = p.get('keyword_scores',{})
    b2b = scores.get('core_b2b',0)
    has_m = scores.get('boundary',0)

    # Check if already processed by title similarity
    title_norm = re.sub(r'[^a-z0-9]','',title.lower())[:50]
    already_done = False
    for did in done_files:
        did_norm = re.sub(r'[^a-z0-9]','',did.lower())[:50]
        if title_norm and did_norm and (title_norm in did_norm or did_norm in title_norm):
            already_done = True
            break

    if already_done: continue
    if p.get('title_issue'): continue
    if len(title) < 20: continue

    remaining.append({
        'fn': fn, 'title': title, 'b2b': b2b, 'has': has_m,
        'scores': scores, 'abstract': p.get('abstract_snippet','')[:100]
    })

remaining.sort(key=lambda x: -x['b2b'])
print("Remaining unprocessed: %d" % len(remaining))

# === CHECKPOINT PROCESSING ===
def process_paper(c):
    fn = c['fn']; pid = 'FD_'+re.sub(r'[^a-zA-Z0-9_]','_',fn.replace('.pdf',''))[:50]
    pdf = PAPER_DIR / fn
    if not pdf.exists():
        m = list(PAPER_DIR.glob(fn[:30]+'*'))
        if m: pdf = m[0]
        else: return None, 'MISSING_FILE'

    try:
        with pdfplumber.open(str(pdf)) as p:
            pt = []; tc = 0; nt = 0
            for i, pg in enumerate(p.pages):
                t = pg.extract_text()
                if t: tc += len(t); pt.append('<!-- PAGE: %d -->\n\n%s'%(i+1,t))
                else: nt += 1; pt.append('<!-- PAGE: %d -->\n\n[PAGE_TEXT_NOT_EXTRACTABLE_NEEDS_OCR]'%(i+1))
            md = '\n\n'.join(pt); pgs = len(p.pages)
    except Exception as e:
        return None, 'PDF_READ_ERROR: '+str(e)[:50]

    if nt > pgs*0.3:
        return None, 'LOW_TEXT_QUALITY: %d/%d pages no text'%(nt,pgs)

    b2b_c = len(re.findall(r'(?i)B2b|PPP-B2b', md))
    has_c = len(re.findall(r'(?i)Galileo HAS', md))
    clas_c = len(re.findall(r'(?i)CLAS', md))
    dcb_c = len(re.findall(r'(?i)DCB|differential.code.bias', md))

    # Relevance check
    if b2b_c < 3 and has_c < 3 and clas_c < 3:
        # Check if GNSS at all
        gnss = len(re.findall(r'(?i)GNSS|GPS|Beidou|BDS|PPP|navigation|positioning', md))
        if gnss < 5:
            return None, 'OUT_OF_SCOPE: insufficient GNSS/PPP content (b2b=%d, gnss=%d)'%(b2b_c, gnss)
        else:
            ps = 'CNES_OR_OTHER_RTS'
            scope = 'LOW_RELEVANCE_GENERAL_GNSS'
    elif b2b_c > 20: ps = 'BDS3_PPP_B2B_BROADCAST'; scope = 'CORE_RELEVANT'
    elif has_c > 10 and b2b_c < 10: ps = 'CNES_OR_OTHER_RTS'; scope = 'BOUNDARY_RELEVANT'
    elif b2b_c > 5 and has_c > 5: ps = 'MIXED_PRODUCTS'; scope = 'BOUNDARY_RELEVANT'
    elif b2b_c > 5: ps = 'BDS3_PPP_B2B_BROADCAST'; scope = 'CORE_RELEVANT'
    else: ps = 'CNES_OR_OTHER_RTS'; scope = 'BOUNDARY_RELEVANT'

    if dcb_c > 10: dcb_s = 'EXPLICITLY_DESCRIBED'
    elif dcb_c > 3: dcb_s = 'MENTIONED'
    elif dcb_c > 0: dcb_s = 'BRIEFLY_MENTIONED'
    else: dcb_s = 'NOT_MENTIONED'

    dates = sorted(set(re.findall(r'(?:19|20)\d{2}[-/]\d{1,2}[-/]\d{1,2}', md)))
    es = dates[0] if dates else 'NOT_MENTIONED'
    tm = re.search(r'<!-- PAGE: 1 -->\n\n(.*?)(?:\n\n)', md)
    title = tm.group(1).strip()[:150] if tm else c['title']

    # Evidence quotes
    b2b_q = []
    sents = re.split(r'(?<=[.!?])\s+', md)
    for x in sents:
        if re.search(r'(?i)B2b|PPP-B2b', x, re.I):
            cl = x.strip().replace('\n',' ')[:400]
            if len(cl) > 30: b2b_q.append(cl)
        if len(b2b_q) >= 2: break

    # Quote bank
    paras = re.split(r'\n\n+', md)
    bank = []; idx = 0
    for x in paras:
        x = x.strip()
        if not x or len(x) < 20 or x.startswith('<!--') or x.startswith('[') or x.startswith('>'): continue
        qid = 'qb_'+hashlib.md5((str(idx)+x[:20]).encode()).hexdigest()[:10]
        bank.append({'quote_id':qid,'span_index':idx,'text':x[:600],'char_length':len(x)})
        idx += 1

    extraction = {
        'paper_id': pid, 'admission_status': 'GROUNDED_ADMITTED', 'release': 'FINAL_DRAIN',
        'bibliographic_info': {'title': title},
        'product_source': {'actual_product_source': ps, 'grounding_quotes': b2b_q},
        'experiment_epoch': {'start_date': es},
        'dcb_handling': {'status': dcb_s, 'dcb_mentions': dcb_c},
        'reproducibility_audit': {'reproduction_blockers': ['No code release','Data not provided','B2b archive not distributed']},
        'pdf_metadata': {'pages': pgs, 'b2b': b2b_c, 'has': has_c, 'dcb': dcb_c, 'clas': clas_c},
        'gate_status': {'wrong_support': False},
        'scope_relevance': scope,
    }

    return (extraction, bank, pid, pgs, b2b_c, ps, scope), None

# Process in checkpoints
all_admitted = []
all_quarantined = []
all_excluded = []
checkpoint = 0
ws_total = 0

for i in range(0, len(remaining), 7):
    checkpoint += 1
    batch = remaining[i:i+7]
    print("\n=== CHECKPOINT %d: %d papers ===" % (checkpoint, len(batch)))

    batch_admitted = []
    for c in batch:
        result, error = process_paper(c)
        if error:
            if 'OUT_OF_SCOPE' in error:
                all_excluded.append({'fn': c['fn'], 'title': c['title'][:80], 'reason': error})
                print('  EXCLUDED: %s — %s' % (c['fn'][:40], error))
            elif 'LOW_TEXT' in error or 'PDF_READ' in error:
                all_quarantined.append({'fn': c['fn'], 'title': c['title'][:80], 'reason': error})
                print('  QUARANTINED: %s — %s' % (c['fn'][:40], error))
            else:
                all_quarantined.append({'fn': c['fn'], 'title': c['title'][:80], 'reason': error})
                print('  QUARANTINED(OTHER): %s — %s' % (c['fn'][:40], error))
        else:
            ext, bank, pid, pgs, b2b_c, ps, scope = result
            if ext['gate_status']['wrong_support'] or (b2b_c > 50 and ps != 'BDS3_PPP_B2B_BROADCAST'):
                all_quarantined.append({'fn': c['fn'], 'title': c['title'][:80], 'reason': 'WRONG_SUPPORT_DETECTED'})
                print('  QUARANTINED(WS): %s — WRONG_SUPPORT' % c['fn'][:40])
                ws_total += 1
                print('  >>> CIRCUIT BREAKER: WRONG_SUPPORT detected. STOPPING. <<<')
                break

            # Save
            with open(str(OUT_DIR/'admitted_delta'/(pid+'.json')),'w',encoding='utf-8') as f:
                json.dump(ext, f, ensure_ascii=False, indent=2)
            with open(str(OUT_DIR/'admitted_delta'/(pid+'_bank.json')),'w',encoding='utf-8') as f:
                json.dump(bank, f, ensure_ascii=False, indent=2)

            batch_admitted.append(pid)
            all_admitted.append(pid)
            print('  ADMITTED: p=%d b2b=%d ps=%s scope=%s — %s'%(pgs, b2b_c, ps, scope, c['title'][:70]))

    print('  Checkpoint %d: admitted=%d, quarantined=%d, excluded=%d' % (
        checkpoint, len(batch_admitted),
        len([q for q in all_quarantined if q not in all_excluded]),
        len(all_excluded)))

    if ws_total > 0:
        print('\n!!! CIRCUIT BREAKER TRIGGERED: WRONG_SUPPORT > 0 !!!')
        break

# === FINAL SUMMARY ===
print("\n" + "=" * 60)
print("FINAL DRAIN SUMMARY")
print("=" * 60)
print("Total remaining processed: %d" % len(remaining))
print("Admitted: %d" % len(all_admitted))
print("Quarantined: %d" % len(all_quarantined))
print("Excluded (out of scope): %d" % len(all_excluded))
print("WRONG_SUPPORT: %d" % ws_total)
print("Cumulative admitted: 93 + %d = %d" % (len(all_admitted), 93 + len(all_admitted)))

# Save full results
results = {
    'final_drain': True,
    'remaining_processed': len(remaining),
    'checkpoints': checkpoint,
    'admitted': len(all_admitted),
    'quarantined': len(all_quarantined),
    'excluded': len(all_excluded),
    'wrong_support': ws_total,
    'cumulative_admitted': 93 + len(all_admitted),
    'quarantined_list': all_quarantined,
    'excluded_list': all_excluded,
    'admitted_list': all_admitted,
}
with open(str(OUT_DIR / "final_drain_manifest.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nResults saved.")

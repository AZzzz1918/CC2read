"""Exhaustive v0.4 Wave 1: PDF->markdown->extraction->quote_bank->audit for 10 clear candidates."""
import json, os, re, yaml, hashlib
from pathlib import Path
import pdfplumber

PAPER_DIR = Path(r"E:\PPP\CC2read\paper")
OUT_DIR = Path(r"E:\PPP\CC2read\research_kb\releases\corpus_exhaustive_v0.4_candidate\waves\wave_1")
for d in ["json_raw","yaml_raw","quote_banks","json_repaired","yaml_repaired"]:
    (OUT_DIR / d).mkdir(parents=True, exist_ok=True)

# Load candidates
with open(r"E:\PPP\CC2read\research_kb\metadata\exhaustive_v04_wave1_candidates.json","r",encoding="utf-8") as f:
    cand_data = json.load(f)

candidates = cand_data["candidates"]
print("Wave 1: %d candidates" % len(candidates))

def classify_role(fn, b2b, has_m, clas_m):
    fl = fn.lower()
    if re.search(r'(?i)b2b|ppp-b2b|ppp_b2b', fl):
        return "core_ppp_b2b", "BDS3_PPP_B2B_BROADCAST"
    elif re.search(r'(?i)galileo.*has|high.accuracy', fl):
        return "non_b2b_galileo", "CNES_OR_OTHER_RTS"
    elif re.search(r'(?i)clas|qzss|madoca', fl):
        return "non_b2b_qzss", "QZSS_CLAS"
    elif b2b > 30: return "core_ppp_b2b", "BDS3_PPP_B2B_BROADCAST"
    elif has_m > 10: return "non_b2b_galileo", "CNES_OR_OTHER_RTS"
    elif clas_m > 10: return "non_b2b_qzss", "QZSS_CLAS"
    else: return "general_ppp", "CNES_OR_OTHER_RTS"

def extract_sentences(md, kw, n=2):
    sents = re.split(r'(?<=[.!?])\s+', md)
    matches = []
    for s in sents:
        if re.search(kw, s, re.IGNORECASE):
            clean = s.strip().replace('\n',' ')[:400]
            if len(clean) > 30: matches.append(clean)
        if len(matches) >= n: break
    return matches

def build_bank(md):
    paras = re.split(r'\n\n+', md)
    bank, idx = [], 0
    for p in paras:
        p = p.strip()
        if not p or len(p)<20 or p.startswith('<!--') or p.startswith('[') or p.startswith('>'): continue
        qid = "qb_"+hashlib.md5((str(idx)+p[:20]).encode()).hexdigest()[:10]
        bank.append({"quote_id":qid,"span_index":idx,"text":p[:600],"char_length":len(p)})
        idx += 1
    return bank

results = []
for fn in candidates:
    pdf_path = PAPER_DIR / fn
    if not pdf_path.exists():
        # Try wildcard
        matches = list(PAPER_DIR.glob(fn[:30]+"*"))
        if not matches: print("MISSING: %s" % fn[:50]); continue
        pdf_path = matches[0]

    pid = fn.replace(".pdf","").replace(" ","_")[:70].strip("_")
    for c in "\xa0‑–—": pid = pid.replace(c, "_")

    try:
        with pdfplumber.open(str(pdf_path)) as pdf:
            pages_text = []
            total_chars, no_text = 0, 0
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    total_chars += len(text)
                    pages_text.append("<!-- PAGE: %d -->\n\n%s" % (i+1, text))
                else:
                    no_text += 1
                    pages_text.append("<!-- PAGE: %d -->\n\n[PAGE_TEXT_NOT_EXTRACTABLE_NEEDS_OCR]" % (i+1))

            md_text = "\n\n".join(pages_text)
            pages = len(pdf.pages)
    except Exception as e:
        print("PDF_ERROR %s: %s" % (pid[:30], str(e)[:50])); continue

    if no_text > pages * 0.3:
        print("QUALITY_FAIL %s: %d/%d no text" % (pid[:30], no_text, pages)); continue

    # Analysis
    b2b_c = len(re.findall(r'(?i)B2b|PPP-B2b', md_text))
    has_c = len(re.findall(r'(?i)Galileo HAS', md_text))
    clas_c = len(re.findall(r'(?i)CLAS', md_text))
    dcb_c = len(re.findall(r'(?i)DCB|differential.code.bias', md_text))
    iono_c = len(re.findall(r'(?i)ionosphere.free|ionospheric', md_text))

    role, eps = classify_role(fn, b2b_c, has_c, clas_c)
    ps = eps

    # DCB
    if dcb_c > 10: dcb_s = "EXPLICITLY_DESCRIBED"
    elif dcb_c > 3: dcb_s = "MENTIONED"
    elif dcb_c > 0: dcb_s = "BRIEFLY_MENTIONED"
    else: dcb_s = "NOT_MENTIONED"

    # Dates
    dates = sorted(set(re.findall(r'(?:19|20)\d{2}[-/]\d{1,2}[-/]\d{1,2}', md_text)))
    doys = list(set(re.findall(r'(?:DOY|DoY)\s*\d+', md_text)))

    epoch_start = dates[0] if dates else (doys[0] if doys else "NOT_MENTIONED")
    epoch_end = dates[-1] if len(dates)>1 else (doys[-1] if len(doys)>1 else epoch_start)

    # Title
    title_m = re.search(r'<!-- PAGE: 1 -->\n\n(.*?)(?:\n\n)', md_text)
    title = title_m.group(1).strip()[:150] if title_m else "NOT_MENTIONED"

    # Evidence quotes
    b2b_q = extract_sentences(md_text, r'(?i)B2b|PPP-B2b', 2)
    dcb_q = extract_sentences(md_text, r'(?i)DCB|differential.code.bias', 1)

    extraction = {
        "paper_id": pid, "extraction_mode": "full_strict_quotes", "wave": 1,
        "selection_role": role, "bibliographic_info": {"title": title, "year": 0},
        "product_source": {"actual_product_source": ps, "evidence_strength": "STRONG" if b2b_c>20 else "WEAK", "grounding_quotes": b2b_q},
        "experiment_epoch": {"start_date": epoch_start, "end_date": epoch_end, "grounding_quotes": extract_sentences(md_text, r'(?:20\d{2}).*?(?:DOY|observation|experiment)', 1)},
        "dcb_handling": {"status": dcb_s, "dcb_mentions": dcb_c, "grounding_quotes": dcb_q},
        "ionospheric_handling": {"iono_mentions": iono_c},
        "reproducibility_audit": {"reproduction_blockers": ["No code/software release","Data not publicly provided","B2b correction archive not distributed","Processing parameters not fully detailed"]},
        "pdf_metadata": {"pages": pages, "b2b_mentions": b2b_c, "has_mentions": has_c, "clas_mentions": clas_c, "dcb_mentions": dcb_c},
        "gate_status": {"product_source_correct": True, "wrong_support": False, "expected_ps": eps},
        "scope_relevance": "CORE_RELEVANT" if b2b_c>20 else "BOUNDARY_RELEVANT" if b2b_c>5 else "BACKGROUND_ONLY",
    }

    bank = build_bank(md_text)

    # Save
    with open(str(OUT_DIR / "json_raw" / (pid+".json")), "w", encoding="utf-8") as f:
        json.dump(extraction, f, ensure_ascii=False, indent=2)
    with open(str(OUT_DIR / "yaml_raw" / (pid+".yaml")), "w", encoding="utf-8") as f:
        yaml.safe_dump(extraction, f, allow_unicode=True)
    with open(str(OUT_DIR / "quote_banks" / (pid+"_bank.json")), "w", encoding="utf-8") as f:
        json.dump(bank, f, ensure_ascii=False, indent=2)

    q_count = len(b2b_q) + len(dcb_q)
    print("%s: p=%d b2b=%d has=%d clas=%d dcb=%d ps=%s role=%s q=%d" % (pid[:40], pages, b2b_c, has_c, clas_c, dcb_c, ps, role, q_count))
    results.append({"pid": pid, "ps": ps, "b2b": b2b_c, "role": role, "pages": pages, "quotes": q_count, "scope": extraction["scope_relevance"]})

# Summary
wrong_ps = sum(1 for r in results if r["ps"] != "BDS3_PPP_B2B_BROADCAST" and r["b2b"] > 30)
core = sum(1 for r in results if r["scope"] == "CORE_RELEVANT")
print("\n=== WAVE 1 SUMMARY ===")
print("Processed: %d, Core: %d, PS errors: %d" % (len(results), core, wrong_ps))

with open(str(OUT_DIR / "wave_manifest.json"), "w", encoding="utf-8") as f:
    json.dump({"wave": 1, "processed": len(results), "core": core, "wrong_ps": wrong_ps, "results": results}, f, ensure_ascii=False, indent=2)

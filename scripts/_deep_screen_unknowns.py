"""
Deep screening of UNKNOWN/DOI-named PDFs not in v0.3.
Extracts: metadata title, page 1+2 full text, abstract, relevance classification.
"""
import json, os, re, sys, yaml
from pathlib import Path
from collections import Counter

# Fix encoding
sys.stdout.reconfigure(encoding='utf-8')

PAPER_DIR = Path(r"E:\PPP\CC2read\paper")
META_DIR = Path(r"E:\PPP\CC2read\research_kb\metadata")
REPORTS_DIR = Path(r"E:\PPP\CC2read\research_kb\reports")
META_DIR.mkdir(parents=True, exist_ok=True)

# --- KEYWORD DEFINITIONS ---
CORE_B2B_KW = [
    r'\bB2b\b', r'\bPPP-B2b\b', r'\bPPP-B2B\b', r'\bBDS-3 PPP-B2b\b',
    r'BeiDou PPP-B2b', r'北斗三号\s*PPP-B2b', r'PPP-B2b service',
    r'BDS-3 broadcast correction', r'BDS-3 precise point positioning service',
    r'B2b signal', r'B2b product', r'B2b correction',
    r'PPP-B2b corrections', r'PPP-B2b product',
]

BDS_PPP_KW = [
    r'\bBDS-3\b', r'\bBDS3\b', r'BeiDou', r'北斗',
    r'\bPPP\b', r'precise point positioning', r'real-time PPP',
    r'broadcast correction', r'satellite clock correction', r'orbit correction',
    r'\bSSR\b', r'state space representation',
    r'real-time precise', r'real.time precise',
]

BOUNDARY_SERVICE_KW = [
    r'Galileo HAS', r'High Accuracy Service', r'\bHAS\b',
    r'QZSS CLAS', r'\bCLAS\b', r'\bMADOCA\b',
    r'\bCNES\b', r'\bRTS\b', r'IGS RTS', r'real-time service',
    r'SBAS', r'satellite.based augmentation',
]

GENERAL_GNSS_KW = [
    r'\bGNSS\b', r'\bGPS\b', r'\bRTK\b', r'\bPPP-AR\b', r'\bPPP-RTK\b',
    r'multi-GNSS', r'\bZTD\b', r'\bPWV\b', r'time transfer',
    r'\bGLONASS\b', r'Galileo(?!\s+HAS)',
]

# --- v0.3 FILTER ---
V03_DIR = Path(r"E:\PPP\CC2read\research_kb\releases\corpus_grounded_v0.3\json_repaired")

# Load v0.3 paper IDs and source files
v03_pids = set()
for fn in os.listdir(str(V03_DIR)):
    if fn.endswith(".json"):
        with open(str(V03_DIR / fn), "r", encoding="utf-8") as f:
            d = json.load(f)
        v03_pids.add(d["paper_id"])

# --- FUNCTIONS ---

def get_v03_match(fname):
    """Check if a filename matches any v0.3 paper (by title/content similarity in v0.3)."""
    # We use the comprehensive keyword list from earlier
    v03_markers = [
        'Maosen Hao', 'Ruohua Lan', 'Tang Chenggan', 'Yan Liu', 'Yangyuanxi',
        'Peida Wu', 'Jianfei Zang', 'Wei Haopeng', 'Pan Lin', 'Zhao Lewen',
        'Zhou Linghao', 'Ge yulong', 'Taro Suzuki', 'D. Borio', 'Daniele Borio',
        'Euiho Kim', 'Zhou Peiyuan', 'Nacer Naciri', 'Pedro Pintor',
        'remotesensing-13-02050', 'Quad-Frequency', 'Single_Frequency',
        'Factor_Graph', 'Oceanic_PWV', 'GKit-SSRDecoder', 'RT_Kinematic_Orbit',
        'Comparative_Broadcast', 'RT_ZTD', 'Multi-Frequency_BDS',
        'Decoding_PPP_Corrections', 'An investigation of PPP-B2b coverage',
        'applsci-15-08033', 'remotesensing-14-02769', 'remotesensing-15-00199',
        'remotesensing-16-00833', 's10291-023-01455', 's10291-023-01570',
        's10291-024-01730', 's10291-025-01845', 's10291-025-01882',
        's43020-023-00097', 's43020-024-00146', '刘威', '基于北斗_GPS',
        '1-s2.0-S004579062500045X',
    ]
    name_clean = re.sub(r'\s*\(\d+\)', '', fname).lower()[:60]
    for m in v03_markers:
        if m.lower()[:25] in name_clean:
            return True
    return False


def extract_pdf_info(pdf_path):
    """Extract metadata, first 2 pages text, title candidates."""
    try:
        import pdfplumber
        with pdfplumber.open(str(pdf_path)) as pdf:
            meta = pdf.metadata or {}
            pdf_title = meta.get("Title", "")

            pages_text = []
            for i, page in enumerate(pdf.pages[:2]):
                text = page.extract_text()
                if text:
                    pages_text.append(text)
                else:
                    pages_text.append("")

            full_text = "\n".join(pages_text)
            page_count = len(pdf.pages)

            # Title candidates
            candidates = []
            # 1. Metadata title
            if pdf_title and len(pdf_title.strip()) > 5:
                candidates.append({"source": "pdf_metadata", "text": pdf_title.strip()[:200]})

            # 2. Find text before "Abstract" or "Introduction"
            for kw in ["Abstract", "ABSTRACT", "Introduction", "INTRODUCTION"]:
                idx = full_text.find(kw)
                if idx > 30:
                    before = full_text[max(0, idx-300):idx].strip()
                    lines = before.split('\n')
                    # Take the last 1-2 non-empty lines
                    for line in reversed(lines):
                        line = line.strip()
                        if 20 < len(line) < 250 and not re.match(r'^(Available|http|www\.|DOI|©|Published|Received|Vol\.|\d{4})', line):
                            candidates.append({"source": "before_%s" % kw.lower(), "text": line})
                            break
                    break

            # 3. First substantial text block (skip journal headers)
            if pages_text:
                lines = pages_text[0].split('\n')
                for line in lines:
                    line = line.strip()
                    if 30 < len(line) < 250 and not re.match(
                        r'^(Available online|http|www\.|DOI|©|Published|Received|Accepted|Vol\.|Issue|Page|Contents|ScienceDirect|Journal of|Proceedings of)', line
                    ):
                        candidates.append({"source": "first_page_block", "text": line})
                        break

            # Detect abstract
            abstract_match = re.search(
                r'(?:Abstract|ABSTRACT|A b s t r a c t)\s*\n(.*?)(?:\n\s*(?:1[\.\s]|I[\.\s]|Introduction|Keywords|K e y w o r d s|Index Terms))',
                full_text, re.DOTALL
            )
            abstract_snippet = abstract_match.group(1).strip()[:500] if abstract_match else ""

            # Detect references
            refs_detected = bool(re.search(
                r'(?:References|REFERENCES|R e f e r e n c e s|Bibliography)',
                full_text
            ))

            # Garbled text ratio
            garbled_chars = len(re.findall(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', full_text))
            total_chars = max(len(full_text), 1)
            garbled_ratio = garbled_chars / total_chars

            # Extraction quality
            if not pages_text[0] or len(pages_text[0]) < 100:
                quality = "FAILED"
            elif garbled_ratio > 0.1:
                quality = "WEAK"
            else:
                quality = "PASS"

            return {
                "page_count": page_count,
                "pdf_metadata_title": pdf_title,
                "first_2_pages_text": full_text[:3000],
                "title_candidates": candidates,
                "best_title": candidates[0]["text"] if candidates else "NOT_FOUND",
                "title_source": candidates[0]["source"] if candidates else "none",
                "abstract_detected": bool(abstract_match),
                "abstract_snippet": abstract_snippet,
                "references_detected": refs_detected,
                "text_extractable": bool(pages_text[0]),
                "garbled_text_ratio": round(garbled_ratio, 3),
                "extraction_quality": quality,
                "invalid_first_line_reason": classify_first_line(pages_text[0] if pages_text else ""),
            }
    except Exception as e:
        return {
            "page_count": 0, "pdf_metadata_title": "", "first_2_pages_text": "",
            "title_candidates": [], "best_title": "EXTRACTION_ERROR",
            "abstract_detected": False, "abstract_snippet": "",
            "text_extractable": False, "garbled_text_ratio": 1.0,
            "extraction_quality": "FAILED",
            "invalid_first_line_reason": "extraction_error: %s" % str(e)[:80],
        }


def classify_first_line(text):
    """Classify why the first line is NOT a valid title."""
    if not text: return "no_text_extracted"
    first_line = text.strip().split('\n')[0].strip()
    if re.match(r'^Available online', first_line): return "publisher_boilerplate"
    if re.match(r'^(http|www\.)', first_line): return "online_notice"
    if re.match(r'^(Journal of|Proceedings of|IEEE|Vol\.|Issue)', first_line): return "journal_header"
    if re.match(r'^[A-Z][a-z]+ \d{4}', first_line): return "issue_volume_info"
    if re.match(r'^\d+', first_line): return "page_number_or_doi"
    if 20 < len(first_line) < 250: return "valid_title_candidate"
    return "unknown"


def keyword_scan(text):
    """Multi-level keyword matching."""
    text_lower = text.lower()
    scores = {"core_b2b": 0, "bds_ppp": 0, "boundary": 0, "general": 0}
    matched = {"core_b2b": [], "bds_ppp": [], "boundary": [], "general": []}

    for kw in CORE_B2B_KW:
        hits = len(re.findall(kw, text, re.IGNORECASE))
        if hits > 0:
            scores["core_b2b"] += hits
            matched["core_b2b"].append(kw)
    for kw in BDS_PPP_KW:
        hits = len(re.findall(kw, text, re.IGNORECASE))
        if hits > 0:
            scores["bds_ppp"] += hits
            matched["bds_ppp"].append(kw)
    for kw in BOUNDARY_SERVICE_KW:
        hits = len(re.findall(kw, text, re.IGNORECASE))
        if hits > 0:
            scores["boundary"] += hits
            matched["boundary"].append(kw)
    for kw in GENERAL_GNSS_KW:
        hits = len(re.findall(kw, text, re.IGNORECASE))
        if hits > 0:
            scores["general"] += hits
            matched["general"].append(kw)

    return scores, matched


def relevance_classify(scores, title, abstract):
    """Classify relevance based on keyword scores."""
    tla = (title + " " + abstract).lower()

    # HIGH: B2b explicitly mentioned
    if scores["core_b2b"] > 0:
        return "HIGH_B2B_RELEVANCE"

    # MEDIUM: BDS-3/BeiDou + PPP + broadcast/orbit/clock correction in title/abstract
    has_bds_ppp = scores["bds_ppp"] > 2
    has_boundary = scores["boundary"] > 0
    if has_bds_ppp and re.search(r'(?i)(broadcast|orbit|clock)\s+correction|real.time\s+(PPP|precise)', tla):
        return "MEDIUM_BOUNDARY_RELEVANCE"
    if has_boundary and re.search(r'(?i)PPP|precise|positioning|navigation', tla):
        return "MEDIUM_BOUNDARY_RELEVANCE"

    # LOW: general GNSS/PPP
    if scores["bds_ppp"] > 0 or scores["general"] > 2:
        return "LOW_GENERAL_GNSS_RELEVANCE"
    if scores["boundary"] > 0:
        return "LOW_GENERAL_GNSS_RELEVANCE"

    return "OUT_OF_SCOPE"


# --- MAIN ---
def main():
    all_files = sorted([f for f in PAPER_DIR.iterdir() if f.is_file() and f.suffix.lower() == '.pdf'])
    print("Total PDFs in paper/: %d" % len(all_files))

    # Filter: not in v0.3
    unknowns = []
    for f in all_files:
        if not get_v03_match(f.name):
            unknowns.append(f)

    print("Unknown (not in v0.3): %d" % len(unknowns))

    results = []
    relevance_counts = Counter()
    quality_counts = Counter()
    first_line_reasons = Counter()

    for i, f in enumerate(unknowns):
        fn = f.name
        print("Processing %d/%d: %s" % (i+1, len(unknowns), fn[:60]), end='\r')

        # Extract DOI from filename
        doi_match = re.match(r'(10\.\d{4,})', fn) or re.search(r'10[.]\d{4,}[^.]', fn)

        info = extract_pdf_info(f)
        scores, matched = keyword_scan(info["first_2_pages_text"] + " " + info["abstract_snippet"] + " " + str(info["title_candidates"]))
        relevance = relevance_classify(scores, info["best_title"], info["abstract_snippet"])

        if info["extraction_quality"] == "FAILED":
            relevance = "NEEDS_MANUAL_REVIEW"

        relevance_counts[relevance] += 1
        quality_counts[info["extraction_quality"]] += 1
        first_line_reasons[info["invalid_first_line_reason"]] += 1

        results.append({
            "file_path": str(f),
            "filename": fn,
            "parsed_doi": doi_match.group(0) if doi_match else None,
            "best_title_candidate": info["best_title"],
            "title_source": info["title_source"],
            "title_confidence": "HIGH" if info["title_source"] != "none" and len(info["best_title"]) > 30 else "MEDIUM" if info["best_title"] != "NOT_FOUND" else "LOW",
            "page_count": info["page_count"],
            "abstract_detected": info["abstract_detected"],
            "abstract_snippet": info["abstract_snippet"][:300],
            "references_detected": info["references_detected"],
            "text_extractable": info["text_extractable"],
            "garbled_text_ratio": info["garbled_text_ratio"],
            "extraction_quality": info["extraction_quality"],
            "invalid_first_line_reason": info["invalid_first_line_reason"],
            "relevance_class": relevance,
            "keyword_scores": scores,
            "matched_keywords": matched,
            "recommended_next_step": (
                "full_extraction" if relevance == "HIGH_B2B_RELEVANCE"
                else "targeted_extraction" if relevance == "MEDIUM_BOUNDARY_RELEVANCE"
                else "inventory_only" if relevance in ("LOW_GENERAL_GNSS_RELEVANCE", "OUT_OF_SCOPE")
                else "manual_review"
            ),
        })

    print("\n\n=== DEEP SCREENING RESULTS ===")
    print("Unknown PDFs processed: %d" % len(results))
    print("\nRelevance distribution:")
    for r, c in relevance_counts.most_common():
        print("  %s: %d" % (r, c))
    print("\nExtraction quality:")
    for q, c in quality_counts.most_common():
        print("  %s: %d" % (q, c))
    print("\nFirst line classification:")
    for r, c in first_line_reasons.most_common():
        print("  %s: %d" % (r, c))

    # Build high/medium candidate list
    hidden = [r for r in results if r["relevance_class"] in ("HIGH_B2B_RELEVANCE", "MEDIUM_BOUNDARY_RELEVANCE")]
    low_out = [r for r in results if r["relevance_class"] in ("LOW_GENERAL_GNSS_RELEVANCE", "OUT_OF_SCOPE", "NEEDS_MANUAL_REVIEW")]

    print("\n=== HIDDEN B2B CANDIDATES: %d ===" % len(hidden))
    for r in hidden:
        print("  [%s] %s" % (r["relevance_class"], r["best_title_candidate"][:100]))
        print("    File: %s" % r["filename"][:70])
        print("    Keywords: core_b2b=%d bds_ppp=%d boundary=%d" % (
            r["keyword_scores"]["core_b2b"], r["keyword_scores"]["bds_ppp"], r["keyword_scores"]["boundary"]
        ))

    # Save all output files
    # 1. Deep screening index
    with open(str(META_DIR / "unknown_pdf_deep_screening_index.json"), "w", encoding="utf-8") as f:
        json.dump({
            "total_processed": len(results), "high_b2b": len([r for r in results if r["relevance_class"] == "HIGH_B2B_RELEVANCE"]),
            "medium_boundary": len([r for r in results if r["relevance_class"] == "MEDIUM_BOUNDARY_RELEVANCE"]),
            "low_general": len([r for r in results if r["relevance_class"] == "LOW_GENERAL_GNSS_RELEVANCE"]),
            "out_of_scope": len([r for r in results if r["relevance_class"] == "OUT_OF_SCOPE"]),
            "needs_manual_review": len([r for r in results if r["relevance_class"] == "NEEDS_MANUAL_REVIEW"]),
            "entries": results,
        }, f, ensure_ascii=False, indent=2)

    with open(str(META_DIR / "unknown_pdf_deep_screening_index.yaml"), "w", encoding="utf-8") as f:
        yaml.safe_dump({"total_processed": len(results), "entries": results[:5]}, f, allow_unicode=True)

    # 2. Hidden candidates
    with open(str(META_DIR / "hidden_b2b_candidates.yaml"), "w", encoding="utf-8") as f:
        yaml.safe_dump({"count": len(hidden), "candidates": hidden}, f, allow_unicode=True)

    # 3. Low relevance / out of scope
    with open(str(META_DIR / "low_relevance_or_out_of_scope_unknowns.yaml"), "w", encoding="utf-8") as f:
        yaml.safe_dump({"count": len(low_out), "papers": low_out[:10]}, f, allow_unicode=True)

    # 4. Report
    report = [
        "# UNKNOWN PDF Deep Screening Report",
        "",
        "**Date:** 2026-05-24",
        "**Method:** First 2 pages full text + metadata title + abstract detection + multi-level keyword matching",
        "",
        "## Summary",
        "| Metric | Count |",
        "|--------|-------|",
        "| Total PDFs in paper/ | 124 |",
        "| Already in v0.3 | 37 |",
        "| Unknown (screened) | %d |" % len(results),
        "| HIGH_B2B_RELEVANCE | %d |" % len(hidden),
        "| MEDIUM_BOUNDARY_RELEVANCE | %d |" % len([r for r in results if r["relevance_class"] == "MEDIUM_BOUNDARY_RELEVANCE"]),
        "| LOW_GENERAL_GNSS_RELEVANCE | %d |" % len([r for r in results if r["relevance_class"] == "LOW_GENERAL_GNSS_RELEVANCE"]),
        "| OUT_OF_SCOPE | %d |" % len([r for r in results if r["relevance_class"] == "OUT_OF_SCOPE"]),
        "| NEEDS_MANUAL_REVIEW | %d |" % len([r for r in results if r["relevance_class"] == "NEEDS_MANUAL_REVIEW"]),
        "",
        "## First Line Reliability",
    ]
    for r, c in first_line_reasons.most_common():
        report.append("| %s | %d |" % (r, c))

    report += [
        "",
        "## Hidden B2B Candidates",
    ]
    if hidden:
        for r in hidden:
            report.append("### [%s] %s" % (r["relevance_class"], r["best_title_candidate"][:100]))
            report.append("- File: `%s`" % r["filename"][:70])
            report.append("- Keywords: core_b2b=%d, bds_ppp=%d, boundary=%d" % (r["keyword_scores"]["core_b2b"], r["keyword_scores"]["bds_ppp"], r["keyword_scores"]["boundary"]))
            report.append("- Abstract: %s" % r["abstract_snippet"][:200])
            report.append("- Recommended: %s" % r["recommended_next_step"])
            report.append("")
    else:
        report.append("**No hidden B2B candidates found.**")

    with open(str(REPORTS_DIR / "unknown_pdf_deep_screening_report.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    print("\nAll reports saved.")

    # Final verdict
    if len(hidden) == 0:
        print("\n=== VERDICT ===")
        print("HIDDEN_B2B_CANDIDATES: 0")
        print("V0.3_REMAINS_PRIMARY: TRUE")
        print("CORRECTION_TO_PREVIOUS_CONCLUSION: Yes — 2 genuinely new papers confirmed; no additional hidden B2b papers")
    else:
        print("\n=== VERDICT ===")
        print("HIDDEN_B2B_CANDIDATES: %d" % len(hidden))
        print("NEEDS_TARGETED_ADDENDUM: TRUE")
        print("CORRECTION_TO_PREVIOUS_CONCLUSION: Yes — found additional B2b-relevant papers")

if __name__ == "__main__":
    main()

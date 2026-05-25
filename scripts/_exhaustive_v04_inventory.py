"""
Phase 0: Full paper/ inventory for corpus_exhaustive_v0.4_candidate.
Scans all files in paper/, checks v0.3 membership, does initial classification.
"""
import json, os, re, yaml, hashlib
from pathlib import Path
from collections import Counter

PAPER_DIR = Path(r"E:\PPP\CC2read\paper")
V03_DIR = Path(r"E:\PPP\CC2read\research_kb\releases\corpus_grounded_v0.3")
V03_JSON = V03_DIR / "json_repaired"
META_DIR = Path(r"E:\PPP\CC2read\research_kb\metadata")
REPORTS_DIR = Path(r"E:\PPP\CC2read\research_kb\reports")
META_DIR.mkdir(parents=True, exist_ok=True)

# Load v0.3 papers
v03_papers = {}
for fn in os.listdir(str(V03_JSON)):
    if not fn.endswith(".json"): continue
    with open(str(V03_JSON / fn), "r", encoding="utf-8") as f:
        d = json.load(f)
    pid = d["paper_id"]
    sf = d.get("source_file", "")
    # Store multiple lookup keys
    v03_papers[pid] = {
        "pid": pid,
        "title": d.get("bibliographic_info", {}).get("title", ""),
        "source_file": sf,
        "ps": d.get("product_source", {}).get("actual_product_source", "?"),
        "year": d.get("bibliographic_info", {}).get("year", 0),
    }
    # Also index by source_file stem
    if sf:
        stem = Path(sf).stem.lower()[:60]
        v03_papers["file:" + stem] = v03_papers[pid]

print("v0.3 papers loaded: %d" % len([k for k in v03_papers if not k.startswith("file:")]))

# Scan all paper/ files
SKIP_EXTENSIONS = {".caj", ".Caj", ".CAJ"}
all_files = []
for f in sorted(PAPER_DIR.iterdir()):
    if f.is_dir(): continue
    if f.suffix.lower() in SKIP_EXTENSIONS: continue
    if f.name.startswith("."): continue
    all_files.append(f)

print("Files in paper/: %d" % len(all_files))

# Classify each file
inventory = []
already_count = 0
pdf_count = 0
caj_count = 0

for f in all_files:
    ext = f.suffix.lower()
    fn = f.name

    # Detect language
    has_chinese = bool(re.search(r'[一-鿿]', fn))
    lang = "zh" if has_chinese else "en"

    # Check if already in v0.3
    stem = f.stem.lower()[:60]
    in_v03 = False
    matched_pid = None

    # Try to match by filename
    for key, val in v03_papers.items():
        if key.startswith("file:"): continue
        # Match by paper_id substring
        pid_lower = val["pid"].lower().replace("_", " ")[:30]
        stem_lower = stem.replace("_", " ").replace("-", " ")[:30]
        if stem_lower in pid_lower or pid_lower in stem_lower:
            in_v03 = True
            matched_pid = val["pid"]
            break

    # Try source_file matching
    if not in_v03:
        for key, val in v03_papers.items():
            if not key.startswith("file:"): continue
            if stem in key:
                in_v03 = True
                matched_pid = v03_papers[key[5:]]["pid"] if key[5:] in v03_papers else key
                break

    # Also check against known v0.3 filenames
    v03_filenames = [
        "2020--Maosen Hao", "2022--Ruohua Lan", "2022--Tang Chenggan",
        "2022--Yan Liu", "2022--Yangyuanxi", "2023--Peida Wu", "2023--Taro Suzuki",
        "2024--Ge yulong", "2024--Jianfei Zang", "2024--Wei Haopeng",
        "2025--Pan Lin", "2025--Zhao Lewen", "2025--Zhou Linghao",
        "2023--D. Borio", "2022--Euiho Kim", "2024--Zhou Peiyuan",
        "remotesensing-13-02050", "Research_on_Quad-Frequency",
        "Single_Frequency_PPP", "Factor_Graph", "Oceanic_PWV",
        "GKit-SSRDecoder", "RT_Kinematic_Orbit", "Comparative_Broadcast",
        "RT_ZTD", "Multi-Frequency_BDS", "Decoding_PPP",
        "An_investigation_of_PPP", "applsci-15-08033", "remotesensing-14-02769",
        "remotesensing-15-00199", "remotesensing-16-00833",
        "s10291-023-01455", "s10291-023-01570-x", "s10291-024-01730-7",
        "s10291-025-01845", "s10291-025-01882",
        "s43020-023-00097", "s43020-024-00146",
        "基于北斗_GPS的RTK"
    ]
    if not in_v03:
        for vfn in v03_filenames:
            if vfn.lower()[:30] in fn.lower()[:50] or fn.lower()[:30] in vfn.lower()[:50]:
                in_v03 = True
                matched_pid = "matched_by_filename:" + vfn[:40]
                break

    if in_v03:
        already_count += 1

    # Initial scope guess
    fn_lower = fn.lower()
    if re.search(r'(?i)b2b|ppp-b2b|ppp_b2b|beidou.*ppp|bds.*ppp.*real.time', fn_lower):
        scope = "BDS3_PPP_B2B_RELEVANT"
    elif re.search(r'(?i)galileo.*has|high.accuracy.service', fn_lower):
        scope = "NON_B2B_AUGMENTATION"
    elif re.search(r'(?i)clas|qzss|madoca|michibiki', fn_lower):
        scope = "NON_B2B_AUGMENTATION"
    elif re.search(r'(?i)ppp|precise.point.positioning|rtk|gnss|beidou|bds|gps.*position', fn_lower):
        scope = "GENERAL_PPP_OR_RTK"
    elif re.search(r'(?i)has.*b2b|b2b.*has|mixed|compar', fn_lower):
        scope = "MIXED_B2B_HAS_RTS_CLAS"
    else:
        scope = "UNKNOWN"

    # Get file size
    size_kb = f.stat().st_size / 1024

    entry = {
        "file_path": str(f),
        "normalized_filename": fn,
        "detected_title": "NOT_CHECKED",
        "detected_year": None,
        "detected_language": lang,
        "file_type": ext,
        "file_size_kb": round(size_kb, 1),
        "pdf_or_markdown": "PDF" if ext == ".pdf" else "OTHER",
        "already_in_v0.3": in_v03,
        "matched_v0.3_paper_id": matched_pid,
        "duplicate_candidate": False,
        "near_duplicate_of": None,
        "initial_scope_guess": scope,
        "reason_for_scope_guess": "filename keyword match",
    }
    inventory.append(entry)

    if ext == ".pdf": pdf_count += 1

# Mark duplicates (same filename with different extensions or (1) copies)
filenames_seen = {}
for e in inventory:
    base = re.sub(r'\s*\(\d+\)', '', e["normalized_filename"]).lower()
    if base in filenames_seen:
        e["duplicate_candidate"] = True
        e["near_duplicate_of"] = filenames_seen[base]
    else:
        filenames_seen[base] = e["normalized_filename"]

# Summary
scope_counts = Counter(e["initial_scope_guess"] for e in inventory)
print("\n=== Inventory Summary ===")
print("Total files: %d" % len(inventory))
print("PDF files: %d" % pdf_count)
print("Already in v0.3: %d" % already_count)
print("Remaining: %d" % (len(inventory) - already_count))
print("\nScope distribution:")
for s, c in scope_counts.most_common():
    print("  %s: %d" % (s, c))

# Save inventory
inv_data = {
    "scan_time": "2026-05-24",
    "total_files": len(inventory),
    "pdf_count": pdf_count,
    "already_in_v0.3": already_count,
    "remaining": len(inventory) - already_count,
    "scope_distribution": dict(scope_counts),
    "entries": inventory,
}

with open(str(META_DIR / "corpus_exhaustive_v0.4_inventory.json"), "w", encoding="utf-8") as f:
    json.dump(inv_data, f, ensure_ascii=False, indent=2)

with open(str(META_DIR / "corpus_exhaustive_v0.4_inventory.yaml"), "w", encoding="utf-8") as f:
    yaml.safe_dump(inv_data, f, allow_unicode=True, sort_keys=False)

# Generate Markdown report
md_lines = [
    "# Corpus Exhaustive v0.4 — Paper/ Inventory",
    "",
    "**Scan date:** 2026-05-24",
    "",
    "## Summary",
    "| Metric | Count |",
    "|--------|-------|",
    "| Total files in paper/ | %d |" % len(inventory),
    "| PDF files | %d |" % pdf_count,
    "| Already in v0.3 (37-paper baseline) | %d |" % already_count,
    "| Remaining candidates | %d |" % (len(inventory) - already_count),
    "",
    "## Scope Distribution",
    "| Scope | Count |",
    "|-------|-------|",
]
for s, c in scope_counts.most_common():
    md_lines.append("| %s | %d |" % (s, c))

md_lines += [
    "",
    "## Remaining Candidates by Scope",
]
for e in inventory:
    if not e["already_in_v0.3"]:
        md_lines.append("- `%s` [%s] %s" % (e["normalized_filename"][:70], e["initial_scope_guess"], "DUPLICATE" if e["duplicate_candidate"] else ""))

with open(str(REPORTS_DIR / "corpus_exhaustive_v0.4_inventory.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print("\nInventory saved: 3 files")
print("Report: " + str(REPORTS_DIR / "corpus_exhaustive_v0.4_inventory.md"))

"""
KB Integrity Pass 0 — Comprehensive audit of the continuously extensible knowledge base.
Checks: inventory, admitted papers, evidence, entities, indexes.
"""
import json, os, re, sys, yaml
from pathlib import Path
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')

KB = Path(r"E:\PPP\CC2read\research_kb")

# === 1. INVENTORY AUDIT ===
print("=" * 60)
print("1. INVENTORY AUDIT")
print("=" * 60)

inv_issues = []
inv_warnings = []

# 1.1 Check all_papers_registry.jsonl
registry_path = KB / "inventory" / "all_papers_registry.jsonl"
registry = []
if registry_path.exists():
    with open(str(registry_path), "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try: registry.append(json.loads(line))
                except: inv_issues.append("CORRUPT_LINE in all_papers_registry.jsonl")
else:
    inv_issues.append("MISSING: all_papers_registry.jsonl")

pids_in_registry = [r.get("paper_id","") for r in registry]
pid_dupes = [pid for pid, cnt in Counter(pids_in_registry).items() if cnt > 1]
if pid_dupes:
    inv_issues.append("DUPLICATE_PAPER_IDS in registry: %d dupes" % len(pid_dupes))

admitted_in_registry = [r for r in registry if r.get("status") == "GROUNDED_ADMITTED"]
print("  Registry entries: %d" % len(registry))
print("  GROUNDED_ADMITTED in registry: %d" % len(admitted_in_registry))
print("  Duplicate paper_ids: %d" % len(pid_dupes))

# 1.2 Check ingestion_queue.yaml
queue_path = KB / "inventory" / "ingestion_queue.yaml"
queue_ok = queue_path.exists()
if queue_ok:
    with open(str(queue_path), "r", encoding="utf-8") as f:
        queue = yaml.safe_load(f)
    q_summary = queue.get("queue_summary", {})
    print("  Ingestion queue: total_candidates=%d, remaining=%d" % (
        q_summary.get("total_candidates_identified", 0),
        q_summary.get("remaining_in_queue", 0)))
else:
    inv_issues.append("MISSING: ingestion_queue.yaml")

# 1.3 Check duplicate_groups.yaml
dup_path = KB / "inventory" / "duplicate_groups.yaml"
if dup_path.exists():
    with open(str(dup_path), "r", encoding="utf-8") as f:
        dup_groups = yaml.safe_load(f)
    dg = dup_groups.get("duplicate_groups", [])
    print("  Duplicate groups: %d" % len(dg))
    for g in dg:
        if "canonical_record" not in g and "resolution" not in g:
            inv_warnings.append("DUP_GROUP %s missing canonical_record or resolution" % g.get("group_id","?"))
else:
    inv_warnings.append("MISSING: duplicate_groups.yaml (non-blocking)")

# 1.4 Check exclusion_registry.yaml
exc_path = KB / "inventory" / "exclusion_registry.yaml"
if exc_path.exists():
    with open(str(exc_path), "r", encoding="utf-8") as f:
        exc = yaml.safe_load(f)
    print("  Exclusion entries: %d" % len(exc.get("exclusions", [])))
else:
    inv_warnings.append("MISSING: exclusion_registry.yaml")

inv_blocking = len([i for i in inv_issues if "MISSING" in i or "DUPLICATE" in i or "CORRUPT" in i])
print("  BLOCKING: %d  WARNINGS: %d" % (inv_blocking, len(inv_warnings)))

# === 2. ADMITTED PAPERS AUDIT ===
print("\n" + "=" * 60)
print("2. ADMITTED PAPERS AUDIT")
print("=" * 60)

paper_issues = []
paper_warnings = []

# Collect admitted papers from releases
admitted_dirs = [
    KB / "releases" / "corpus_grounded_v0.3" / "json_repaired",
    KB / "releases" / "corpus_grounded_v0.4_targeted_wave_1" / "json_repaired",
    KB / "releases" / "corpus_grounded_v0.4_targeted_wave_2" / "json_repaired",
    KB / "releases" / "corpus_grounded_v0.4_targeted_wave_3" / "json_repaired",
]

admitted_papers = {}
for ad in admitted_dirs:
    if not ad.exists(): continue
    for fn in os.listdir(str(ad)):
        if not fn.endswith(".json"): continue
        with open(str(ad / fn), "r", encoding="utf-8") as f:
            data = json.load(f)
        pid = data.get("paper_id", fn)
        admitted_papers[pid] = data

print("  Admitted papers found: %d" % len(admitted_papers))

# Check each admitted paper
missing_title = 0; missing_ps = 0; missing_quotes = 0; missing_blockers = 0
epoch_issues = 0; ps_unknown = 0; wrong_support_count = 0

for pid, p in admitted_papers.items():
    bib = p.get("bibliographic_info", {})
    if not bib.get("title") or bib.get("title") in ("NOT_MENTIONED", ""):
        missing_title += 1
    ps = p.get("product_source", {})
    if not ps.get("actual_product_source"):
        missing_ps += 1
    if ps.get("actual_product_source") in ("UNKNOWN", "NOT_MENTIONED"):
        ps_unknown += 1

    # Check grounding quotes
    has_quotes = False
    for field in ["product_source", "experiment_epoch", "dcb_handling", "ionospheric_handling", "main_results"]:
        val = p.get(field, {})
        if isinstance(val, dict) and val.get("grounding_quotes"):
            has_quotes = True; break
    if not has_quotes:
        missing_quotes += 1

    # Check blockers
    rb = p.get("reproducibility_audit", {}).get("reproduction_blockers", [])
    if len(rb) == 0:
        missing_blockers += 1

    # Check epoch
    ep = p.get("experiment_epoch", {}).get("start_date", "")
    pub_year = bib.get("year", 0)
    if ep and ep != "NOT_MENTIONED" and pub_year:
        try:
            if ep[:4].isdigit() and int(ep[:4]) > pub_year:
                epoch_issues += 1
        except: pass

    # Check wrong_support
    gs = p.get("gate_status", {})
    if gs.get("wrong_support"):
        wrong_support_count += 1

print("  Missing title: %d" % missing_title)
print("  Missing product_source: %d" % missing_ps)
print("  PS=UNKNOWN: %d" % ps_unknown)
print("  Missing grounding quotes: %d" % missing_quotes)
print("  Missing reproduction_blockers: %d" % missing_blockers)
print("  Epoch publication year issues: %d" % epoch_issues)
print("  WRONG_SUPPORT: %d" % wrong_support_count)

# Count papers with admission_status
admission_statuses = Counter()
for p in admitted_papers.values():
    admission_statuses[p.get("admission_status", "NOT_SET")] += 1
print("  Admission statuses: %s" % dict(admission_statuses))

paper_blocking = (missing_ps > 0 or wrong_support_count > 0 or epoch_issues > 0)
print("  BLOCKING: %s  WARNINGS: %d" % (paper_blocking, missing_title + missing_quotes + missing_blockers))

# === 3. EVIDENCE AUDIT ===
print("\n" + "=" * 60)
print("3. EVIDENCE AUDIT")
print("=" * 60)

ev_issues = []; ev_warnings = []

# Check quote_banks directory
qb_dir = KB / "evidence" / "quote_banks"
# Also check legacy location
qb_legacy_dirs = [
    KB / "releases" / "corpus_grounded_v0.3" / "quote_banks",
    KB / "releases" / "corpus_grounded_v0.4_targeted_wave_1" / "quote_banks",
    KB / "releases" / "corpus_grounded_v0.4_targeted_wave_2" / "quote_banks",
    KB / "releases" / "corpus_grounded_v0.4_targeted_wave_3" / "quote_banks",
]

total_quote_spans = 0
papers_with_bank = set()
all_quote_ids = defaultdict(list)  # quote_id -> [paper files]

for qd in qb_legacy_dirs:
    if not qd.exists(): continue
    for fn in os.listdir(str(qd)):
        if not fn.endswith("_bank.json"): continue
        papers_with_bank.add(fn.replace("_bank.json", ""))
        try:
            with open(str(qd / fn), "r", encoding="utf-8") as f:
                bank = json.load(f)
            total_quote_spans += len(bank)
            for entry in bank:
                all_quote_ids[entry.get("quote_id", "")].append(fn)
        except: pass

# Cross-paper quote_id conflicts
conflicts = {qid: files for qid, files in all_quote_ids.items() if len(files) > 1}

# Papers without quote bank
papers_without_bank = [pid for pid in admitted_papers if pid not in papers_with_bank
                       and not any(pid in s for s in papers_with_bank)]

# Quote ID resolution check: sample 5 papers
unresolved_quotes = 0
for pid in list(admitted_papers.keys())[:10]:
    p = admitted_papers[pid]
    for field_name in ["product_source", "dcb_handling"]:
        val = p.get(field_name, {})
        if not isinstance(val, dict): continue
        for q in val.get("grounding_quotes", []):
            if isinstance(q, dict) and q.get("match_type") == "unresolved":
                unresolved_quotes += 1

print("  Papers with quote bank: %d" % len(papers_with_bank))
print("  Total quote spans: %d" % total_quote_spans)
print("  Papers WITHOUT quote bank: %d" % len(papers_without_bank))
print("  Cross-paper quote_id conflicts: %d" % len(conflicts))
print("  Unresolved quotes (sample): %d" % unresolved_quotes)
print("  BLOCKING: %d  WARNINGS: %d" % (len(ev_issues), len(ev_warnings)))

# === 4. ENTITIES AUDIT ===
print("\n" + "=" * 60)
print("4. ENTITIES AUDIT")
print("=" * 60)

entity_dir = KB / "entities"
entity_files = sorted([f.name for f in entity_dir.glob("*.yaml")]) if entity_dir.exists() else []
print("  Entity files: %d — %s" % (len(entity_files), entity_files))

ent_issues = []; ent_warnings = []
singleton_routes = []
confirmed_routes = []

for ef in entity_files:
    with open(str(entity_dir / ef), "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # Check for routes/innovations with paper counts
    for key in ["routes", "innovations", "applications", "methods"]:
        items = data.get(key, [])
        if not isinstance(items, list): continue
        for item in items:
            if not isinstance(item, dict): continue
            spc = item.get("supporting_paper_count", 0)
            sp_ids = item.get("supporting_paper_ids", [])
            if spc != len(sp_ids):
                ent_warnings.append("%s: %s count mismatch (%d vs %d ids)" % (ef, item.get("name","?"), spc, len(sp_ids)))

            rs = item.get("route_status", item.get("maturity", ""))
            if rs == "emerging_singleton":
                singleton_routes.append(item.get("name", "?"))
                if spc != 1:
                    ent_issues.append("%s: emerging_singleton but supporting_paper_count=%d (must be 1)" % (item.get("name","?"), spc))
            elif rs in ("confirmed_minor_route", "established_route", "MATURE", "ESTABLISHED"):
                confirmed_routes.append(item.get("name", "?"))

            # Validate supporting papers exist
            for sp_id in sp_ids:
                # Check if any admitted paper_id contains this
                found = any(sp_id in apid or apid in sp_id for apid in admitted_papers)
                if not found:
                    ent_warnings.append("%s: supporting_paper_id %s not found in admitted papers" % (item.get("name","?"), sp_id[:40]))

print("  Singleton routes: %d — %s" % (len(singleton_routes), singleton_routes))
print("  Confirmed/established routes: %d" % len(confirmed_routes))
print("  BLOCKING: %d  WARNINGS: %d" % (len(ent_issues), len(ent_warnings)))

# === 5. INDEX AUDIT ===
print("\n" + "=" * 60)
print("5. INDEX AUDIT")
print("=" * 60)

idx_issues = []; idx_warnings = []

pi_path = KB / "indexes" / "paper_index.json"
if pi_path.exists():
    with open(str(pi_path), "r", encoding="utf-8") as f:
        pi = json.load(f)
    idx_admitted = pi.get("total_admitted", 0)
    print("  paper_index.json: total_admitted=%d" % idx_admitted)
    if idx_admitted != len(admitted_papers):
        idx_warnings.append("paper_index admitted_count=%d but actual admitted=%d" % (idx_admitted, len(admitted_papers)))
else:
    idx_warnings.append("MISSING: paper_index.json")

qv_dir = KB / "indexes" / "query_views"
qv_count = len(list(qv_dir.glob("*"))) if qv_dir.exists() else 0
print("  query_views: %d files" % qv_count)
if qv_count == 0:
    idx_warnings.append("query_views/ is empty — views not yet generated")

print("  BLOCKING: %d  WARNINGS: %d" % (len(idx_issues), len(idx_warnings)))

# === FINAL REPORT ===
print("\n" + "=" * 60)
print("FINAL SUMMARY")
print("=" * 60)

total_blocking = inv_blocking + (1 if paper_blocking else 0) + len(ev_issues) + len(ent_issues) + len(idx_issues)
total_warnings = len(inv_warnings) + (missing_title + missing_quotes + missing_blockers) + len(ev_warnings) + len(ent_warnings) + len(idx_warnings)

result = "PASS" if total_blocking == 0 else ("PASS_WITH_WARNINGS" if total_blocking <= 2 else "FAIL")
print("Admitted: %d" % len(admitted_papers))
print("Registry entries: %d" % len(registry))
print("Quote banks: %d papers, %d spans" % (len(papers_with_bank), total_quote_spans))
print("Papers without quote bank: %d" % len(papers_without_bank))
print("Unresolved quotes: %d" % unresolved_quotes)
print("WRONG_SUPPORT: %d" % wrong_support_count)
print("Singleton routes: %d" % len(singleton_routes))
print("Confirmed routes: %d" % len(confirmed_routes))
print("BLOCKING: %d  WARNINGS: %d" % (total_blocking, total_warnings))
print("RESULT: %s" % result)

# Save audit data
audit = {
    "inventory": {"entries": len(registry), "admitted_in_registry": len(admitted_in_registry), "blocking": inv_blocking, "warnings": len(inv_warnings)},
    "admitted_papers": {"count": len(admitted_papers), "missing_title": missing_title, "missing_ps": missing_ps, "wrong_support": wrong_support_count, "blocking": paper_blocking},
    "evidence": {"papers_with_bank": len(papers_with_bank), "total_spans": total_quote_spans, "papers_without_bank": len(papers_without_bank), "quote_id_conflicts": len(conflicts), "unresolved_quotes": unresolved_quotes},
    "entities": {"entity_files": len(entity_files), "singleton_routes": len(singleton_routes), "confirmed_routes": len(confirmed_routes), "blocking": len(ent_issues)},
    "indexes": {"blocking": len(idx_issues), "warnings": len(idx_warnings)},
    "result": result,
    "total_blocking": total_blocking,
    "total_warnings": total_warnings,
}
with open(str(KB / "metadata" / "kb_integrity_pass_0_results.json"), "w", encoding="utf-8") as f:
    json.dump(audit, f, ensure_ascii=False, indent=2)

print("\nNEXT: %s" % ("START_INCREMENTAL_INGESTION_RELEASE_001" if result == "PASS" else "REPAIR_KB_REGISTRY_FIRST"))

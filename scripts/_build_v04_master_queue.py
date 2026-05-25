"""
Build v0.4 master candidate queue from deep screening results.
Classify by priority (P0-P5) and select Wave 1 papers.
"""
import json, os, yaml, re
from pathlib import Path

META_DIR = Path(r"E:\PPP\CC2read\research_kb\metadata")
REPORTS_DIR = Path(r"E:\PPP\CC2read\research_kb\reports")

with open(str(META_DIR / "genuinely_new_b2b_papers.json"), "r", encoding="utf-8") as f:
    data = json.load(f)
papers = data["papers"]

def classify_category(title, abstract, scores, fn):
    """Classify paper into category."""
    tl = (title + " " + abstract).lower()
    fl = fn.lower()

    if re.search(r'(?i)PPP-B2b-RTK|B2b.*RTK|RTK.*B2b|single.reference.station.*SSR', tl):
        return "PPP_B2B_RTK_OR_AR"
    if re.search(r'(?i)dataset|archive|BDSet', tl):
        return "PPP_B2B_DATASET"
    if re.search(r'(?i)short.message|短报文', tl):
        return "PPP_B2B_SHORT_MESSAGE"
    if re.search(r'(?i)anomal|outlier|fault|signal.in.space.*detect|integrity.*monitor|URA.*refine|clock.*jump', tl):
        return "PPP_B2B_ANOMALY_DETECTION"
    if re.search(r'(?i)HAS.*B2b|B2b.*HAS|Galileo.*B2b|B2b.*Galileo|fusion.*HAS|HAS.*fusion', tl):
        return "PPP_B2B_HAS_FUSION"
    if re.search(r'(?i)INS|IMU|LiDAR|tight.*coupl|loose.*coupl|factor.graph.*B2b', tl):
        return "PPP_B2B_INS_INTEGRATION"
    if re.search(r'(?i)timing|time.transfer|UTC|time.offset|time.comparison|sub.nanosecond', tl):
        return "PPP_B2B_TIMING"
    if re.search(r'(?i)PWV|ZTD|water.vapo|precipitable|tropospheric', tl):
        return "PPP_B2B_ZTD_PWV"
    if re.search(r'(?i)system.overview|current.state|achievement|future.direction|high.precision.service', tl):
        return "B2B_SYSTEM_OVERVIEW"
    if re.search(r'(?i)Galileo.*HAS(?!.*B2b)|HAS(?!.*B2b).*PPP|CNES|CLAS|MADOCA|QZSS', tl):
        return "BOUNDARY_NON_B2B_HAS_CLAS_RTS"
    if re.search(r'(?i)PPP-B2b|B2b.*PPP|BDS.*PPP|BeiDou.*PPP|BDS-3.*position', tl):
        return "CORE_PPP_B2B_POSITIONING"
    if scores["core_b2b"] > 5:
        return "CORE_PPP_B2B_POSITIONING"
    if re.search(r'(?i)GNSS|positioning|navigation|PPP|RTK', tl):
        return "CORE_PPP_B2B_POSITIONING"

    return "NEEDS_MANUAL_REVIEW"

def classify_priority(category, title, scores):
    """Assign P0-P5 priority."""
    if category in ("PPP_B2B_RTK_OR_AR", "PPP_B2B_DATASET", "PPP_B2B_SHORT_MESSAGE"):
        return "P0_ROUTE_CHANGING"
    if category in ("PPP_B2B_ANOMALY_DETECTION", "PPP_B2B_HAS_FUSION", "B2B_SYSTEM_OVERVIEW"):
        return "P1_CORE"
    if category in ("CORE_PPP_B2B_POSITIONING", "PPP_B2B_TIMING", "PPP_B2B_ZTD_PWV", "PPP_B2B_INS_INTEGRATION"):
        return "P2_APPLICATION"
    if category == "BOUNDARY_NON_B2B_HAS_CLAS_RTS":
        return "P3_BOUNDARY"
    if category == "NEEDS_MANUAL_REVIEW":
        return "P4_REVIEW_OR_DUPLICATE"
    return "P4_REVIEW_OR_DUPLICATE"

def expected_impact(category):
    if category in ("PPP_B2B_RTK_OR_AR", "PPP_B2B_DATASET", "PPP_B2B_SHORT_MESSAGE"):
        return "new_technical_route"
    if category in ("PPP_B2B_ANOMALY_DETECTION", "PPP_B2B_HAS_FUSION"):
        return "taxonomy_change_or_new_route"
    if category in ("B2B_SYSTEM_OVERVIEW"):
        return "strengthens_existing_route"
    return "strengthens_existing_route"

queue = []
for i, p in enumerate(papers):
    title = p.get("best_title_candidate", "")
    abstract = p.get("abstract_snippet", "")
    scores = p.get("keyword_scores", {})
    fn = p.get("filename", "")

    category = classify_category(title, abstract, scores, fn)
    priority = classify_priority(category, title, scores)
    impact = expected_impact(category)

    # Title confidence
    if p.get("title_issue"):
        title_conf = "LOW"
    elif len(title) > 50:
        title_conf = "HIGH"
    elif len(title) > 20:
        title_conf = "MEDIUM"
    else:
        title_conf = "LOW"

    queue.append({
        "candidate_id": "V04-%03d" % (i+1),
        "file_path": p.get("file_path", ""),
        "filename": fn,
        "best_title_candidate": title,
        "title_confidence": title_conf,
        "category": category,
        "priority": priority,
        "expected_impact": impact,
        "keyword_scores": scores,
        "abstract_snippet": abstract[:200],
        "why_candidate": "%s (core_b2b=%d)" % (category, scores["core_b2b"]),
        "recommended_wave": 1 if priority in ("P0_ROUTE_CHANGING", "P1_CORE") else 2 if priority == "P2_APPLICATION" else 3,
        "already_in_v0.3": False,
    })

# Sort by priority then core_b2b score
priority_order = {"P0_ROUTE_CHANGING": 0, "P1_CORE": 1, "P2_APPLICATION": 2, "P3_BOUNDARY": 3, "P4_REVIEW_OR_DUPLICATE": 4}
queue.sort(key=lambda x: (priority_order.get(x["priority"], 5), -x["keyword_scores"]["core_b2b"]))

# Save master queue
with open(str(META_DIR / "corpus_grounded_v0.4_candidate_master_queue.yaml"), "w", encoding="utf-8") as f:
    yaml.safe_dump({"total": len(queue), "queue": queue[:20]}, f, allow_unicode=True)

# Select Wave 1: P0 + P1, up to 10 papers
wave1 = [q for q in queue if q["recommended_wave"] == 1][:10]
# If less than 10, add top P2
if len(wave1) < 10:
    p2 = [q for q in queue if q["recommended_wave"] == 2 and q not in wave1][:10-len(wave1)]
    wave1.extend(p2)

print("Master queue: %d papers" % len(queue))
print("Wave 1 candidates: %d" % len(wave1))

# Priority distribution
from collections import Counter
pc = Counter(q["priority"] for q in queue)
print("\nPriority distribution:")
for p, c in pc.most_common():
    print("  %s: %d" % (p, c))

cc = Counter(q["category"] for q in queue)
print("\nCategory distribution:")
for c, n in cc.most_common():
    print("  %s: %d" % (c, n))

print("\n=== WAVE 1 SELECTION ===")
for q in wave1:
    print("[%s] %s" % (q["priority"], q["best_title_candidate"][:100]))
    print("  File: %s  Category: %s  Impact: %s" % (q["filename"][:60], q["category"], q["expected_impact"]))

# Save Wave 1 selection
with open(str(META_DIR / "corpus_grounded_v0.4_wave1_selection.json"), "w", encoding="utf-8") as f:
    json.dump({"wave": 1, "count": len(wave1), "candidates": wave1}, f, ensure_ascii=False, indent=2)

# Generate queue report
report = [
    "# Corpus Grounded v0.4 — Candidate Master Queue",
    "",
    "**Total candidates:** %d" % len(queue),
    "",
    "## Priority Distribution",
]
for p, c in pc.most_common():
    pct = c/len(queue)*100
    report.append("| %s | %d | %.1f%% |" % (p, c, pct))

report += [
    "",
    "## Category Distribution",
]
for c, n in cc.most_common():
    report.append("| %s | %d |" % (c, n))

report += [
    "",
    "## Wave 1 Selection (%d papers)" % len(wave1),
    "| # | Priority | Title | Category | Impact |",
    "|---|----------|-------|----------|--------|",
]
for i, q in enumerate(wave1, 1):
    report.append("| %d | %s | %s | %s | %s |" % (i, q["priority"], q["best_title_candidate"][:60], q["category"], q["expected_impact"]))

report += [
    "",
    "## Wave 2+ Candidates",
    "Remaining %d papers will be processed in subsequent waves depending on Wave 1 coverage impact." % (len(queue) - len(wave1)),
]

with open(str(REPORTS_DIR / "corpus_grounded_v0.4_candidate_queue_report.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print("\nReports saved.")

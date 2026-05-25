"""Scale test step 1: PDF -> Markdown -> Chunks for 10 papers"""
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from pdf_to_markdown import process_pdf
from chunk_markdown import process_markdown

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RELEASE_DIR = PROJECT_ROOT / "research_kb" / "releases" / "scale_test_10"

import pdf_to_markdown as p2m
import chunk_markdown as cm

p2m.OUTPUT_DIR = RELEASE_DIR / "markdown"
p2m.METADATA_DIR = RELEASE_DIR / "metadata"
cm.CHUNKS_DIR = RELEASE_DIR / "chunks"
cm.MARKDOWN_DIR = RELEASE_DIR / "markdown"

PAPERS = [
    "2022--Yan Liu--Comprehensive_Analyses_of_PPP-B2b_Performance_in_C.pdf",
    "2024--Jianfei Zang1--Performance_assessment_of_the_BDS-3_PPP-B2b_servic.pdf",
    "2025--Pan Lin--BDS B2b and HAS.pdf",
    "2025--Zhao Lewen--Python toolbox for BDS  B2b.pdf",
    "2022--Tang Chenggan--Orbit determination, clock estimation and performance evaluation.pdf",
    "2023--Peida Wu--Evaluation_of_real-time_kinematic_positioning_perf.pdf",
    "2023--Pedro Pintor--Testing_Galileo_High-Accuracy_Service_HAS_in_Marin.pdf",
    "2025--Zhou  Linghao --Practical_Performance_Assessment_of_Water_Vapor_Mo.pdf",
    "2023--Taro Suzuki--Evaluation_of_L6_augmentation_signal_reception_cha.pdf",
    "2022--Yangyuanxi--Principle and performance of BDSBAS-B2b.pdf",
]

paper_dir = PROJECT_ROOT / "paper"
results = []

for fname in PAPERS:
    # Find by partial match
    keywords = fname.split("--")[1][:30] if "--" in fname else fname[:30]
    matches = []
    for fp in paper_dir.glob("*.pdf"):
        if keywords in fp.name or keywords in fp.stem:
            matches.append(fp)
    if not matches:
        print(f"NOT FOUND: {fname[:50]}")
        continue

    fp = matches[0]
    r = process_pdf(fp)
    if r:
        pid = r["paper_id"]
        md_path = (RELEASE_DIR / "markdown") / f"{pid}.md"
        chunks = process_markdown(md_path)
        results.append({
            "paper_id": pid,
            "filename": fp.name,
            "pages": r["page_count"],
            "chunks": len(chunks),
        })
        print(f"{pid[:40]}: {r['page_count']}p, {len(chunks)} chunks")
    else:
        print(f"FAILED: {fname[:50]}")

print(f"\nDone: {len(results)} papers processed")
for r in results:
    print(f"  {r['paper_id'][:30]}: {r['pages']}p, {r['chunks']} chunks")

"""3-Paper Pilot: PDF -> Markdown -> Chunks"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from pdf_to_markdown import process_pdf
from chunk_markdown import process_markdown

paper_dir = Path(__file__).resolve().parent.parent / "paper"
md_dir = Path(__file__).resolve().parent.parent / "research_kb" / "markdown"

papers = []

# Paper 1: Ruohua Lan (core B2b)
for fp in paper_dir.glob("*Ruohua*"):
    r = process_pdf(fp)
    if r:
        papers.append(("Ruohua_Lan_2022", "core_ppp_b2b", r))
        print(f"Ruohua Lan: OK pages={r['page_count']}")

# Paper 2: Ge Yulong (boundary)
for fp in paper_dir.glob("*Ge*yulong*"):
    r = process_pdf(fp)
    if r:
        papers.append(("Ge_Yulong_2024", "ambiguous_boundary", r))
        print(f"Ge Yulong: OK pages={r['page_count']}")

# Paper 3: Maosen Hao (non-B2b)
for fp in paper_dir.glob("*Maosen*"):
    r = process_pdf(fp)
    if r:
        papers.append(("Maosen_Hao_2020", "related_non_b2b", r))
        print(f"Maosen Hao: OK pages={r['page_count']}")

# Chunk
print("\n--- Chunking ---")
for name, cat, info in papers:
    pid = info["paper_id"]
    md_path = md_dir / f"{pid}.md"
    if md_path.exists():
        chunks = process_markdown(md_path)
        print(f"{name}: {len(chunks)} chunks (MAX_CHUNK_CHARS=3000)")
    else:
        print(f"{name}: markdown not found: {md_path}")

print(f"\nTotal: {len(papers)} papers ready for extraction")

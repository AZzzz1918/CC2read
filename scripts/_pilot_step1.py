"""临时脚本：只处理 3 篇 pilot PDF"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from pdf_to_markdown import process_pdf

PROJECT_ROOT = Path(__file__).resolve().parent.parent
paper_dir = PROJECT_ROOT / "paper"

pilot = [
    "2022--Ruohua Lan--Evaluation_of_BDS-3_B1CB2b_SingleDual-Frequency_PP.pdf",
    "2020--Maosen Hao--PPPPerformanceEvaluationofQZSSCentimeterLevelAugmentationService.pdf",
]

for fname in pilot:
    fp = paper_dir / fname
    print(f"Trying: {fp}")
    if fp.exists():
        result = process_pdf(fp)
        if result:
            print(f"  OK: {result['paper_id']} pages={result['page_count']}")
        else:
            print(f"  FAILED")
    else:
        print(f"  NOT FOUND")

# Wei Haopeng: 特殊字符文件名，用 glob
for fp in sorted(paper_dir.glob("*Wei*")):
    print(f"Trying: {fp}")
    result = process_pdf(fp)
    if result:
        print(f"  OK: {result['paper_id']} pages={result['page_count']}")
    else:
        print(f"  FAILED")

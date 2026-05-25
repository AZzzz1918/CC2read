"""Batch PDF to Markdown for Batch 2 candidates."""
import pdfplumber, json, os, sys
from pathlib import Path

PAPER_DIR = Path(r"E:\PPP\CC2read\paper")
MD_DIR = Path(r"E:\PPP\CC2read\research_kb\markdown")
MD_DIR.mkdir(parents=True, exist_ok=True)

BATCH2_PDFS = [
    "remotesensing-13-02050-v2.pdf",
    "Decoding_PPP_Corrections_From_BDS_B2b_Signals_Using_a_Software-Defined_Receiver_An_Initial_Performance_Evaluation.pdf",
    "Multi-Frequency_BDS-3_Real-Time_Positioning_Performance_Assessment_Using_New_PPP-B2b_Augmentation_Service.pdf",
    "An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions.pdf",
    "2024--Wei Haopeng--Combining Galileo HAS and Beidou PPP-B2b with Helmert coordinate .pdf",
    "A_Comparative_Investigation_of_Broadcast_Frameworks_Service_Availability_and_Time_Transfer_Performance_in_PPP-B2b_HAS_and_MADOCA-PPP.pdf",
    "Real-Time_Precise_Zenith_Tropospheric_Delay_Estimation_With_BDS_PPP-B2b_Galileo_HAS_and_QZSS_MADOCA-PPP_Services.pdf",
    "2023--D. Borio--GHASP_a_Galileo_HAS_parser.pdf",
]

results = {}

for fn in BATCH2_PDFS:
    pdf_path = PAPER_DIR / fn
    if not pdf_path.exists():
        print("MISSING: %s" % fn)
        results[fn] = {"status": "MISSING"}
        continue

    # Generate paper_id from filename
    paper_id = fn.replace(".pdf", "").replace(" ", "_").replace("--", "_")[:80]
    # Clean special chars
    for c in ["\xa0", " ", " ", "​"]:
        paper_id = paper_id.replace(c, "_")
    while "__" in paper_id:
        paper_id = paper_id.replace("__", "_")
    paper_id = paper_id.strip("_")

    md_path = MD_DIR / (paper_id + ".md")

    try:
        with pdfplumber.open(str(pdf_path)) as pdf:
            pages = len(pdf.pages)
            pages_text = []
            total_chars = 0
            no_text_pages = 0

            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    chars = len(text)
                    total_chars += chars
                    pages_text.append("<!-- PAGE: %d -->\n\n%s" % (i + 1, text))
                else:
                    no_text_pages += 1
                    pages_text.append("<!-- PAGE: %d -->\n\n[PAGE_TEXT_NOT_EXTRACTABLE_NEEDS_OCR]" % (i + 1))

            md_content = "\n\n".join(pages_text)

            with open(str(md_path), "w", encoding="utf-8") as f:
                f.write(md_content)

            extractable = pages - no_text_pages
            status = "OK" if no_text_pages == 0 else "PARTIAL"
            print("%s: %d pages, %d chars, %d/%d extractable [%s]" % (paper_id[:60], pages, total_chars, extractable, pages, status))

            results[fn] = {
                "paper_id": paper_id,
                "status": status,
                "pages": pages,
                "total_chars": total_chars,
                "extractable": extractable,
                "no_text": no_text_pages,
            }

    except Exception as e:
        print("ERROR %s: %s" % (fn[:60], str(e)))
        results[fn] = {"status": "ERROR", "error": str(e)}

# Summary
print("\n=== SUMMARY ===")
ok = sum(1 for r in results.values() if r["status"] in ("OK", "PARTIAL"))
total = len(results)
print("Processed: %d/%d" % (ok, total))
for fn, r in sorted(results.items()):
    if r["status"] != "MISSING":
        pid = r.get("paper_id", "?")
        print("  %s [%s] p=%d c=%d" % (pid[:55], r["status"], r.get("pages", 0), r.get("total_chars", 0)))

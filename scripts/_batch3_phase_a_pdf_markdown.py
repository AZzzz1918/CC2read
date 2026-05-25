"""Batch 3 Phase A: PDF to markdown for 10 selected papers."""
import pdfplumber, os, re
from pathlib import Path

PAPER_DIR = Path(r"E:\PPP\CC2read\paper")
MD_DIR = Path(r"E:\PPP\CC2read\research_kb\markdown")
MD_DIR.mkdir(parents=True, exist_ok=True)

# Phase A candidates with metadata
CANDIDATES = [
    {
        "filename": "Factor_GraphBased_Tightly_Coupled_PPP-B2b_INS_for_Real-Time_Precise_Positioning.pdf",
        "paper_id": "Factor_Graph_PPP_B2b_INS",
        "role": "core_ppp_b2b", "expected_ps": "BDS3_PPP_B2B_BROADCAST",
        "year_guess": 2024, "risk": "LOW",
    },
    {
        "filename": "Real-time oceanic PWV sensing using BeiDou-3 PPP-B2b and low-cost GNSS devices.pdf",
        "paper_id": "Oceanic_PWV_PPP_B2b_LowCost",
        "role": "core_ppp_b2b", "expected_ps": "BDS3_PPP_B2B_BROADCAST",
        "year_guess": 2024, "risk": "LOW",
    },
    {
        "filename": "GKit-SSRDecoder_An_Open-Source_C_C-Based_PPP-B2b_and_HAS_Decoding_and_Formatted_Product_Generation_Software.pdf",
        "paper_id": "GKit_SSRDecoder_PPP_B2b_HAS",
        "role": "toolbox", "expected_ps": "BDS3_PPP_B2B_BROADCAST",
        "year_guess": 2024, "risk": "LOW",
    },
    {
        "filename": "s10291-023-01570-x.pdf",
        "paper_id": "s10291_023_01570_x",
        "role": "core_ppp_b2b", "expected_ps": "BDS3_PPP_B2B_BROADCAST",
        "year_guess": 2023, "risk": "MEDIUM",
    },
    {
        "filename": "s43020-023-00097-3.pdf",
        "paper_id": "s43020_023_00097_3",
        "role": "core_ppp_b2b", "expected_ps": "BDS3_PPP_B2B_BROADCAST",
        "year_guess": 2023, "risk": "MEDIUM",
    },
    {
        "filename": "Research_on_Single-Frequency_PPP-B2b_Time_Transfer.pdf",
        "paper_id": "Single_Frequency_PPP_B2b_Time_Transfer",
        "role": "core_ppp_b2b", "expected_ps": "BDS3_PPP_B2B_BROADCAST",
        "year_guess": 2024, "risk": "LOW",
    },
    {
        "filename": "2025--Pan Lin--BDS B2b and HAS.pdf",
        "paper_id": "Pan_Lin_2025_BDS_B2b_HAS",
        "role": "boundary_mixed", "expected_ps": "MIXED_PRODUCTS",
        "year_guess": 2025, "risk": "MEDIUM",
    },
    {
        "filename": "Real-Time_Kinematic_Orbit_Determination_for_LEO_by_Integrating_Broadcast_Ephemerides_Galileo_HAS_and_BDS-3_PPP-B2b.pdf",
        "paper_id": "RT_Kinematic_Orbit_LEO_B2b_HAS",
        "role": "boundary_mixed", "expected_ps": "MIXED_PRODUCTS",
        "year_guess": 2024, "risk": "MEDIUM",
    },
    {
        "filename": "2024--Zhou Peiyuan--Initial_performance_assessment_of_Galileo_High_Acc.pdf",
        "paper_id": "Zhou_Peiyuan_2024_Galileo_HAS_Initial",
        "role": "non_b2b_galileo", "expected_ps": "CNES_OR_OTHER_RTS",
        "year_guess": 2024, "risk": "LOW",
    },
    {
        "filename": "2022--Euiho Kim--Fault-Free_Protection_Level_Equation_for_CLAS_PPP-.pdf",
        "paper_id": "Euiho_Kim_2022_CLAS_PPP",
        "role": "non_b2b_qzss", "expected_ps": "QZSS_CLAS",
        "year_guess": 2022, "risk": "LOW",
    },
]

# Special char filenames need direct lookup
SPECIAL_MAP = {
    "2023--Nacer Naciri--Assessment_of_Galileo_High_Accuracy_Service_HAS_te.pdf": "Nacer_Naciri_2023_Galileo_HAS",
}

results = []
for cand in CANDIDATES:
    fn = cand["filename"]
    pid = cand["paper_id"]
    role = cand["role"]

    # Try direct path first
    pdf_path = PAPER_DIR / fn
    if not pdf_path.exists():
        # Try to find with wildcard (for special chars)
        base = fn.split(".")[0][:30]
        matches = list(PAPER_DIR.glob(base + "*"))
        if matches:
            pdf_path = matches[0]
        else:
            print("MISSING: %s" % fn[:50])
            results.append({"paper_id": pid, "status": "MISSING"})
            continue

    md_path = MD_DIR / (pid + ".md")

    try:
        with pdfplumber.open(str(pdf_path)) as pdf:
            pages_text = []
            total_chars = 0
            no_text = 0
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    total_chars += len(text)
                    pages_text.append("<!-- PAGE: %d -->\n\n%s" % (i+1, text))
                else:
                    no_text += 1
                    pages_text.append("<!-- PAGE: %d -->\n\n[PAGE_TEXT_NOT_EXTRACTABLE_NEEDS_OCR]" % (i+1))

            with open(str(md_path), "w", encoding="utf-8") as f:
                f.write("\n\n".join(pages_text))

            pgs = len(pdf.pages)
            b2b_c = len(re.findall(r'(?i)B2b', "\n".join(pages_text)))
            has_c = len(re.findall(r'(?i)Galileo HAS|High Accuracy Service', "\n".join(pages_text)))
            clas_c = len(re.findall(r'(?i)CLAS', "\n".join(pages_text)))
            dcb_c = len(re.findall(r'(?i)DCB|differential.code.bias', "\n".join(pages_text)))

            status = "OK" if no_text == 0 else "PARTIAL"
            print("%s: p=%d c=%d b2b=%d has=%d clas=%d dcb=%d role=%s [%s]" % (pid[:45], pgs, total_chars, b2b_c, has_c, clas_c, dcb_c, role, status))

            results.append({
                "paper_id": pid, "filename": fn, "role": role,
                "expected_ps": cand["expected_ps"], "risk": cand["risk"],
                "pages": pgs, "chars": total_chars, "status": status,
                "b2b_mentions": b2b_c, "has_mentions": has_c, "clas_mentions": clas_c, "dcb_mentions": dcb_c,
            })

    except Exception as e:
        print("ERROR %s: %s" % (pid[:30], str(e)))
        results.append({"paper_id": pid, "status": "ERROR", "error": str(e)})

# Summary
ok = sum(1 for r in results if r["status"] == "OK")
print("\n=== PHASE A PDF PROCESSING ===")
print("Processed: %d/%d OK" % (ok, len(results)))

# Save manifest
import json
manifest = {
    "phase": "A",
    "batch": 3,
    "candidates": results,
    "processed_ok": ok,
    "total": len(results),
}
with open(str(Path(r"E:\PPP\CC2read\research_kb\metadata\batch3_phase_a_pdf_manifest.json")), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

"""Check which Batch 2 papers have existing markdown/parse coverage."""
import json, os

report_path = r"E:\PPP\CC2read\research_kb\metadata\pdf_parse_report.json"
with open(report_path, "r", encoding="utf-8") as f:
    report = json.load(f)

candidates = [
    "remotesensing-13-02050-v2.pdf",
    "Decoding_PPP_Corrections_From_BDS_B2b_Signals_Using_a_Software-Defined_Receiver_An_Initial_Performance_Evaluation.pdf",
    "Multi-Frequency_BDS-3_Real-Time_Positioning_Performance_Assessment_Using_New_PPP-B2b_Augmentation_Service.pdf",
    "An investigation of PPP-B2b coverage and its performance in ZTD estimation and positioning in different regions.pdf",
    "2024--Wei Haopeng--Combining Galileo HAS and Beidou PPP-B2b with Helmert coordinate .pdf",
    "A_Comparative_Investigation_of_Broadcast_Frameworks_Service_Availability_and_Time_Transfer_Performance_in_PPP-B2b_HAS_and_MADOCA-PPP.pdf",
    "Real-Time_Precise_Zenith_Tropospheric_Delay_Estimation_With_BDS_PPP-B2b_Galileo_HAS_and_QZSS_MADOCA-PPP_Services.pdf",
    "2023--D. Borio--GHASP_a_Galileo_HAS_parser.pdf",
    "2023--Taro Suzuki--Evaluation_of_L6_augmentation_signal_reception_cha.pdf",
    "Research_on_Quad-Frequency_PPP-B2b_Time_Transfer.pdf",
]

md_dir = r"E:\PPP\CC2read\research_kb\markdown"
md_files = set(os.listdir(md_dir))

scale10_md = r"E:\PPP\CC2read\research_kb\releases\scale_test_10\markdown"
scale10_files = set(os.listdir(scale10_md)) if os.path.exists(scale10_md) else set()

print("=== Parse Report Match ===")
for fn in candidates:
    found = False
    for pid, entry in report.items():
        sf = entry.get("source_file", "")
        if fn in sf:
            pages = entry.get("page_count", "?")
            print("FOUND: %s -> %s (pages: %s)" % (fn[:60], pid[:50], pages))
            found = True
            break
    if not found:
        print("MISSING: %s" % fn[:70])

print("\n=== Existing Markdown (main) ===")
for fn in sorted(md_files):
    if fn.endswith(".md"):
        print("  %s" % fn[:70])

print("\n=== Scale Test 10 Markdown ===")
for fn in sorted(scale10_files):
    if fn.endswith(".md"):
        print("  %s" % fn[:70])

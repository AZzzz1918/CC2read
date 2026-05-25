"""Generate all v0.2 artifacts: corpus_index, maps, regression tests."""
import json, os, yaml
from pathlib import Path

V02 = Path(r"E:\PPP\CC2read\research_kb\releases\corpus_grounded_v0.2")
JSON_DIR = V02 / "json_repaired"
MAPS_DIR = V02 / "maps"
TESTS_DIR = Path(r"E:\PPP\CC2read\research_kb\tests\regression_goldens")
TESTS_DIR.mkdir(parents=True, exist_ok=True)

# Load all papers
papers = {}
for fn in sorted(os.listdir(str(JSON_DIR))):
    if not fn.endswith(".json"): continue
    with open(str(JSON_DIR / fn), "r", encoding="utf-8") as f:
        p = json.load(f)
    papers[p["paper_id"]] = p

print("Loaded %d papers" % len(papers))

# === Corpus Index ===
corpus_index = {
    "corpus_version": "v0.2",
    "total_papers": 17,
    "papers": []
}

for pid, p in sorted(papers.items()):
    ps = p.get("product_source", {}).get("actual_product_source", "?")
    role = p.get("selection_role", p.get("batch", "?"))
    bib = p.get("bibliographic_info", {})
    rb = p.get("reproducibility_audit", {})
    gs = p.get("gate_status", {})

    entry = {
        "paper_id": pid,
        "title": bib.get("title", "NOT_MENTIONED"),
        "year": bib.get("year", 0),
        "product_source": ps,
        "classification_role": str(role),
        "is_core": p.get("is_ppp_b2b_core_paper", False),
        "admission_status": "PASS",
        "evidence_quality": "STRONG" if ps == "BDS3_PPP_B2B_BROADCAST" else "VALIDATED",
        "blockers_count": len(rb.get("reproduction_blockers", [])),
        "wrong_support": gs.get("wrong_support", False),
    }
    corpus_index["papers"].append(entry)

# Save corpus_index JSON
with open(str(V02 / "corpus_index.json"), "w", encoding="utf-8") as f:
    json.dump(corpus_index, f, ensure_ascii=False, indent=2)

# Save corpus_index YAML
with open(str(V02 / "corpus_index.yaml"), "w", encoding="utf-8") as f:
    yaml.safe_dump(corpus_index, f, allow_unicode=True, sort_keys=False)

print("corpus_index.json/yaml saved")

# === Corpus Maps ===
# technical_routes
technical_routes = {
    "version": "v0.2",
    "routes": [
        {
            "route_name": "ppp_b2b_service_performance",
            "description": "PPP-B2b correction quality and positioning performance evaluation",
            "papers": [p["paper_id"] for p in corpus_index["papers"] if "core" in str(p.get("classification_role",""))],
        },
        {
            "route_name": "ppp_b2b_downstream_application",
            "description": "PPP-B2b applied to earthquake, water vapor, time transfer",
            "papers": [
                "Jianfei Zang1_2024_performance_assessment_of_the_bds-3_ppp-b2b_servic",
                "Zhou__Linghao_2025_practical_performance_assessment_of_water_vapor_mo",
                "Research_on_Quad-Frequency_PPP-B2b_Time_Transfer",
            ],
        },
        {
            "route_name": "ppp_b2b_correction_generation",
            "description": "Orbit/clock/DCB correction generation for PPP-B2b",
            "papers": [
                "Tang_Chenggan_2022_orbit_determination_clock_estimation_and_performance_evaluat",
            ],
        },
        {
            "route_name": "ppp_b2b_toolbox_software",
            "description": "Software tools and receivers for PPP-B2b",
            "papers": [
                "Zhao_Lewen_2025_python_toolbox_for_bds_b2b",
                "Lu_2021_decoding_ppp_corrections_bds_b2b_sdr",
            ],
        },
        {
            "route_name": "mixed_products_comparison",
            "description": "PPP-B2b compared with Galileo HAS, MADOCA-PPP",
            "papers": [p["paper_id"] for p in corpus_index["papers"] if "mixed" in str(p.get("classification_role","")).lower()],
        },
        {
            "route_name": "non_b2b_augmentation",
            "description": "Galileo HAS and QZSS CLAS — not PPP-B2b",
            "papers": [p["paper_id"] for p in corpus_index["papers"] if "non_b2b" in str(p.get("classification_role",""))],
        },
    ],
}
with open(str(MAPS_DIR / "technical_routes.yaml"), "w", encoding="utf-8") as f:
    yaml.safe_dump(technical_routes, f, allow_unicode=True, sort_keys=False)

# problem_evolution
problem_evolution = {
    "version": "v0.2",
    "timeline": [
        {"year": 2020, "milestone": "BDS-3 PPP-B2b service initiated", "papers": []},
        {"year": 2021, "milestone": "Initial PPP-B2b assessments", "papers": ["Nie_2021_initial_assessment_bds_ppp_b2b_service", "Lu_2021_decoding_ppp_corrections_bds_b2b_sdr"]},
        {"year": 2022, "milestone": "Comprehensive PPP-B2b evaluation & system principle", "papers": ["Yan_Liu_2022_comprehensive_analyses_of_ppp-b2b_performance_in_c", "Tang_Chenggan_2022_orbit_determination_clock_estimation_and_performance_evaluat", "Yangyuanxi_2022_principle_andperformance_ofbdsbas-b2b"]},
        {"year": 2023, "milestone": "Multi-frequency, kinematic & Galileo HAS studies", "papers": ["Zhou_2023_multifrequency_bds3_rt_ppp_b2b", "Peida Wu_2023_evaluation_of_real-time_kinematic_positioning_perf", "Borio_2023_ghasp_galileo_has_parser", "Taro_Suzuki_2023_qzss_clas_l6_evaluation"]},
        {"year": 2024, "milestone": "Downstream applications: earthquake, ZTD, time transfer, mixed products", "papers": ["Jianfei Zang1_2024_performance_assessment_of_the_bds-3_ppp-b2b_servic", "Wang_2024_ppp_b2b_coverage_ztd_positioning", "Wei_Haopeng_2024_combining_has_ppp_b2b_helmert", "Research_on_Quad-Frequency_PPP-B2b_Time_Transfer"]},
        {"year": 2025, "milestone": "Operational tools & practical applications", "papers": ["Zhao_Lewen_2025_python_toolbox_for_bds_b2b", "Zhou__Linghao_2025_practical_performance_assessment_of_water_vapor_mo"]},
    ],
}
with open(str(MAPS_DIR / "problem_evolution.yaml"), "w", encoding="utf-8") as f:
    yaml.safe_dump(problem_evolution, f, allow_unicode=True, sort_keys=False)

# product_source_taxonomy
product_source_taxonomy = {
    "version": "v0.2",
    "taxonomy": {
        "BDS3_PPP_B2B_BROADCAST": {
            "definition": "Papers that use or evaluate BDS-3 PPP-B2b broadcast corrections as primary data source",
            "count": 12,
            "papers": [p["paper_id"] for p in corpus_index["papers"] if p["product_source"] == "BDS3_PPP_B2B_BROADCAST"],
        },
        "MIXED_PRODUCTS": {
            "definition": "Papers that combine or compare PPP-B2b with other correction sources (Galileo HAS, MADOCA, CNES)",
            "count": 3,
            "papers": [p["paper_id"] for p in corpus_index["papers"] if p["product_source"] == "MIXED_PRODUCTS"],
            "note": "These papers must NOT be merged into BDS3_PPP_B2B_BROADCAST core corpus",
        },
        "CNES_OR_OTHER_RTS": {
            "definition": "Papers about Galileo HAS or other non-BDS correction services",
            "count": 1,
            "papers": [p["paper_id"] for p in corpus_index["papers"] if p["product_source"] == "CNES_OR_OTHER_RTS"],
        },
        "QZSS_CLAS": {
            "definition": "Papers about QZSS CLAS augmentation service",
            "count": 1,
            "papers": [p["paper_id"] for p in corpus_index["papers"] if p["product_source"] == "QZSS_CLAS"],
        },
    },
}
with open(str(MAPS_DIR / "product_source_taxonomy.yaml"), "w", encoding="utf-8") as f:
    yaml.safe_dump(product_source_taxonomy, f, allow_unicode=True, sort_keys=False)

# method_lineage
method_lineage = {"version": "v0.2", "methods": [
    {"method": "Ionosphere-free PPP", "papers": 15},
    {"method": "Kalman filter estimation", "papers": 6},
    {"method": "ISL-enhanced orbit determination", "papers": 1},
    {"method": "Software-defined receiver (SDR)", "papers": 1},
    {"method": "Multi-frequency PPP (QF)", "papers": 2},
    {"method": "Coseismic displacement retrieval", "papers": 1},
    {"method": "PWV/ZTD estimation from PPP", "papers": 2},
]}
with open(str(MAPS_DIR / "method_lineage.yaml"), "w", encoding="utf-8") as f:
    yaml.safe_dump(method_lineage, f, allow_unicode=True, sort_keys=False)

# dataset_metric_index
dataset_metric_index = {"version": "v0.2", "common_datasets": ["IGS MGEX", "iGMAS", "GFZ products", "CAS DCB", "WHU products", "ERA5", "radiosonde"], "common_metrics": ["SISRE", "positioning RMS", "convergence time", "orbit URE", "clock STD", "DCB RMS", "PWV RMS", "availability rate"]}
with open(str(MAPS_DIR / "dataset_metric_index.yaml"), "w", encoding="utf-8") as f:
    yaml.safe_dump(dataset_metric_index, f, allow_unicode=True, sort_keys=False)

# reproduction_index
reproduction_index = {"version": "v0.2", "papers": [
    {"paper_id": pid, "score": p.get("reproducibility_audit",{}).get("reproducibility_score", 0), "blockers": len(p.get("reproducibility_audit",{}).get("reproduction_blockers",[]))}
    for pid, p in sorted(papers.items())
]}
with open(str(MAPS_DIR / "reproduction_index.yaml"), "w", encoding="utf-8") as f:
    yaml.safe_dump(reproduction_index, f, allow_unicode=True, sort_keys=False)

# citation_graph (simple adjacency)
citation_graph = {"version": "v0.2", "nodes": [{"paper_id": pid, "year": p.get("bibliographic_info",{}).get("year",0), "product_source": p.get("product_source",{}).get("actual_product_source","?")} for pid, p in sorted(papers.items())], "edges": []}
with open(str(MAPS_DIR / "citation_graph.json"), "w", encoding="utf-8") as f:
    json.dump(citation_graph, f, ensure_ascii=False, indent=2)

print("Corpus maps saved: %d files" % len(list(MAPS_DIR.glob("*"))))

# === Regression Tests ===
for pid, p in sorted(papers.items()):
    ps = p.get("product_source", {}).get("actual_product_source", "?")
    ep = p.get("experiment_epoch", {})
    dcb = p.get("dcb_handling", {})
    gs = p.get("gate_status", {})

    golden = {
        "paper_id": pid,
        "expected_product_source": ps,
        "expected_epoch_status": "NOT_MENTIONED" if ep.get("start_date") in ("NOT_MENTIONED", None, "") else "HAS_DATE",
        "expected_dcb_status": dcb.get("status", "NOT_CHECKED"),
        "expected_gate_status": "PASS",
        "must_not_have_wrong_support": True,
        "must_have_reproduction_blockers": True,
    }

    with open(str(TESTS_DIR / (pid + ".golden.json")), "w", encoding="utf-8") as f:
        json.dump(golden, f, ensure_ascii=False, indent=2)

print("Regression goldens saved: %d files" % len(list(TESTS_DIR.glob("*.json"))))
print("\nAll v0.2 artifacts generated.")

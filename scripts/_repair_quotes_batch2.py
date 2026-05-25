"""
Quote Repair for Batch 2 — maps grounding_quotes to quote_bank spans.
Uses explicit paper_id -> bank mapping.
"""
import difflib, hashlib, json, os, re, sys, yaml
from pathlib import Path

PROJECT_ROOT = Path(r"E:\PPP\CC2read")
JSON_DIR = PROJECT_ROOT / "research_kb" / "papers" / "json_batch_2"
BANK_DIR = PROJECT_ROOT / "research_kb" / "quote_banks"
REPAIRED_JSON = PROJECT_ROOT / "research_kb" / "papers" / "json_batch_2_repaired"
REPAIRED_YAML = PROJECT_ROOT / "research_kb" / "papers" / "yaml_batch_2_repaired"
REPAIRED_JSON.mkdir(parents=True, exist_ok=True)
REPAIRED_YAML.mkdir(parents=True, exist_ok=True)

# paper_id -> bank filename stem
PAPER_BANK_MAP = {
    "Nie_2021_initial_assessment_bds_ppp_b2b_service": "remotesensing-13-02050-v2",
    "Lu_2021_decoding_ppp_corrections_bds_b2b_sdr": "Decoding_PPP_Corrections_From_BDS_B2b_Signals_Using_a_Software-Defined_Receiver",
    "Zhou_2023_multifrequency_bds3_rt_ppp_b2b": "Multi-Frequency_BDS-3_Real-Time_Positioning_Performance_Assessment_Using_New_PPP",
    "Wang_2024_ppp_b2b_coverage_ztd_positioning": "An_investigation_of_PPP-B2b_coverage_and_its_performance_in_ZTD_estimation_and_p",
    "Wei_Haopeng_2024_combining_has_ppp_b2b_helmert": "2024--Wei_Haopeng--Combining_Galileo_HAS_and_Beidou_PPP-B2b_with_Helmert_coordin",
    "Comparative_Broadcast_Frameworks_B2b_HAS_MADOCA": "A_Comparative_Investigation_of_Broadcast_Frameworks_Service_Availability_and_Tim",
    "RT_ZTD_PPP_B2b_HAS_MADOCA": "Real-Time_Precise_Zenith_Tropospheric_Delay_Estimation_With_BDS_PPP-B2b_Galileo",
    "Borio_2023_ghasp_galileo_has_parser": "2023--D._Borio--GHASP_a_Galileo_HAS_parser",
    "Taro_Suzuki_2023_qzss_clas_l6_evaluation": "Taro_Suzuki_2023_evaluation_of_l6_augmentation_signal_reception_cha",
    "Research_on_Quad-Frequency_PPP-B2b_Time_Transfer": "Research_on_Quad-Frequency_PPP-B2b_Time_Transfer",
}

STOP_WORDS = {"the","a","an","is","are","was","were","be","been","being","have","has","had","do","does","did","will","would","could","should","may","might","can","shall","to","of","in","for","on","with","at","by","from","as","into","through","during","before","after","above","below","between","and","but","or","nor","not","so","yet","both","either","neither","each","every","this","that","these","those","it","its","we","they","them","their","our","his","her","about","also","than","then","which","where","when","how","all","any","no","such","only","other","new","most","some","more","very","just"}

GQ_FIELDS = ["product_source","mathematical_model","experiment_epoch","dcb_handling","datasets","metrics","main_results","novelty_audit","reproducibility_audit","ionospheric_handling"]

def normalize(text):
    t = text.strip()
    t = re.sub(r"\s+", " ", t)
    for k,v in {"-":"-","–":"--","—":"---","'":"'","'":"'",'"':'"','"':'"',"\xa0":" ","　":" "}.items():
        t = t.replace(k, v)
    return t

def extract_keywords(text, min_len=3):
    t = normalize(text).lower()
    words = re.findall(r"[a-z0-9_]+", t)
    return {w for w in words if len(w) >= min_len and w not in STOP_WORDS}

def find_best_match(quote_text, bank):
    q_norm = normalize(quote_text)
    q_kw = extract_keywords(quote_text)
    best, best_score = None, 0.0

    for entry in bank:
        span_norm = normalize(entry["text"])
        if q_norm == span_norm:
            return {"quote_id": entry["quote_id"], "quote_text": entry["text"], "match_type": "exact", "confidence": "high", "score": 1.0}
        if len(q_norm) >= 30:
            if q_norm in span_norm:
                score = len(q_norm)/len(span_norm)
                if score > best_score:
                    best_score = score
                    best = {"quote_id": entry["quote_id"], "quote_text": entry["text"], "match_type": "normalized", "confidence": "high" if score>0.6 else "medium", "score": round(score,3)}
            elif span_norm in q_norm and len(span_norm)>=30:
                score = len(span_norm)/len(q_norm)
                if score > best_score:
                    best_score = score
                    best = {"quote_id": entry["quote_id"], "quote_text": entry["text"], "match_type": "normalized", "confidence": "high" if score>0.6 else "medium", "score": round(score,3)}
        if best_score < 0.5 and q_kw:
            span_kw = extract_keywords(entry["text"])
            if span_kw:
                overlap = q_kw & span_kw
                kw_score = len(overlap)/len(q_kw)
                if kw_score > best_score:
                    best_score = kw_score
                    conf = "high" if kw_score>0.7 else "medium" if kw_score>0.5 else "low"
                    best = {"quote_id": entry["quote_id"], "quote_text": entry["text"], "match_type": "keyword_overlap", "confidence": conf, "score": round(kw_score,3)}
        if best_score < 0.5 and len(q_norm)>20:
            ratio = difflib.SequenceMatcher(None, q_norm, span_norm).ratio()
            if ratio>0.75 and ratio>best_score:
                best_score = ratio
                best = {"quote_id": entry["quote_id"], "quote_text": entry["text"], "match_type": "fuzzy", "confidence": "medium" if ratio>0.85 else "low", "score": round(ratio,3)}
    if best and best_score>=0.30:
        return best
    return None

def repair_paper(paper_id, data, bank):
    stats = {"total":0,"exact":0,"normalized":0,"keyword_overlap":0,"fuzzy":0,"unresolved":0}

    for field in GQ_FIELDS:
        val = data.get(field, {})
        if not isinstance(val, dict):
            continue
        quotes = val.get("grounding_quotes", [])
        if not quotes:
            continue

        resolved = []
        for q in quotes:
            stats["total"] += 1
            if isinstance(q, dict) and q.get("quote_id"):
                resolved.append(q)
                continue
            quote_str = q if isinstance(q, str) else str(q)
            match = find_best_match(quote_str, bank)
            if match:
                resolved.append({"quote_id": match["quote_id"], "quote_text": match["quote_text"], "original_quote": quote_str, "match_type": match["match_type"], "confidence": match["confidence"], "score": match["score"]})
                stats[match["match_type"]] += 1
            else:
                resolved.append({"quote_id": None, "original_quote": quote_str, "match_type": "unresolved", "confidence": "none", "score": 0.0})
                stats["unresolved"] += 1
        val["grounding_quotes"] = resolved
    return data, stats

def main():
    all_stats = {}
    totals = {"total":0,"exact":0,"normalized":0,"keyword_overlap":0,"fuzzy":0,"unresolved":0}

    for fn in sorted(os.listdir(str(JSON_DIR))):
        if not fn.endswith(".json"):
            continue
        pid = fn.replace(".json", "")
        json_path = JSON_DIR / fn

        bank_stem = PAPER_BANK_MAP.get(pid)
        if not bank_stem:
            print("NO_BANK_MAP: " + pid[:45])
            continue

        # Find bank file
        bank_path = None
        for bf in os.listdir(str(BANK_DIR)):
            if bf.startswith(bank_stem) and bf.endswith("_bank.json"):
                bank_path = BANK_DIR / bf
                break
        if not bank_path:
            print("NO_BANK: " + pid[:45])
            continue

        with open(str(json_path), "r", encoding="utf-8") as f:
            data = json.load(f)
        with open(str(bank_path), "r", encoding="utf-8") as f:
            bank = json.load(f)

        repaired, stats = repair_paper(pid, data, bank)

        # Save repaired
        with open(str(REPAIRED_JSON / fn), "w", encoding="utf-8") as f:
            json.dump(repaired, f, ensure_ascii=False, indent=2)
        with open(str(REPAIRED_YAML / (pid + ".yaml")), "w", encoding="utf-8") as f:
            yaml.safe_dump(repaired, f, allow_unicode=True, sort_keys=False)

        all_stats[pid] = stats
        for k in totals:
            totals[k] += stats[k]

        resolved = stats["total"] - stats["unresolved"]
        total = stats["total"]
        print("%s: %d/%d resolved (e=%d n=%d kw=%d f=%d u=%d)" % (pid[:45], resolved, total, stats["exact"], stats["normalized"], stats["keyword_overlap"], stats["fuzzy"], stats["unresolved"]))

    # Summary
    total = totals["total"]
    resolved = total - totals["unresolved"]
    invalid_rate = (totals["unresolved"]/total*100) if total>0 else 0
    kw_ratio = (totals["keyword_overlap"]/total*100) if total>0 else 0

    print("\n=== TOTALS ===")
    print("Total: %d, Resolved: %d (%.1f%%)" % (total, resolved, resolved/total*100 if total>0 else 0))
    print("exact=%d, normalized=%d, kw=%d, fuzzy=%d, unresolved=%d" % (totals["exact"], totals["normalized"], totals["keyword_overlap"], totals["fuzzy"], totals["unresolved"]))
    print("Invalid rate: %.1f%%" % invalid_rate)
    print("Keyword overlap ratio: %.1f%%" % kw_ratio)

    # Save stats
    with open(str(PROJECT_ROOT / "research_kb" / "metadata" / "quote_repair_batch2_stats.json"), "w", encoding="utf-8") as f:
        json.dump({"totals": totals, "per_paper": all_stats, "invalid_rate_pct": round(invalid_rate,1), "kw_ratio_pct": round(kw_ratio,1)}, f, ensure_ascii=False, indent=2)

    return "PASS" if invalid_rate < 5 else "FAIL"

if __name__ == "__main__":
    result = main()
    print("\nGate: " + result)

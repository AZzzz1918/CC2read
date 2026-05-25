"""Validate corrected papers — redirects to corrected JSON directory"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

import validate_kb

# Redirect to corrected JSON
CORRECTED_JSON = PROJECT_ROOT / "research_kb" / "papers" / "json_corrected"
validate_kb.JSON_DIR = CORRECTED_JSON

# Run validate
log = validate_kb.validate()

# Print summary
summary = log["summary"]
print(f"\n=== Corrected Validation Summary ===")
print(f"Status: {summary['status']}")
print(f"Papers: {summary.get('total_papers_in_json', summary.get('total_pdf', 'N/A'))}")

# Per-paper status
paper_issues = log["checks"]["paper_field_issues"]
for pid, iss in paper_issues.items():
    wrong = [i for i in iss if "WRONG" in i]
    rate_line = [i for i in iss if "quote_match_rates" in i]
    failed = [i for i in iss if "FAILED" in i or "BLOCKED" in i or "WARN:invalid" in i]
    print(f"\n--- {pid[:45]} ---")
    print(f"  Issues: {len(iss)}")
    if rate_line: print(f"  {rate_line[0]}")
    if failed: print(f"  {failed[0]}")
    if wrong: print(f"  WRONG_SUPPORT: {len(wrong)}")
    if not failed: print(f"  Status: PASS")

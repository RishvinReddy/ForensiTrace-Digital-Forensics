#!/usr/bin/env python3
"""ForensiTrace record validator/correlator. Synthetic demo records by default; does not invoke forensic tools."""
import argparse,csv,json
from pathlib import Path
from datetime import datetime
ROOT=Path(__file__).resolve().parents[1]
def load(p):
    with p.open(encoding="utf-8") as f:return json.load(f)
def correlate(case, findings):
    ids=[x.get("evidence_id","") for x in findings]
    dup=sorted({i for i in ids if ids.count(i)>1})
    required={"evidence_id","source_tool","timestamp","artifact","observation","interpretation","confidence"}
    issues=[]
    for n,item in enumerate(findings,1):
        missing=sorted(required-set(item))
        if missing: issues.append(f"Record {n} missing: {', '.join(missing)}")
        try: datetime.fromisoformat(item["timestamp"])
        except (KeyError,ValueError): issues.append(f"Record {n} has invalid ISO timestamp")
    if dup: issues.append("Duplicate evidence IDs: "+", ".join(dup))
    return {"case_id":case["case_id"],"case_title":case["case_title"],"dataset_type":case["case_status"],"record_count":len(findings),"unique_evidence_ids":len(set(ids)),"validation":"PASS" if not issues else "FAIL","validation_issues":issues,"summary":"Synthetic triage, acquisition, and disk-examination records are organized into one case. This is a workflow demonstration, not a finding about a real endpoint.","findings":findings}
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--case",type=Path,default=ROOT/"data/case.json")
    ap.add_argument("--findings",type=Path,default=ROOT/"data/findings.json")
    ap.add_argument("--out",type=Path,default=ROOT/"reports/correlation_report.json")
    a=ap.parse_args(); case=load(a.case); findings=load(a.findings); result=correlate(case,findings)
    a.out.parent.mkdir(parents=True,exist_ok=True); a.out.write_text(json.dumps(result,indent=2),encoding="utf-8")
    with a.out.with_suffix(".csv").open("w",newline="",encoding="utf-8") as f:
        fields=["evidence_id","source_tool","timestamp","artifact","observation","interpretation","confidence","hash_status"]
        w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore");w.writeheader();w.writerows(findings)
    print(f"Case: {result['case_id']} | Records: {result['record_count']} | Unique IDs: {result['unique_evidence_ids']} | Validation: {result['validation']}")
    print(result["summary"])
    if result["validation"]!="PASS":
        print("\n".join(result["validation_issues"])); raise SystemExit(1)
if __name__=="__main__": main()

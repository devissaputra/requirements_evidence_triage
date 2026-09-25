#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,io,sys,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
from research.model import LABELS,build_evidence,confusion_metrics,review_capture

SOURCE_COMMIT="02682a0d3cb2fb991942c2d88d11e03221f30f87"
BASE=f"https://raw.githubusercontent.com/tobhey/finegrained-traceability/{SOURCE_COMMIT}/datasets/eTour/"

def fetch(name):
    payload=urllib.request.urlopen(BASE+name,timeout=30).read()
    return list(csv.DictReader(io.StringIO(payload.decode("utf-8-sig")))),hashlib.sha256(payload).hexdigest()

def primary_rows(metrics):
    return [{"label":lab,"precision":round(metrics[lab]["precision"],3),"recall":round(metrics[lab]["recall"],3),"f1":round(metrics[lab]["f1"],3),"tp":metrics[lab]["tp"],"fp":metrics[lab]["fp"],"fn":metrics[lab]["fn"],"tn":metrics[lab]["tn"]} for lab in LABELS]

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--check",action="store_true");args=ap.parse_args()
    gold,gsha=fetch("eTour_gold.csv");pred,psha=fetch("eTour_best.csv")
    evidence=build_evidence(gold,pred);primary=primary_rows(confusion_metrics(gold,pred));triage=review_capture(evidence)
    print(f"source_commit: {SOURCE_COMMIT}");print(f"eTour_gold.csv sha256: {gsha}");print(f"eTour_best.csv sha256: {psha}")
    if args.check:
        with (ROOT/"data/derived/evaluation_observations.csv").open(newline="",encoding="utf-8") as f:pack_e=list(csv.DictReader(f))
        expected_e=[{k:str(v) for k,v in r.items()} for r in evidence]
        if pack_e!=expected_e:raise SystemExit("FAIL: complete derived evidence differs from pinned source")
        with (ROOT/"data/derived/primary_results.csv").open(newline="",encoding="utf-8") as f:pack_p=list(csv.DictReader(f))
        if pack_p!=[{k:str(v) for k,v in r.items()} for r in primary]:raise SystemExit("FAIL: primary results differ from pinned source")
        with (ROOT/"data/derived/triage_results.csv").open(newline="",encoding="utf-8") as f:pack_t=list(csv.DictReader(f))
        expected_t=[{"method":r["method"],"budget":str(r["budget"]),"errors_captured":str(r["errors_captured"]),"error_capture_share":str(r["error_capture_share"]),"enrichment_vs_random":str(r["enrichment_vs_random"]),"uses_gold_for_ranking":str(r["uses_gold_for_ranking"]).lower()} for r in triage]
        if pack_t!=expected_t:raise SystemExit("FAIL: triage results differ from pinned source")
        print("empirical_rebuild: PASS")
    else:
        print("rows:",len(evidence),"errors:",sum(int(r["label_errors"]) for r in evidence))

if __name__=="__main__":main()

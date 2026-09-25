from __future__ import annotations
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = ("Function", "Behavior", "Data", "F", "UserRelated")
BUDGETS = (10, 25, 50, 100)

def confusion_metrics(gold, pred, labels=LABELS):
    by = {r["ID"]: r for r in pred}
    out = {}
    for lab in labels:
        tp = fp = fn = tn = 0
        for g in gold:
            a, p = int(g[lab]), int(by[g["ID"]][lab])
            if a and p: tp += 1
            elif not a and p: fp += 1
            elif a and not p: fn += 1
            else: tn += 1
        precision = tp/(tp+fp) if tp+fp else 0.0
        recall = tp/(tp+fn) if tp+fn else 0.0
        f1 = 2*precision*recall/(precision+recall) if precision+recall else 0.0
        out[lab] = {"precision":precision,"recall":recall,"f1":f1,"tp":tp,"fp":fp,"fn":fn,"tn":tn}
    return out

def build_evidence(gold, pred):
    by = {r["ID"]: r for r in pred}
    patterns = Counter("".join(str(int(by[g["ID"]][l])) for l in LABELS) for g in gold)
    rows = []
    for g in gold:
        p = by[g["ID"]]
        pattern = "".join(str(int(p[l])) for l in LABELS)
        row = {"ID": g["ID"]}
        errors = 0
        for lab in LABELS:
            a, b = int(g[lab]), int(p[lab])
            state = "TP" if a and b else "FP" if (not a and b) else "FN" if (a and not b) else "TN"
            row[f"{lab}_outcome"] = state
            errors += state in {"FP","FN"}
        row["predicted_pattern"] = pattern
        row["pattern_frequency"] = patterns[pattern]
        row["predicted_positive_count"] = sum(int(x) for x in pattern)
        row["hierarchy_violation"] = int((int(p["Function"]) or int(p["Behavior"]) or int(p["Data"])) and not int(p["F"]))
        row["label_errors"] = int(errors)
        rows.append(row)
    return rows

def metrics_from_evidence(rows):
    out = {}
    for lab in LABELS:
        c = Counter(r[f"{lab}_outcome"] for r in rows)
        tp,fp,fn,tn = c["TP"],c["FP"],c["FN"],c["TN"]
        precision = tp/(tp+fp) if tp+fp else 0.0
        recall = tp/(tp+fn) if tp+fn else 0.0
        f1 = 2*precision*recall/(precision+recall) if precision+recall else 0.0
        out[lab]={"precision":precision,"recall":recall,"f1":f1,"tp":tp,"fp":fp,"fn":fn,"tn":tn}
    return out

def oracle_rank(rows):
    return sorted(rows,key=lambda r:(-int(r["label_errors"]),str(r["ID"])))

def prediction_pattern_rarity_rank(rows):
    return sorted(rows,key=lambda r:(int(r["pattern_frequency"]),-int(r["hierarchy_violation"]),-int(r["predicted_positive_count"]),str(r["ID"])))

def review_capture(rows,budgets=BUDGETS):
    total=sum(int(r["label_errors"]) for r in rows)
    oracle,deploy=oracle_rank(rows),prediction_pattern_rarity_rank(rows)
    out=[]
    for k in budgets:
        random_share=k/len(rows)
        for name,ranked,uses_gold in (("oracle_upper_bound",oracle,True),("prediction_pattern_rarity",deploy,False)):
            errors=sum(int(r["label_errors"]) for r in ranked[:k]); share=errors/total if total else 0.0
            out.append({"method":name,"budget":k,"errors_captured":errors,"error_capture_share":round(share,3),"enrichment_vs_random":round(share/random_share,3),"uses_gold_for_ranking":uses_gold})
        out.append({"method":"random_expected","budget":k,"errors_captured":round(total*random_share,3),"error_capture_share":round(random_share,3),"enrichment_vs_random":1.0,"uses_gold_for_ranking":False})
    return out

def load_evidence():
    with (ROOT/"data/derived/evaluation_observations.csv").open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def load_primary_results():
    with (ROOT/"data/derived/primary_results.csv").open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def load_triage_results():
    with (ROOT/"data/derived/triage_results.csv").open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def load_summary():
    return json.loads((ROOT/"results/empirical_summary.json").read_text(encoding="utf-8"))

def validate_bundle():
    rows=load_evidence(); metrics=metrics_from_evidence(rows); primary={r["label"]:r for r in load_primary_results()}
    if len(rows)!=571 or sum(int(r["label_errors"]) for r in rows)!=534:return False
    for lab in LABELS:
        r,m=primary[lab],metrics[lab]
        if (int(r["tp"]),int(r["fp"]),int(r["fn"]),int(r["tn"]))!=(m["tp"],m["fp"],m["fn"],m["tn"]):return False
        if abs(float(r["f1"])-round(m["f1"],3))>1e-9:return False
    calc=review_capture(rows)
    packaged=load_triage_results()
    if len(calc)!=len(packaged):return False
    for a,b in zip(calc,packaged):
        if a["method"]!=b["method"] or a["budget"]!=int(b["budget"]) or a["uses_gold_for_ranking"]!=(b["uses_gold_for_ranking"].lower()=="true"):return False
        for key in ("errors_captured","error_capture_share","enrichment_vs_random"):
            if abs(float(a[key])-float(b[key]))>1e-9:return False
    s=load_summary()["headline_metrics"]
    return s["n_requirement_elements"]==571 and s["total_label_errors_across_5_fields"]==534 and s["oracle_top_100_error_capture_share"]==0.519 and s["deployable_top_100_error_capture_share"]==0.215 and s["random_expected_top_100_error_capture_share"]==0.175 and s["deployable_top_100_enrichment_vs_random"]==1.23

# Release verification is enforced by GitHub Actions.

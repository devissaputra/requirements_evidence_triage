from __future__ import annotations
import csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LABELS=('Function','Behavior','Data','F','UserRelated')
def confusion_metrics(gold,pred,labels=LABELS):
    by={r['ID']:r for r in pred}; out={}
    for lab in labels:
        tp=fp=fn=tn=0
        for g in gold:
            a=int(g[lab]); p=int(by[g['ID']][lab])
            if a and p:tp+=1
            elif not a and p:fp+=1
            elif a and not p:fn+=1
            else:tn+=1
        precision=tp/(tp+fp) if tp+fp else 0.; recall=tp/(tp+fn) if tp+fn else 0.; f1=2*precision*recall/(precision+recall) if precision+recall else 0.
        out[lab]={'precision':precision,'recall':recall,'f1':f1,'tp':tp,'fp':fp,'fn':fn,'tn':tn}
    return out
def disagreement_counts(gold,pred,labels=LABELS):
    by={r['ID']:r for r in pred}; return sorted((sum(int(g[l])!=int(by[g['ID']][l]) for l in labels) for g in gold), reverse=True)
def review_capture(counts,budgets=(10,25,50,100)):
    total=sum(counts); return {k:(sum(counts[:k]), sum(counts[:k])/total if total else 0.) for k in budgets}
def load_summary():return json.loads((ROOT/'results/empirical_summary.json').read_text())
def validate_bundle():
    s=load_summary()['headline_metrics']; return s['n_requirement_elements']==571 and s['total_label_errors_across_5_fields']==534 and abs(s['top_100_review_error_capture_share']-.519)<.001

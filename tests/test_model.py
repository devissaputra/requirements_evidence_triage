from research.model import LABELS,load_evidence,metrics_from_evidence,oracle_rank,prediction_pattern_rarity_rank,review_capture,validate_bundle

EXPECTED={"Function":(264,70,35,202,0.834),"Behavior":(329,113,13,116,0.839),"Data":(148,63,38,322,0.746),"F":(455,51,2,63,0.945),"UserRelated":(140,10,139,282,0.653)}

def test_five_label_scope():assert LABELS==("Function","Behavior","Data","F","UserRelated")
def test_complete_packaged_evidence():
    rows=load_evidence();assert len(rows)==571;assert sum(int(r["label_errors"]) for r in rows)==534
def test_all_confusion_matrices_recompute_from_evidence():
    m=metrics_from_evidence(load_evidence())
    for lab,(tp,fp,fn,tn,f1) in EXPECTED.items():
        assert (m[lab]["tp"],m[lab]["fp"],m[lab]["fn"],m[lab]["tn"])==(tp,fp,fn,tn);assert round(m[lab]["f1"],3)==f1
def test_review_curves_exact():
    r={(x["method"],x["budget"]):x for x in review_capture(load_evidence())}
    assert r[("oracle_upper_bound",100)]["errors_captured"]==277 and r[("oracle_upper_bound",100)]["error_capture_share"]==0.519
    assert r[("prediction_pattern_rarity",100)]["errors_captured"]==115 and r[("prediction_pattern_rarity",100)]["error_capture_share"]==0.215
    assert r[("prediction_pattern_rarity",100)]["enrichment_vs_random"]==1.23 and r[("random_expected",100)]["error_capture_share"]==0.175
def test_deployable_ranking_does_not_depend_on_gold_outcomes():
    rows=load_evidence();a=[r["ID"] for r in prediction_pattern_rarity_rank(rows)];altered=[dict(r) for r in rows]
    for r in altered:
        for lab in LABELS:r[f"{lab}_outcome"]="TN"
        r["label_errors"]=0
    assert a==[r["ID"] for r in prediction_pattern_rarity_rank(altered)]
def test_oracle_and_deployable_are_distinct():
    rows=load_evidence();assert [r["ID"] for r in oracle_rank(rows)[:20]]!=[r["ID"] for r in prediction_pattern_rarity_rank(rows)[:20]]
def test_full_bundle_validation():assert validate_bundle()

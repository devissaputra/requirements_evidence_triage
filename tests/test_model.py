from research.model import LABELS,confusion_metrics,disagreement_counts,review_capture,validate_bundle
def test_five_label_scope(): assert LABELS==('Function','Behavior','Data','F','UserRelated')
def test_metrics_and_capture_fixture():
    g=[{'ID':'1','Function':'1','Behavior':'0','Data':'0','F':'1','UserRelated':'0'},{'ID':'2','Function':'0','Behavior':'1','Data':'0','F':'1','UserRelated':'1'}]
    p=[dict(g[0]),dict(g[1])]; p[1]['UserRelated']='0'; m=confusion_metrics(g,p); assert m['Function']['f1']==1 and m['UserRelated']['fn']==1; c=disagreement_counts(g,p); assert sum(c)==1; assert review_capture(c,(1,))[1][0]==1
def test_corrected_packaged_counts(): assert validate_bundle()

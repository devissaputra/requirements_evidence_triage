#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,html
from pathlib import Path
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def t(x,y,s,z=16,w="400",a="start"):return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{z}" font-weight="{w}" text-anchor="{a}">{html.escape(str(s))}</text>'
def o(w,h):return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="white"/>'
def primary():
    with (ROOT/"data/derived/primary_results.csv").open() as f:return list(csv.DictReader(f))
def tri():
    with (ROOT/"data/derived/triage_results.csv").open() as f:return list(csv.DictReader(f))
def architecture():
    p=[o(1200,420),t(45,50,"Requirements Evidence Triage",29,"700"),t(45,82,"Pinned source → five-label evaluation → oracle ceiling → prediction-only routing → bounded interpretation",15)]
    ls=[("Pinned source","571 eTour items"),("Classify","5 labels"),("Oracle","gold-aware ceiling"),("Deployable","prediction-only"),("Interpret","review efficiency")]
    for i,(a,b) in enumerate(ls):
        x=35+i*232;p+=[f'<rect x="{x}" y="145" width="185" height="120" rx="12" fill="#f7f7f7" stroke="#333"/>',t(x+92.5,185,a,17,"700","middle"),t(x+92.5,218,b,14,"400","middle")]
        if i<4:p.append(f'<line x1="{x+185}" y1="205" x2="{x+222}" y2="205" stroke="#222" stroke-width="2"/>')
    return "".join(p+["</svg>"])
def method():
    s=["Join gold and automatic rows by ID.","Compute confusion matrices for five comparable labels.","Use gold-error ranking only as an oracle upper bound.","Rank deployably by prediction-pattern rarity; compare with random expectation."]
    p=[o(1200,520),t(45,50,"Method",29,"700"),t(45,82,"The operational queue never uses gold labels for ranking.",15)]
    for i,x in enumerate(s,1):
        y=120+(i-1)*90;p+=[f'<circle cx="75" cy="{y+30}" r="23" fill="#f0f0f0" stroke="#333"/>',t(75,y+36,i,16,"700","middle"),f'<rect x="120" y="{y}" width="1020" height="62" rx="10" fill="#fafafa" stroke="#444"/>',t(145,y+38,x,15)]
    return "".join(p+["</svg>"])
def research():
    p=[o(1050,560),t(40,45,"Five-label classification F1",27,"700"),t(40,73,"UserRelated recall is the dominant weakness in the released eTour evaluation.",14)]
    left,bottom,top,bw,gap=85,460,95,120,65
    for i,r in enumerate(primary()):
        v=float(r["f1"]);x=left+i*(bw+gap);bh=v*(bottom-top);y=bottom-bh;p+=[f'<rect x="{x}" y="{y:.2f}" width="{bw}" height="{bh:.2f}" fill="#555" fill-opacity="0.72"/>',t(x+bw/2,y-10,f"{v:.3f}",15,"700","middle"),t(x+bw/2,bottom+28,r["label"],13,"700","middle")]
    return "".join(p+[f'<line x1="{left-20}" y1="{bottom}" x2="1010" y2="{bottom}" stroke="#222"/>',"</svg>"])
def triage():
    rows=tri();names={"oracle_upper_bound":"Oracle upper bound","prediction_pattern_rarity":"Prediction-only rarity","random_expected":"Random expected"};p=[o(1100,610),t(40,45,"Human-review error capture",27,"700"),t(40,73,"Oracle uses gold labels; deployable rarity uses predictions only.",14)]
    for bi,b in enumerate((10,25,50,100)):
        y=130+bi*105;p.append(t(55,y+30,f"Budget {b}",14,"700"))
        for mi,m in enumerate(("oracle_upper_bound","prediction_pattern_rarity","random_expected")):
            r=next(x for x in rows if x["method"]==m and int(x["budget"])==b);share=float(r["error_capture_share"]);x=180+mi*285;width=share*430;p+=[t(x,y,names[m],12,"700"),f'<rect x="{x}" y="{y+12}" width="{width:.2f}" height="22" fill="#666" fill-opacity="{0.85-mi*0.18:.2f}"/>',t(x+width+8,y+29,f"{share*100:.1f}%",12)]
    return "".join(p+[t(40,585,"The 51.9% figure is an oracle ceiling, not an operational policy.",13,"700"),"</svg>"])
def evaluation():
    p=[o(1200,510),t(45,50,"Evidence Boundary",29,"700")]
    bs=[("Classification finding","F1 spans 0.653–0.945 across five evaluated labels; 534 label errors are observed."),("Oracle ceiling","Gold-aware top-100 ranking captures 51.9% of errors. It cannot be deployed before review."),("Deployable finding","Prediction-only rarity captures 21.5% in 100 items vs 17.5% random expectation (1.23×)."),("Boundary","Exploratory, post-hoc, single-benchmark routing result; no external-validation or optimality claim.")]
    for i,(a,b) in enumerate(bs):
        y=90+i*95;p+=[f'<rect x="55" y="{y}" width="1090" height="72" rx="10" fill="#f8f8f8" stroke="#444"/>',t(80,y+28,a,16,"700"),t(80,y+53,b,14)]
    return "".join(p+["</svg>"])
def render(out):
    out.mkdir(parents=True,exist_ok=True);fs={"architecture.svg":architecture(),"method.svg":method(),"research_design.svg":research(),"triage.svg":triage(),"evaluation.svg":evaluation()}
    for n,c in fs.items():ET.fromstring(c);(out/n).write_text(c,encoding="utf-8")
    return fs
def main():
    a=argparse.ArgumentParser();a.add_argument("--out-dir",default=str(ROOT/"assets"));x=a.parse_args();print("generated_figures:",len(render(Path(x.out_dir))))
if __name__=="__main__":main()

#!/usr/bin/env python3
import json
from research.model import load_summary,review_capture,load_evidence,validate_bundle
print(json.dumps(load_summary(),indent=2,ensure_ascii=False))
print(json.dumps(review_capture(load_evidence()),indent=2,ensure_ascii=False))
print("bundle_validation:","PASS" if validate_bundle() else "FAIL")

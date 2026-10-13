import json,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from correlate_findings import correlate
class Tests(unittest.TestCase):
 def setUp(self):
  r=Path(__file__).resolve().parents[1];self.case=json.loads((r/"data/case.json").read_text());self.findings=json.loads((r/"data/findings.json").read_text())
 def test_valid_demo_dataset(self):
  x=correlate(self.case,self.findings);self.assertEqual(x["validation"],"PASS");self.assertEqual(x["record_count"],5);self.assertEqual(x["unique_evidence_ids"],5)
 def test_duplicate_ids_rejected(self):
  x=correlate(self.case,self.findings+[dict(self.findings[0])]);self.assertEqual(x["validation"],"FAIL")
if __name__=="__main__":unittest.main()

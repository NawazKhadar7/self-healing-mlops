import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.registry import Registry
class RegistryTests(unittest.TestCase):
    def test_gate(self):
        with tempfile.TemporaryDirectory() as tmp:
            r=Registry(Path(tmp)/'model');self.assertFalse(r.promote({'weight':1},.6,.5));self.assertFalse(r.promote({'weight':1},.8,.9));self.assertTrue(r.promote({'weight':1},.9,.8));self.assertEqual(r.load()['score'],.9)
    def test_checksum(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'model';r=Registry(p);r.promote({'weight':1},1,1);v=json.loads(p.read_text());v['payload']['score']=0;p.write_text(json.dumps(v))
            with self.assertRaises(ValueError):r.load()

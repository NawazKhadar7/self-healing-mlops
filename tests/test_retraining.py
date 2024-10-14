import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
class RetrainTests(unittest.TestCase):
    def test_missing_batch_blocked(self):
        r=run_case({'id':'m','family':'missing','size':32,'seed':3})['metrics'];self.assertFalse(r['retraining_triggered']);self.assertFalse(r['promoted'])
    def test_label_flip_isolated(self):
        r=run_case({'id':'f','family':'label-flip','size':64,'seed':1})['metrics'];self.assertTrue(r['isolated_job']);self.assertTrue(r['promotion_safe'])

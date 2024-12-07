import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.quality import train,accuracy,valid_rows
class QualityTests(unittest.TestCase):
    def test_training(self):
        rows=[(-2,0),(-1,0),(1,1),(2,1)];self.assertEqual(accuracy(train(rows),rows),1)
    def test_missing(self):self.assertEqual(valid_rows([(None,1),(1,1),(float('nan'),0)]),[(1,1)])

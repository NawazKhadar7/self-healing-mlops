import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.drift import ks_statistic,threshold
class DriftTests(unittest.TestCase):
    def test_known_distances(self):self.assertEqual(ks_statistic([1,2],[1,2]),0);self.assertEqual(ks_statistic([0,1],[3,4]),1)
    def test_ties(self):self.assertAlmostEqual(ks_statistic([0,0],[0,1]),.5)

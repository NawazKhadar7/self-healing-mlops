# stable-seventeen

Evaluate a stable batch above the sample threshold.

All rows remain clean and the baseline classifier is correct.

Family: stable. Size: 17. Deterministic seed: 910802.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case stable-seventeen
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| received | equals 17 |
| clean | equals 17 |
| missing | equals 0 |
| accounted | equals true |
| promotion_safe | equals true |
| baseline_accuracy | equals 1 |
| ks_statistic | min 0, max 1 |
| candidate_accuracy | min 0, max 1 |

Scope: Synthetic batches and the local retraining subprocess.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).

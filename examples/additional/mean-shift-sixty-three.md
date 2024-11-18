# mean-shift-sixty-three

Evaluate an odd-sized mean-shift batch.

Observe the KS decision while preserving promotion safety.

Family: mean-shift. Size: 63. Deterministic seed: 910809.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case mean-shift-sixty-three
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| received | equals 63 |
| clean | equals 63 |
| missing | equals 0 |
| accounted | equals true |
| promotion_safe | equals true |
| baseline_accuracy | equals 1 |
| ks_statistic | min 0, max 1 |
| candidate_accuracy | min 0, max 1 |

Scope: Synthetic batches and the local retraining subprocess.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).

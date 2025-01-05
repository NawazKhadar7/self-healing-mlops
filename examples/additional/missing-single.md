# missing-single

Evaluate a batch with its only feature missing.

No clean samples remain and retraining cannot start.

Family: missing. Size: 1. Deterministic seed: 910803.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case missing-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| received | equals 1 |
| clean | equals 0 |
| missing | equals 1 |
| accounted | equals true |
| promotion_safe | equals true |
| baseline_accuracy | equals 0 |
| retraining_triggered | equals false |
| isolated_job | equals false |
| promoted | equals false |
| ks_statistic | min 0, max 1 |
| candidate_accuracy | min 0, max 1 |

Scope: Synthetic batches and the local retraining subprocess.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).

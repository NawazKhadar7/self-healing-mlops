# small-batch-below

Evaluate the gated small-batch family.

The explicit family gate keeps retraining disabled.

Family: small-batch. Size: 15. Deterministic seed: 910807.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case small-batch-below
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| received | equals 15 |
| clean | equals 15 |
| missing | equals 0 |
| accounted | equals true |
| promotion_safe | equals true |
| baseline_accuracy | equals 1 |
| retraining_triggered | equals false |
| isolated_job | equals false |
| promoted | equals false |
| ks_statistic | min 0, max 1 |
| candidate_accuracy | min 0, max 1 |

Scope: Synthetic batches and the local retraining subprocess.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).

# missing-seventeen

Evaluate seventeen rows with periodic missing features.

Six missing rows leave eleven clean rows and prevent retraining.

Family: missing. Size: 17. Deterministic seed: 910804.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case missing-seventeen
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| received | equals 17 |
| clean | equals 11 |
| missing | equals 6 |
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

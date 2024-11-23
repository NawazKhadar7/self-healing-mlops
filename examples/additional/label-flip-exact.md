# label-flip-exact

Flip labels at the sixteen-row threshold.

The quality failure starts an isolated retraining job.

Family: label-flip. Size: 16. Deterministic seed: 910806.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case label-flip-exact
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| received | equals 16 |
| clean | equals 16 |
| missing | equals 0 |
| accounted | equals true |
| promotion_safe | equals true |
| baseline_accuracy | equals 0 |
| quality_failure | equals true |
| retraining_triggered | equals true |
| isolated_job | equals true |
| ks_statistic | min 0, max 1 |
| candidate_accuracy | min 0, max 1 |

Scope: Synthetic batches and the local retraining subprocess.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).

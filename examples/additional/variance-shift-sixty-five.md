# variance-shift-sixty-five

Evaluate an odd-sized variance-shift batch.

A spread change preserves accounting and promotion safety.

Family: variance-shift. Size: 65. Deterministic seed: 910810.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case variance-shift-sixty-five
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| received | equals 65 |
| clean | equals 65 |
| missing | equals 0 |
| accounted | equals true |
| promotion_safe | equals true |
| baseline_accuracy | equals 1 |
| ks_statistic | min 0, max 1 |
| candidate_accuracy | min 0, max 1 |

Scope: Synthetic batches and the local retraining subprocess.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).

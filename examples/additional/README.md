# Additional scenarios for self-healing-mlops

Ten runnable scenarios cover small inputs, odd sizes, and behavior boundaries in the existing reference implementation.

This directory contains 10 input JSON files, 10 metric-oracle JSON files, 10 scenario notes, this guide, and the runner (32 files).

Run from the project directory with Python 3.10 or later and the dependencies already listed in requirements.txt.

~~~powershell
python -B examples/additional/run_cases.py --list
python -B examples/additional/run_cases.py
python -B examples/additional/run_cases.py --case stable-single --json
~~~

The runner exits with zero only when all selected scenarios pass. --json includes metrics and output or a failure reason for each scenario.

Each .case.json is paired with a .expected.json containing equality checks or numeric bounds for the existing syslab.common.check helper.
Scenario notes explain the selected boundaries. Fixed seeds make inputs repeatable; expected files contain assertions rather than recorded timings.

| Scenario | Family | Size | Purpose |
| --- | --- | --- | --- |
| stable-single | stable | 1 | Evaluate one valid row. |
| stable-seventeen | stable | 17 | Evaluate a stable batch above the sample threshold. |
| missing-single | missing | 1 | Evaluate a batch with its only feature missing. |
| missing-seventeen | missing | 17 | Evaluate seventeen rows with periodic missing features. |
| label-flip-below | label-flip | 15 | Flip labels below the sixteen-row threshold. |
| label-flip-exact | label-flip | 16 | Flip labels at the sixteen-row threshold. |
| small-batch-below | small-batch | 15 | Evaluate the gated small-batch family. |
| small-batch-exact | small-batch | 16 | Reach sixteen rows in the gated small-batch family. |
| mean-shift-sixty-three | mean-shift | 63 | Evaluate an odd-sized mean-shift batch. |
| variance-shift-sixty-five | variance-shift | 65 | Evaluate an odd-sized variance-shift batch. |

Scope: Synthetic batches and the local retraining subprocess.

Supplemental inputs have their own runner, so the existing workload discovery and its 36-case suite retain their current behavior.
Bytecode generation is disabled. Reports go to standard output; storage and model artifacts use the reference code's temporary directories.

See [limitations](../../docs/LIMITATIONS.md) and [running instructions](../../docs/RUNNING.md).

# small-batch-096-06

Use a minimum-sample policy and disable automatic retraining for this diagnostic profile.

Input scale: 96; deterministic random seed: 261.
Run `python scripts/demo.py --case workloads/small-batch-096-06.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.

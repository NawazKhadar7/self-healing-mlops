# variance-shift-024-02

Increase feature variance and test drift detection.

Input scale: 24; deterministic random seed: 164.
Run `python scripts/demo.py --case workloads/variance-shift-024-02.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.

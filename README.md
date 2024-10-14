# Self-Healing MLOps Pipeline

Distribution monitoring, quality gates and isolated local retraining with holdout-controlled model promotion.

This is newly generated educational reference code based on a concept in the supplied PDF.
It has **165 non-empty source, test, configuration, workload and documentation files**.
It is a prototype for study and extension, not evidence of previous deployment or measured large-scale performance.

## Quick start

Requires Python 3.10+; the default path uses the standard library.

```sh
python scripts/demo.py
python scripts/run_tests.py
python scripts/benchmark.py
python scripts/serve.py --port 8080
```

Open http://127.0.0.1:8080 for the workload dashboard. `scripts/demo.py --case workloads/<id>.case.json`
executes one workload and checks its independent acceptance conditions. `benchmark.py` prints actual local timings.

## Implemented scope

Two-sample KS statistic, asymptotic threshold, missingness gate, simple logistic training in a subprocess, held-out accuracy comparison and checksummed atomic local registry.

## Limits and optional runtimes

No cloud jobs, MLflow service or production metrics backend. KS threshold is approximate, not an exact p-value, and repeated testing requires false-alarm control. The reference is a one-feature classifier. Holdout sets are small; promotion accuracy is illustrative, not a clinical or business acceptance standard.

All bundled data are synthetic. No credentials, pretrained model weights, historical commits, or fabricated benchmark results are included.
See `docs/PROVENANCE.md`, `docs/TESTING.md`, and the bundle's validation report for evidence and omissions.

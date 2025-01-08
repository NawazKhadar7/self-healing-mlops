# Self-Healing MLOps Pipeline

Distribution monitoring, quality gates and isolated local retraining with holdout-controlled model promotion.

## 1. Overview

A retraining pipeline should distinguish changed data, poor data quality and an actually better replacement model. This local reference combines monitoring, isolated training and a held-out promotion gate so the decision to replace a model can be examined.

**Project type:** educational reference implementation. **Repository contents:** 165 non-empty source, test, configuration, workload and documentation files, including 36 synthetic workload scenarios.

## 2. Core Features — Why They Matter

- **Distribution monitoring:** Computes a two-sample Kolmogorov-Smirnov statistic with an approximate threshold.
- **Quality gates:** Tracks missing data and requires enough clean samples for training.
- **Isolated retraining:** Runs a simple logistic trainer in a local subprocess when policy conditions trigger it.
- **Controlled promotion:** Compares held-out accuracy and records models in a checksummed atomic local registry.

## 3. Tech Stack & Architecture

| Layer | Technology | Implementation status |
| --- | --- | --- |
| Execution | Python 3.10+ standard library | Runnable local pipeline |
| Monitoring and training | KS statistic, one-feature logistic classifier, subprocess | Reference implementations |
| Registry | Local JSON/checksum records and atomic writes | No cloud job or MLflow service |

### How the components fit together

An incoming batch passes cleaning and missingness checks. Distribution and accuracy monitoring feed a retraining policy; eligible batches launch an isolated trainer. A held-out gate decides promotion before the local registry is updated.

| Component | Responsibility |
| --- | --- |
| [src/syslab/drift.py](src/syslab/drift.py) | Distribution statistic and approximate threshold. |
| [src/syslab/quality.py](src/syslab/quality.py) | Missingness and clean-sample checks. |
| [src/syslab/retrain.py](src/syslab/retrain.py) | Local isolated training job. |
| [src/syslab/registry.py](src/syslab/registry.py) | Checksummed model storage and atomic publication. |

See [Architecture](docs/ARCHITECTURE.md) and [Algorithms](docs/ALGORITHMS.md) for implementation notes.

### Scope and limitations

No cloud jobs, MLflow service or production metrics backend. KS threshold is approximate, not an exact p-value, and repeated testing requires false-alarm control. The reference is a one-feature classifier. Holdout sets are small; promotion accuracy is illustrative, not a clinical or business acceptance standard.

## 4. Getting Started / Installation

**Prerequisites:** Python 3.10+. The default reference uses Python's standard library. No API keys or external services are needed for the default sample.

Download/extract this project or clone its repository, then open a terminal in the `self-healing-mlops` folder. Create an isolated environment:

```sh
python -m venv .venv
```

Activate it on Linux/macOS:

```sh
source .venv/bin/activate
```

Or on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the declared Python dependencies and run the demo:

```sh
python -m pip install -r requirements.txt
python scripts/demo.py
```

Check behavior and collect timings on your own machine:

```sh
python scripts/run_tests.py
python scripts/benchmark.py
```

The original bundle validation recorded **24 passing tests** for this project and **36 accepted workload scenarios**. These are local reference checks, not production or hardware benchmarks. See [Testing](docs/TESTING.md) and [Benchmark notes](docs/BENCHMARKS.md).

## 5. Usage Examples

### Run a reproducible workload

The bundled [sample request](examples/request.json) contains:

```json
{
  "family": "stable",
  "id": "stable-016-01",
  "seed": 101,
  "size": 16
}
```

Run the corresponding workload and check its independent acceptance conditions:

```sh
python scripts/demo.py --case workloads/stable-016-01.case.json
```

Expected `metrics` excerpt from the verified local run; the complete JSON also includes `output`:

```json
{
  "metrics": {
    "accounted": true,
    "baseline_accuracy": 1.0,
    "candidate_accuracy": 1.0,
    "clean": 16,
    "drift_detected": false,
    "isolated_job": false,
    "ks_statistic": 0.132812,
    "missing": 0,
    "promoted": false,
    "promotion_safe": true,
    "quality_failure": false,
    "received": 16,
    "retraining_triggered": false
  }
}
```

The stable example contains 16 clean samples, reports no drift and triggers neither retraining nor promotion. Accuracy values of 1.0 belong to this small synthetic example and are not evidence of general model performance.

The complete example is in [examples/response.json](examples/response.json). Floating-point last digits can vary across numeric environments.

### Explore through the local dashboard

```sh
python scripts/serve.py --port 8080
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080), select a workload and choose **Run and check**. The server listens on loopback and is intended for local inspection.

With the server running, a second terminal can call its workload inspection API:

```sh
curl "http://127.0.0.1:8080/api/run?id=stable-016-01"
```

This endpoint executes the bundled workload; it is not a production domain API.

## 6. Your Contributions / Research Alignment

### Implementation evidence

The following work areas are present in this reference and can be reviewed directly:

| Work area in this reference | Repository evidence |
| --- | --- |
| Distribution monitoring | [src/syslab/drift.py](src/syslab/drift.py) |
| Correctness and edge cases | [tests/](tests/) and [acceptance workloads](workloads/) |
| Reproducible evaluation | [scripts/demo.py](scripts/demo.py), [scripts/benchmark.py](scripts/benchmark.py), [testing notes](docs/TESTING.md) |

### Research alignment

The project connects applied machine learning with reliable automation, monitoring and experiment design. It can support discussion of when distribution changes justify retraining and how promotion policies avoid replacing a model with a weaker candidate.

**A question to investigate:** How should drift thresholds and promotion gates be calibrated to limit unnecessary retraining and repeated-testing false alarms?

This question is a proposed extension, not a completed research result. Evaluate it with controlled inputs, independent correctness checks and measurements tied to a reproducible configuration.

### Personal contribution record

This reference was generated from the supplied project concept. Personal authorship or research contributions have not been verified. For an MS application, document only the modules you actually changed, the design choices you can explain, and experiments you ran; link those claims to commits or reproducible reports. See [Provenance](docs/PROVENANCE.md).

All bundled inputs are synthetic. The repository does not establish historical development dates, prior deployment or published research.

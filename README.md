# harness-demo-app

Sample Python (Flask) application for the Harness **CI + CD + STO** hands-on exercise.

## Local development

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
pytest
python -m src.app
# In another terminal:
curl http://localhost:5000/
curl http://localhost:5000/health
```

## Endpoints

| Method | Path | Returns |
|--------|------|---------|
| GET | `/` | JSON `{"status": "ok", "version": "<APP_VERSION>"}` |
| GET | `/health` | Plain text `healthy` |

## Docker

```bash
docker build -t harness-demo-app:local .
docker run --rm -p 5000:5000 -e APP_VERSION=local harness-demo-app:local
```

## Kubernetes

Manifests in `manifests/` are templated for Harness:
- `<+artifact.image>` — Harness injects the deployed image
- `<+pipeline.variables.appVersion>` — Harness injects the version from the CD pipeline

## What this repo is used for

This repo is the sample app for a hands-on Harness exercise that covers:

- **CI** — clone, install, test, build wheel, scan, build image, push to DockerHub
- **CD** — service + environment + rolling deploy to Kubernetes
- **STO** — Gitleaks (secrets), Semgrep (SAST), Aqua Trivy (deps + image)
- **GitOps** — Hosted Agent syncing this repo's manifests to a cluster

See the exercise guide for the full step-by-step.

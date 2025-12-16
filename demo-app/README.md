# Sample Web App CI/CD with Jenkins, Docker, Kubernetes, Prometheus/Grafana

This repository contains a Flask web app that uses PostgreSQL, a Dockerfile, Kubernetes manifests, and a Jenkins pipeline for CI/CD on an AWS EC2 instance running k3s.

## Components
- Flask app with `/health` and `/metrics` (Prometheus)
- PostgreSQL database (StatefulSet + PVC)
- Jenkinsfile stages:
  1. Code Fetch
  2. Docker Image Build & Basic Health Test
  3. Push to DockerHub
  4. Kubernetes Deploy/Update
  5. Prometheus/Grafana Install via Helm

## Folder layout
- `app/` — Flask application code
- `k8s/` — Kubernetes manifests
- `Jenkinsfile` — CI/CD pipeline

See `REPORT.md` for detailed steps and screenshots guide.
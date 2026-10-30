# Production Monitoring & Observability

> Reference for Prometheus telemetry architecture, TSDB metrics collection, PromQL syntax, Grafana visual dashboards, and Alertmanager routing.

---

## 1. Verified Official Documentation & Standards
- [Prometheus Official Documentation](https://prometheus.io/docs/introduction/overview/)
- [PromQL Query Language Reference](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- [Grafana Visualization Documentation](https://grafana.com/docs/grafana/latest/)
- [Google Site Reliability Engineering (SRE) Book](https://sre.google/sre-book/table-of-contents/)

---

## 2. Essential CLI & Configuration Cheatsheet
```text
# Essential PromQL Queries
rate(http_requests_total[5m])                                     # Request rate per second
sum by (status) (rate(http_requests_total{status=~"5.."}[5m]))    # 5xx error rate
histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket[5m]))) # 95th percentile latency
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)        # CPU utilization %
```

---

## 3. Best Practices & Production Guidelines
- **Reproducibility:** Never configure production components manually. All configuration must be committed to Git.
- **Least Privilege:** Restrict permissions, ports, and access tokens to the absolute minimum required.
- **Fail Fast:** Incorporate automated validation and linting in early CI stages.
- **Continuous Observability:** Instrument metrics and structured logs at every tier of the architecture.

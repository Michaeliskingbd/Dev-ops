# Kubernetes Container Orchestration

> Production reference for Kubernetes architecture, Pods, Deployments, Services, Ingress, ConfigMaps, Secrets, PV/PVC, and Helm charts.

---

## 1. Verified Official Documentation & Standards
- [Kubernetes Official Documentation](https://kubernetes.io/docs/)
- [kubectl Command Reference](https://kubernetes.io/docs/reference/kubectl/)
- [Helm Package Manager Documentation](https://helm.sh/docs/)
- [Kubernetes Production Best Practices](https://kubernetes.io/docs/setup/best-practices/)

---

## 2. Essential CLI & Configuration Cheatsheet
```bash
# kubectl Diagnostic Commands
kubectl get pods -A -o wide                # View all pods across namespaces
kubectl describe pod <pod-name>            # Inspect pod events and failure traces
kubectl logs <pod-name> -c <container> -f  # Stream container logs
kubectl rollout status deployment/<name>   # Monitor zero-downtime rolling update
kubectl get events --sort-by='.metadata.creationTimestamp' # Recent cluster events
```

---

## 3. Best Practices & Production Guidelines
- **Reproducibility:** Never configure production components manually. All configuration must be committed to Git.
- **Least Privilege:** Restrict permissions, ports, and access tokens to the absolute minimum required.
- **Fail Fast:** Incorporate automated validation and linting in early CI stages.
- **Continuous Observability:** Instrument metrics and structured logs at every tier of the architecture.

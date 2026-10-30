# Python for DevOps & Infrastructure Automation

> Core reference guide for writing Python automation scripts, parsing JSON/YAML configs, making HTTP requests, and executing subprocesses safely.

---

## 1. Verified Official Documentation & Standards
- [Official Python 3 Documentation](https://docs.python.org/3/)
- [Python Subprocess Management](https://docs.python.org/3/library/subprocess.html)
- [Python Requests Library Guide](https://requests.readthedocs.io/)
- [PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)
- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)

---

## 2. Essential CLI & Configuration Cheatsheet
```python
import subprocess
import requests
import json
import os

# Safe subprocess execution
result = subprocess.run(
    ["df", "-h"],
    capture_output=True,
    text=True,
    check=True
)
print(result.stdout)

# REST API Request with timeout & error handling
try:
    response = requests.get("https://api.github.com/status", timeout=5)
    response.raise_for_status()
    data = response.json()
    print(f"Status: {data.get('status')}")
except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")
```

---

## 3. Best Practices & Production Guidelines
- **Reproducibility:** Never configure production components manually. All configuration must be committed to Git.
- **Least Privilege:** Restrict permissions, ports, and access tokens to the absolute minimum required.
- **Fail Fast:** Incorporate automated validation and linting in early CI stages.
- **Continuous Observability:** Instrument metrics and structured logs at every tier of the architecture.

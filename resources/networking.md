# Computer Networking & Network Protocols

> Comprehensive reference for TCP/IP, IPv4/IPv6, CIDR subnetting, DNS resolution, HTTP/HTTPS lifecycle, and packet analysis.

---

## 1. Verified Official Documentation & Standards
- [RFC 791 - Internet Protocol Specification](https://datatracker.ietf.org/doc/html/rfc791)
- [RFC 793 - Transmission Control Protocol](https://datatracker.ietf.org/doc/html/rfc793)
- [RFC 1035 - Domain Names Implementation & Specification](https://datatracker.ietf.org/doc/html/rfc1035)
- [Mozilla Developer Network (MDN) HTTP Guides](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [Nginx Reverse Proxy Documentation](https://nginx.org/en/docs/)

---

## 2. Essential CLI & Configuration Cheatsheet
```bash
# Network Socket & Connection Inspection
ss -tulpn                              # Listening TCP and UDP sockets with PIDs
ss -s                                  # Summary statistics of sockets

# DNS & Resolution Diagnostics
dig +trace example.com                 # Full hierarchical DNS resolution trace
dig @1.1.1.1 example.com A +short       # Fast record lookup via Cloudflare DNS
nslookup example.com                   # Standard name query

# Packet Inspection & Tracing
traceroute -n example.com              # Network route hop tracing
sudo tcpdump -i eth0 -nn -c 20 port 80 # Capture 20 packets on port 80
curl -Iv https://example.com           # Verbose HTTP/TLS handshake inspection
```

---

## 3. Best Practices & Production Guidelines
- **Reproducibility:** Never configure production components manually. All configuration must be committed to Git.
- **Least Privilege:** Restrict permissions, ports, and access tokens to the absolute minimum required.
- **Fail Fast:** Incorporate automated validation and linting in early CI stages.
- **Continuous Observability:** Instrument metrics and structured logs at every tier of the architecture.

# Security Policy

The security of the **Real-Time E-Commerce Insights Engine** is important to us. We appreciate your efforts to responsibly disclose any vulnerabilities you may discover.

---

## Supported Versions

We actively maintain and provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| `main`  | :white_check_mark: |
| < 1.0.0 | :x:                |

---

## Reporting a Vulnerability

> [!IMPORTANT]
> **Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**

If you discover a security vulnerability within this project, please report it through one of the following channels:

1. **GitHub Private Vulnerability Reporting (Preferred):**  
   Use GitHub's advisory feature:  
   👉 [Report a security vulnerability](https://github.com/AhmadAbukhuit/ecommerce-insights-api/security/advisories/new)

2. **Direct Contact:**  
   Alternatively, contact the repository maintainer directly through your preferred secure channel or email.

### What to Include in Your Report

To help us triage and resolve the issue quickly, please provide:

- **Summary:** A clear description of the vulnerability and its potential impact.
- **Steps to Reproduce:** Step-by-step instructions (including sample requests, cURL commands, or reproduction scripts).
- **Environment Details:** OS, Python version, Docker version, and installed dependency versions.
- **Proof of Concept (PoC):** Any code, logs, or error outputs demonstrating the issue.
- **Proposed Fix (Optional):** Any suggested mitigations or patches if you have one.

---

## Response Process

When a security vulnerability is reported:

1. **Acknowledgment:** We aim to acknowledge receipt of the report within **48 hours**.
2. **Triage & Validation:** We will investigate and confirm the vulnerability, determining its severity and impact.
3. **Resolution & Release:** A patch will be developed, tested, and merged into the `main` branch.
4. **Coordinated Disclosure:** Once the fix is published, a public security advisory will be issued, and credit will be given to the reporter (unless you request anonymity).

We kindly ask that you keep details of the vulnerability confidential until a patch has been made publicly available.

---

## Security Best Practices for Production Deployment

This project serves as a demonstration API integrating **FastAPI**, **Pandas**, and **Docker**. If deploying this service in production, please implement the following hardening practices:

- **Authentication & Authorization:** The demonstration API endpoints are currently unauthenticated. Implement API keys, OAuth2, or JWT validation before exposing endpoints to untrusted networks.
- **CORS Restrictions:** Configure FastAPI's `CORSMiddleware` with explicit allowed origins rather than wildcard (`*`) access.
- **Rate Limiting:** Implement rate limiting (e.g., using `slowapi` or an API gateway/reverse proxy) to safeguard against abuse and denial-of-service (DoS) attempts.
- **Container Hardening:**
  - Run the application under a non-root user within the `Dockerfile`.
  - Disable `--reload` flag in production commands.
  - Keep base Docker images (`python:3.12-slim`) updated.
- **Dependency Auditing:** Regularly scan dependencies for known CVEs using tools like `pip-audit`:

  ```bash
  pip-audit -r requirements.txt
  ```

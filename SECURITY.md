# Security Policy

## Supported Versions

| Component | Version | Support Status |
|-----------|---------|----------------|
| Python    | 3.12.x  | ✅ Recommended |
| Python    | 3.11.x  | ✅ Supported   |
| Python    | 3.10.x  | ⚠️ Minimum     |
| Python    | < 3.10  | ❌ Not Supported |

## Security Update Process

### Regular Dependency Scanning

This project uses pip-audit for dependency vulnerability scanning. To run a security audit:

```bash
# Install pip-audit (if not already installed)
pip install pip-audit

# Run security audit
pip-audit -r requirements.txt
```

### Current Dependencies (Last Updated: 2026-02-08)

All dependencies are pinned to specific versions to ensure reproducibility and security:

- `ollama==0.6.1` - Latest stable version
- `python-dotenv==1.2.1` - Latest stable version
- `requests==2.32.5` - Latest secure version
- `html-sanitizer==2.6.0` - Latest stable version
- `nicegui==3.7.1` - Latest stable version

### Vulnerability Status

**Last Scan**: February 2026  
**Status**: ✅ No known vulnerabilities found  
**Tool**: pip-audit

## Reporting a Vulnerability

If you discover a security vulnerability, please report it by:

1. **DO NOT** open a public issue
2. Email the maintainer or use GitHub's private vulnerability reporting feature
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if available)

We will respond within 48 hours and work to address the issue promptly.

## Security Best Practices

### For Users

1. **Always use virtual environments** to isolate dependencies
2. **Keep dependencies updated** - run `pip list --outdated` regularly
3. **Use specific versions** in requirements.txt (avoid unpinned dependencies)
4. **Run security scans** before deploying to production
5. **Keep your .env file secure** - never commit it to version control

### For Developers

1. **Pin all dependencies** to specific versions
2. **Review changelogs** before updating dependencies
3. **Test thoroughly** after dependency updates
4. **Use pip-audit** in your development workflow
5. **Keep the Docker base image updated** to the latest stable Python version

### Docker Security

The project uses official Python Docker images:
- Base image: `python:3.12-slim`
- Multi-stage build to minimize image size
- Minimal runtime dependencies
- Regular security updates via base image updates

To rebuild with latest security patches:
```bash
docker build --no-cache -t carmelolg/hogwarts-gui-chat .
```

## Automated Dependency Updates

### GitHub Dependabot (Recommended)

To enable automated dependency updates, create `.github/dependabot.yml`:

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    
  - package-ecosystem: "docker"
    directory: "/"
    schedule:
      interval: "weekly"
```

### Manual Update Process

1. Check for outdated packages:
   ```bash
   pip list --outdated
   ```

2. Review changelogs for breaking changes

3. Update versions in `requirements.txt`

4. Run tests (if available)

5. Run security audit:
   ```bash
   pip-audit -r requirements.txt
   ```

6. Test the application manually

7. Commit and deploy

## Python Version Policy

- **Minimum supported**: Python 3.11
- **Recommended**: Python 3.12 (used in Docker)
- **EOL tracking**: Monitor [Python's release schedule](https://devguide.python.org/versions/)

When a Python version reaches EOL, it will be removed from supported versions within 90 days.

## Third-Party Dependencies

### Direct Dependencies Audit

| Package | Purpose | Security Considerations |
|---------|---------|------------------------|
| ollama | LLM integration | Official client, actively maintained |
| python-dotenv | Environment management | Widely used, minimal attack surface |
| requests | HTTP client | Industry standard, actively maintained |
| html-sanitizer | HTML cleaning | Security-focused library for XSS prevention |
| nicegui | Web UI framework | Modern framework with active development |

### Transitive Dependencies

Transitive dependencies are managed by pip and should be audited regularly using pip-audit.

## Docker Image Security

The Docker image is built using:
- Official Python images from Docker Hub
- Multi-stage build to reduce attack surface
- Minimal runtime dependencies
- Non-root user considerations (to be implemented)

## Security Contacts

For security-related questions or concerns, please refer to the repository's security policy on GitHub.

---

**Last Updated**: 2026-02-08  
**Next Review**: 2026-05-08 (Quarterly review recommended)

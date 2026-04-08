# Security

- No hardcoded secrets -- API keys, tokens, passwords belong in `.env` files only
- `.env` and `.env.*` must be in `.gitignore` for every project
- Validate all user inputs at system boundaries (forms, APIs, CLI args)
- Flag OWASP Top 10 vulnerabilities when spotted: injection, XSS, broken auth, SSRF, etc.
- Never expose credentials in logs, error messages, comments, or commit messages
- When creating examples, use clearly labeled dummy data -- never real credentials
- Never commit secrets to version control -- if accidentally committed, rotate immediately

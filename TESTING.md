# Certisured Internship Support Agent
## Local Testing Report

### Server
Command: uvicorn web:app --reload
URL: http://127.0.0.1:8000

### Website Test
- Homepage loaded successfully.
- CSS and JavaScript loaded successfully.
### AI Chat Test

Question: What is the duration of the Web Development internship?

Expected: 6 weeks based on synthetic program records.

Actual: [The Web Development internship lasts **6 weeks**.  
The fee and timing details are currently listed as “Unconfirmed,” so you’ll need to check with staff for the most up‑to‑date information.
]

Status: PASS

HTTP response: 200 OK
### Inquiry Form Test
- Inquiry form submitted with fictional test data.
- Consent checkbox selected.
- API response: 200 OK.
- Database persistence: Not yet verified.

### Security
- GROQ_API_KEY is stored in local .env.
- .env must remain excluded from Git.
- No real student information used for testing.
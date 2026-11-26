# Certisured Internship Support Agent
## Local Testing Report

### Test Environment
- Application: Certisured Internship Support Agent
- Framework: FastAPI
- Server: Uvicorn
- Command: `uvicorn web:app --reload`
- Local URL: http://127.0.0.1:8000
- Environment: Local Windows development environment

### Test 1: Application Startup

Status: PASS

Observed server output:
- Application startup complete.
- GET / returned 304 Not Modified.
- GET /style.css returned 304 Not Modified.
- GET /app.js returned 304 Not Modified.

Result: Website loaded successfully.

### Test 2: AI Chat Functionality

Status: PASS

Question:
What is the duration of the Web Development internship?

Actual assistant response:
The Web Development internship lasts 6 weeks.
The fee and timing details are currently listed as
"Unconfirmed", so staff confirmation is required.

Expected:
Retrieve the Web Development internship duration
from the synthetic program data.

Result:
The assistant correctly identified the duration
as 6 weeks and did not invent fees or timings.

HTTP Status:
POST /api/ask - 200 OK

### Test 3: Inquiry Form

Status: PASS (HTTP submission)

Actions:
1. Opened the inquiry form.
2. Entered test details.
3. Selected the consent checkbox.
4. Submitted the inquiry.

Observed response:
Staff follow-up requested, no admission promised.

HTTP Status:
POST /api/inquiry - 200 OK

Database persistence:
Not independently verified.

### Security Verification

- GROQ_API_KEY is configured in the local .env file.
- The .env file must remain excluded from Git.
- No API keys are included in this report.

### Overall Result

Local application startup: PASS
Website loading: PASS
AI chat response: PASS
Inquiry HTTP submission: PASS

The Certisured Internship Support Agent was tested
locally using Uvicorn.
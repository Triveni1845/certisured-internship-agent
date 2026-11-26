# Certisured Internship AI Support Agent

A Python and LangGraph-backed ReAct-style student support prototype.

This application helps prospective internship students ask questions about programs, durations, fees, timings, and internship policies.

**Important:** This is a development and staging prototype using synthetic records. Information must not be represented as an officially verified Certisured policy.

## Features

- AI-powered internship question answering
- LangGraph-backed agent with approved tools
- Program and policy lookup
- Fallback responses for unconfirmed information
- Consent-based student inquiry form
- FastAPI backend
- HTML, CSS, and JavaScript frontend

## Technology Stack

- Python
- FastAPI
- LangChain and LangGraph
- Groq API
- SQLite for local prototype inquiries
- HTML, CSS, JavaScript
- GitHub
- Render for staging deployment

## Run Locally

Install Python 3.11+, Git, and VS Code.

### Clone the Repository

```bash
git clone https://github.com/Triveni1845/certisured-internship-agent.git
cd certisured-internship-agent
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create the local environment file:

```powershell
Copy-Item .env.example .env
```

Add your credentials to `.env`:

```dotenv
GROQ_API_KEY=YOUR_PRIVATE_GROQ_KEY
GROQ_MODEL=openai/gpt-oss-20b
```

**Security:** Never commit `.env` or actual API keys to GitHub.

### Initialize the Database

```bash
python db.py
```

### Run Tests

```bash
python -m pytest -q
```

### Start the Application

```bash
uvicorn web:app --reload
```

Open the application in your browser:

http://127.0.0.1:8000

## Staging Deployment

The application can be deployed to a Python-compatible hosting service such as Render.

### Deployment Configuration

| Setting | Value |
|---|---|
| Platform | Render |
| Service Type | Web Service |
| Runtime | Python 3 |
| Repository | Triveni1845/certisured-internship-agent |
| Branch | main |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn web:app --host 0.0.0.0 --port $PORT` |

### Environment Variables

Configure the following environment variables securely through the hosting platform:

- `GROQ_API_KEY`: Private Groq API key stored as a server-side secret
- `GROQ_MODEL`: Supported Groq model

Never expose API keys in source code, screenshots, recordings, or GitHub commits.

### Staging Restrictions

- Use synthetic program records only.
- Use fictional student information during testing.
- Do not advertise staging as an official admissions service.
- Do not automatically issue internship offer letters.
- Do not rely on temporary SQLite storage for permanent inquiries.
- Restrict staging usage to development and demonstration purposes.

## Production Gate

**This application is not ready for real student data.**

Before production deployment, complete the following requirements:

1. Replace synthetic internship information with verified Certisured policies.
2. Confirm official program durations, fees, timings, and offer-letter procedures.
3. Implement a managed database with appropriate access controls.
4. Maintain consent records for student inquiries.
5. Publish an appropriate privacy notice.
6. Implement staff authentication and authorization.
7. Add API rate limits and abuse protection.
8. Configure a durable LangGraph checkpointer.
9. Implement monitoring, error logging, and alerts.
10. Configure database backups and recovery procedures.
11. Perform security, privacy, and functional testing.
12. Establish a staff-approved inquiry follow-up workflow.

Only after completing these requirements should the application be considered for deployment at:

**internships.certisured.com**

No automated offer-letter issuance is permitted without an approved institutional workflow.

## Demo and Testing

The demonstration is designed to cover the following application behaviors.

### Test 1: Verified Sample Answer

**Question:**

What is the duration of the Web Development internship?

**Expected Behavior:**

The agent retrieves the synthetic program record and explains that the sample duration is six weeks.

### Test 2: Fallback Behavior

**Question:**

What is the confirmed fee for the Agentic AI internship?

**Expected Behavior:**

The agent explains that the fee is unconfirmed and refers the student to Certisured staff.

### Test 3: Consent-Based Inquiry

**Action:**

Submit a fictional student inquiry with the consent checkbox selected.

**Expected Behavior:**

The application acknowledges the follow-up request without promising admission.

## Demo Recording

The demonstration recording has been uploaded to Google Drive.

**[▶ Watch Certisured Internship Support Agent Demo](https://drive.google.com/file/d/1F83qmJJBRRMPyLHnzWiulT3E0y--vffg/view?usp=sharing)**

The demonstration is intended to show:

1. Sample answers retrieved from synthetic internship records.
2. Fallback responses when internship details are unconfirmed.
3. Consent-based inquiry submission using fictional student information.

**Privacy and Security:**

The recording must not reveal API keys, passwords, private student information, or other sensitive credentials.

The demo is for educational and staging review purposes only.

## Project Status

**Current Stage:** Development prototype and staging review.

The application includes an AI-powered internship support interface, synthetic program data, policy lookup functionality, and a consent-based inquiry workflow.

Local testing has been performed during development. Staging deployment and production readiness must be verified separately.

**Production Status:** Not production-ready.

Before deployment for real student use, all requirements listed in the Production Gate section must be completed.
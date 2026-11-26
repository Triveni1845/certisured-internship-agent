# Certisured Internship AI Support Agent
A Python and LangGraph-backed ReAct-style student support prototype.

## Run locally
Install Python 3.11+, Git and VS Code. Create a virtual environment, then install requirements:
```bash
pip install -r requirements.txt
python db.py
python -m pytest -q
uvicorn web:app --reload
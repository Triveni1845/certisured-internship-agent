import json
from pathlib import Path
from langchain_core.tools import tool
ROOT=Path(__file__).parent
@tool
def get_program(program_id:str)->str:
 """Look up public program details by id AI, DATA or WEB."""
 rows=json.loads((ROOT/'data/programs.json').read_text(encoding='utf-8'))
 return json.dumps(next((x for x in rows if x['id']==program_id.upper()),{'status':'unknown_program'}))
@tool
def get_policy(question:str)->str:
 """Read the internship fees, timing and offer letter policy."""
 return json.dumps({'source':'data/policy.md','content':(ROOT/'data/policy.md').read_text(encoding='utf-8')})
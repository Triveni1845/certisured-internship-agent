import uuid
from pathlib import Path
from fastapi import FastAPI,HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel,Field
from agent import make_agent
from db import init,save
init()
app=FastAPI()
agent=None
class Question(BaseModel):
 question:str=Field(min_length=1,max_length=800)
 thread_id:str|None=None
class Inquiry(BaseModel):
 name:str=Field(min_length=1,max_length=100)
 email:str=Field(min_length=5,max_length=254)
 program:str=Field(min_length=1,max_length=100)
 consent:bool
@app.post('/api/ask')
def ask(req:Question):
 global agent
 if agent is None:
  try: agent=make_agent()
  except Exception: raise HTTPException(503,'Model unavailable')
 thread=req.thread_id or str(uuid.uuid4())
 if len(thread)>80: raise HTTPException(400,'Invalid thread')
 try:
  state=agent.invoke({'messages':[{'role':'user','content':req.question}]},config={'configurable':{'thread_id':thread},'recursion_limit':12})
  return {'answer':str(state['messages'][-1].content),'thread_id':thread}
 except Exception: raise HTTPException(503,'Unable to answer; contact staff')
@app.post('/api/inquiry')
def inquiry(req:Inquiry):
 if not req.consent: raise HTTPException(400,'Consent required')
 try: identifier=save(req.name,req.email,req.program)
 except ValueError as e: raise HTTPException(400,str(e))
 return {'id':identifier,'message':'Staff follow-up requested, no admission promised'}
@app.get('/api/health')
def health():return {'ok':True}
app.mount('/',StaticFiles(directory=str(Path(__file__).parent/'static'),html=True),name='static')
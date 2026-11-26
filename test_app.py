import json
from tools import get_program,get_policy
from db import init,save
def test_program(): assert json.loads(get_program.invoke({'program_id':'DATA'}))['weeks']==8
def test_unknown(): assert json.loads(get_program.invoke({'program_id':'XYZ'}))['status']=='unknown_program'
def test_fee(): assert 'unconfirmed' in get_policy.invoke({'question':'fee'}).lower()
def test_db():
 init()
 assert save('Sample','sample@example.test','AI')>0
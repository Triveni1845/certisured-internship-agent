import sqlite3
from pathlib import Path
DB=Path(__file__).parent/'inquiries.sqlite3'
def init():
 with sqlite3.connect(DB) as c:
  c.execute('CREATE TABLE IF NOT EXISTS inquiries(id INTEGER PRIMARY KEY,name TEXT,email TEXT,program TEXT,created TEXT DEFAULT CURRENT_TIMESTAMP)')
def save(name,email,program):
 if not name.strip() or '@' not in email or not program.strip(): raise ValueError('Invalid inquiry')
 with sqlite3.connect(DB) as c:
  cur=c.execute('INSERT INTO inquiries(name,email,program) VALUES(?,?,?)',(name.strip(),email.strip(),program.strip()))
  return cur.lastrowid
if __name__=='__main__':
 init()
 print('Database ready')
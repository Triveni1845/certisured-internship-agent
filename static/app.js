let thread=null;
document.getElementById('chat').onsubmit=async e=>{
 e.preventDefault();
 const q=document.getElementById('q').value;
 const h=document.getElementById('history');
 h.textContent+='You: '+q+'\n';
 try{
  const r=await fetch('/api/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({question:q,thread_id:thread})});
  const j=await r.json();thread=j.thread_id||thread;
  h.textContent+='Assistant: '+(j.answer||j.detail)+'\n\n';
 }catch{h.textContent+='Service unavailable\n'}
 document.getElementById('q').value='';
};
document.getElementById('lead').onsubmit=async e=>{
 e.preventDefault();
 const data={name:document.getElementById('name').value,email:document.getElementById('email').value,program:document.getElementById('program').value,consent:document.getElementById('consent').checked};
 const r=await fetch('/api/inquiry',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});
 const j=await r.json();
 document.getElementById('result').textContent=j.message||j.detail;
};
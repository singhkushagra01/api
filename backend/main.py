import fastapi
import embedchain
import os
from embedchain import App
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to your React app's URL in a production environment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
os.environ["OPENAI_API_KEY"] = "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"
application = App()
application.add(("What is myidfi", "myIDFi makes getting a new mortgage simple and easy"), data_type="qna_pair")
application.add(("Where do I go to loging to Realtor", "http://localhost:3000/signin?ROLE=REALTOR"), data_type="qna_pair")
application.add(("Where do I go to loging to Lender", "http://localhost:3000/signin?ROLE=LENDER"), data_type="qna_pair")
application.add(("Where do I go to loging to Customer", "http://localhost:3000/signin?ROLE=CUSTOMER"), data_type="qna_pair")
application.add(("Where do I go to the Website", "https://www.eddiequiroz.com/"), data_type="qna_pair")
application.add(("Where do I go to the About Us", "https://www.eddiequiroz.com/about-us/"), data_type="qna_pair")
application.add(("Where do I go to the Blog", "https://www.eddiequiroz.com/blog/"), data_type="qna_pair")
application.add(("Where do I go to the Contact Us", "https://www.eddiequiroz.com/contact-us/"), data_type="qna_pair")



class chatBOT(BaseModel):
    prompt:str
    max_tokens: int = 150

@app.post('/chatbot')
async def root(request: chatBOT):  
    k = application.query(request.prompt)
    return {'Message' : k}

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

#python -m main.py
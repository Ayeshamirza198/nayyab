from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user : [str,str,[str,str],str] = {}
class Registration(BaseModel):
    user_name : str
    email : str
    education : str
    info : str

class Login(BaseModel):
    email : str
    password : str
    login_detail : str

@app.post("/register")
def reg(info: str ):
    username = info.user.user_name
    email = info.user.email
    education = info.user.education
    if username in user:
        return {"message": "registered successfully"}
    else:
        return {"token": "not registered"}

@app.post("/login")
def login(login_detail : str):
    username = login_detail.user.username
    email = login_detail.user.email
    password = login_detail.user.password
    if username in user:
        return {"message: login successfully"}
    else:
        return {"token: unauthorized access"}





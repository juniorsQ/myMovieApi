from fastapi import APIRouter
from pydantic import BaseModel
from middlewares.jwt_bearer import JWTBearer
from fastapi.responses import HTMLResponse, JSONResponse
from jwt_manager import create_token

class User(BaseModel):
    email:str
    password:str

login_router = APIRouter()

#login  
@login_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email =="juniors@gmail.com" and user.password =="admin":
     token: str= create_token(user.dict())
     return JSONResponse(status_code=200, content=token)
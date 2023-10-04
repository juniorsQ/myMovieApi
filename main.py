from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import os
from config.database import engine,Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.login import login_router

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0",
#                 port=int(os.environ.get("PORT", 8000)))



app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(login_router)
app.include_router(movie_router)

# class User(BaseModel):
#     email:str
#     password:str


Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

#login  
# @app.post('/login', tags=['auth'])
# def login(user: User):
#     if user.email =="juniors@gmail.com" and user.password =="admin":
#      token: str= create_token(user.dict())
#      return JSONResponse(status_code=200, content=token)


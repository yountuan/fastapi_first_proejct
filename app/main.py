from fastapi import FastAPI
from app.auth.routers import router as auth_router
from app.auth.models import User
from app.database import create_table

app = FastAPI()
app.include_router(
    auth_router
)

@app.on_event('startup')
def create_tables():
    create_table()

@app.get('/home')
def home_page():
    return {'message':'Hello world'}


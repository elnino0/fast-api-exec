from fastapi import FastAPI
from Db.startup import create_db_and_tables, insert_users
from Routers.Auth import router as routerAuth
app = FastAPI()

app.include_router(routerAuth)
    
@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.on_event("startup")
async def on_startup():
    create_db_and_tables()
    await insert_users()

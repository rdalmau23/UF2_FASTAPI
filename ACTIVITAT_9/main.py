from fastapi import FastAPI
from schemas.users_sch import users_schema
from crud.users_crud import get_all_users

app = FastAPI()

@app.get("/users/", response_model=list[dict])
async def read_users():
    users = get_all_users()
    return users_schema(users)

from Db.Repos.UsersRepo import UsersRepo
from Db.Models.User import Users, pwd_context
from sqlmodel import SQLModel,Session
from Db.init_session import get_session,engine


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

users = [
    Users(name="fat John", email="fatJohn.com", hashed_password=pwd_context.hash("password")),
    Users(name="fat sara", email="fatsara.com", hashed_password=pwd_context.hash("password")),
    Users(name="fat sally", email="fatsally.com", hashed_password=pwd_context.hash("password")),
]

async def insert_users():
    with Session(engine) as session:
        users_repo = UsersRepo(session)
        await users_repo.create_users_if_not_exist(users)


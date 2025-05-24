from Db.Models.User import Users
from sqlmodel import Session, select

class UsersRepo():
    def __init__(self, session: Session):
        self.session = session

    async def get_all_users(self):
        return self.session.exec(Users).all()

    async def get_user_by_email(self, email):
        statement = select(Users).where(Users.email == email)

        user = self.session.exec(statement).one_or_none()
        return user

    async def create_user(self, user):
        self.session.add(user)
        self.session.commit()
        return user
    
    async def delete_user(self, user):
        self.session.delete(user)
        self.session.commit()
        return user
    
    async def update_user(self, user:Users, user_db:Users):
        user_db.name = user.name
        user_db.email = user.email
        user_db.hashed_password = user.hashed_password
        self.session.add(user_db)
        self.session.commit()
        return user
    
    async def create_users_if_not_exist(self, users: list[Users]):
        
        for user in users:
            user_db = await self.get_user_by_email(user.email)
            if user_db is None:
                 await self.create_user(user)
            else:
                await self.update_user(user, user_db)
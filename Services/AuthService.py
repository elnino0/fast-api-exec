from Db.Repos.UsersRepo import UsersRepo
from Modles.User import User
import jwt
import datetime
from config import AppConfig


SECRET_KEY = AppConfig.JWT_SECRECT
ALGORITHM = AppConfig.ALGORITHM
EXPIRES_IN = AppConfig.EXPIRES_IN

class AuthService():
    
    def __init__(self,session):
        self.user_repository = UsersRepo(session=session)
    
    async def login(self, user:User):
        db_user = await self.user_repository.get_user_by_email(user.email)
        if not db_user.verify_password(user.password):
            raise Exception("Invalid password")
        
        token = jwt.encode({"email":db_user.email,"exp": datetime.datetime.now() + datetime.timedelta(minutes=EXPIRES_IN)}, SECRET_KEY, algorithm=ALGORITHM)
        return token

    async def register(self, user:User):
        user = await self.user_repository.create_user(user)
        return user

    async def logout(self):
        pass
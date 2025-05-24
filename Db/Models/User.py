from passlib.context import CryptContext
from sqlmodel import Field, SQLModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str
    hashed_password: str
    
    def set_password(self, password: str):
        self.hashed_password = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)
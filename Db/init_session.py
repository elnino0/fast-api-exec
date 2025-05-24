from sqlmodel import Session ,SQLModel, create_engine


SQLALCHEMY_DATABASE_URL = "postgresql://your_user:your_password@localhost:5432/fat_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
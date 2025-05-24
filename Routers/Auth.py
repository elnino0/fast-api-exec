from fastapi import APIRouter, Depends
from Modles.User import User
from Services.AuthService import AuthService
from Db.init_session import get_session

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login")
async def login(user:User,session = Depends(get_session)):
    auth_service = AuthService(session=session)
    token = await auth_service.login(user)
    return {"token": token}

@router.post("/logout")
async def logout(session = Depends(get_session)):
    auth_service = AuthService(session=session)
    auth_service.logout()

@router.post("/register")
async def register(user:User, session = Depends(get_session)):
    auth_service = AuthService(session=session)
    await auth_service.register(user)
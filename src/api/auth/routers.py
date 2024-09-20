from fastapi import APIRouter, Depends
from sqlalchemy import insert, select

from api.auth.schemas import UserLoginSchema, UserSchema
from api.auth.utils import sign_jwt
from db.base import async_session
from db.models import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/signup")
async def create_user(user: UserSchema):
    query = (
        insert(User)
        .values(fullname=user.fullname, email=user.email, password=user.password)
        .returning(User.id)
    )
    async with async_session() as session:
        user_id = (await session.execute(query)).scalar()
        await session.commit()
        return sign_jwt(user_id)


@router.post("/login")
async def user_login(user: UserLoginSchema):
    query = select(User.id).where(
        User.email == user.email, User.password == user.password
    )
    async with async_session() as session:
        user_id = (await session.scalars(query)).one()
        if user_id:
            return sign_jwt(user_id)
    return {"error": "Wrong login details!"}

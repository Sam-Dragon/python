from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from database.db_config import get_session
from database.models import User

user_router = APIRouter(prefix="/users")


@user_router.get("/")
def get(session: Session = Depends(get_session)):
    statement = select(User)
    result = session.execute(statement).scalars().all()
    users = jsonable_encoder(result)

    return users


# @user_router.post("/")
# def post(user: User, session: Session = Depends(get_session)):
#     statement = insert(User)
#     session.execute(statement, user)
#     session.commit()

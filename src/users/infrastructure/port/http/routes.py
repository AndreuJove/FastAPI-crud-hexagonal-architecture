from typing import Dict

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.shared.database import get_db
from src.users.domain.schemas.user import UserBaseSchema
from src.users.infrastructure.dependency_injector.containers import UserControllerContainer

user_router = APIRouter()


@user_router.get("/", status_code=status.HTTP_200_OK)
def get_users(
    db_session: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ""
) -> Dict:
    users = UserControllerContainer.get_users()(db_session, limit, page, search)
    return {"Status": "Success", "Results": len(users), "Users": users}


@user_router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(payload: UserBaseSchema, db_session: Session = Depends(get_db)) -> Dict:
    new_user = UserControllerContainer.create_user()(db_session, payload)
    return {"Status": "Success", "User": new_user}


@user_router.patch("/{userId}", status_code=status.HTTP_202_ACCEPTED)
def update_user(userId: str, payload: UserBaseSchema, db_session: Session = Depends(get_db)):
    db_user = UserControllerContainer.get_user_by_id()(db_session, userId)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No User with this id: {userId} found",
        )
    update_data = payload.dict(exclude_unset=True)

    UserControllerContainer.update_user_by_id()(db_session, userId, update_data)
    return {"Status": "Success", "User": db_user}


@user_router.get("/{userId}", status_code=status.HTTP_200_OK)
def get_user(userId: str, db_session: Session = Depends(get_db)):
    db_user = UserControllerContainer.get_user_by_id()(db_session, userId)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No User with this id: `{userId}` found",
        )

    return {"Status": "Success", "User": db_user}


@user_router.delete("/{userId}", status_code=status.HTTP_200_OK)
def delete_user(userId: str, db_session: Session = Depends(get_db)):
    db_user = UserControllerContainer.get_user_by_id()(db_session, userId)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No user with this id: {userId} found",
        )

    UserControllerContainer.delete_user_by_id()(db_session, userId)
    return {"Status": "Success", "Message": "User deleted successfully"}

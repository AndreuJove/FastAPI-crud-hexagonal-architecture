from typing import Dict

from sqlalchemy.orm import Session

from src.users.domain.models.user import User
from src.users.domain.repositories.user_repository import UserRepository
from src.users.domain.schemas.user import UserBaseSchema


class SQLiteDBUserRepository(UserRepository):
    def __init__(self, user: User) -> None:
        self.user = user

    def get_users(self, db_session: Session, limit: int, page: int, search: str):
        skip = (page - 1) * limit
        users = (
            db_session.query(self.user)
            .filter(User.first_name.contains(search))
            .limit(limit)
            .offset(skip)
            .all()
        )

        return users

    def create_user(self, db_session: Session, payload: UserBaseSchema) -> User:
        new_user = self.user(**payload.dict())
        db_session.add(new_user)
        db_session.commit()
        db_session.refresh(new_user)
        return new_user

    def get_user_by_id(self, db_session: Session, id: str) -> User:
        user_query = db_session.query(self.user).filter(self.user.id == id)
        db_user = user_query.first()
        return db_user

    def update_user_by_id(self, db_session: Session, id: str, update_data: Dict) -> None:
        db_user = self.get_user_by_id(db_session, id)
        user_query = db_session.query(self.user).filter(self.user.id == id)
        user_query.filter(self.user.id == id).update(update_data, synchronize_session=False)
        db_session.commit()
        db_session.refresh(db_user)

    def delete_user_by_id(self, db_session: Session, id: str) -> None:
        user_query = db_session.query(self.user).filter(self.user.id == id)
        user_query.delete(synchronize_session=False)
        db_session.commit()

from sqlalchemy.orm import Session

from src.users.domain.repositories.user_repository import UserRepository


class CreateUser:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def __call__(self, db_session: Session, payload):
        users = self.user_repository.create_user(db_session, payload)
        return users

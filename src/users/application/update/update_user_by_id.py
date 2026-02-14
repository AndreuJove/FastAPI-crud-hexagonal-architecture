from typing import Dict

from sqlalchemy.orm import Session

from src.users.domain.repositories.user_repository import UserRepository


class UpdateUserById:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def __call__(self, db_session: Session, id: str, update_data: Dict) -> None:
        self.user_repository.update_user_by_id(db_session, id, update_data)

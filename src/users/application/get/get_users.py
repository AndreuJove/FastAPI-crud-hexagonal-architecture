from sqlalchemy.orm import Session

from src.users.domain.repositories.user_repository import UserRepository


class GetUsers:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def __call__(self, db_session: Session, limit: int = 10, page: int = 1, search: str = ""):
        users = self.user_repository.get_users(db_session, limit, page, search)
        return users

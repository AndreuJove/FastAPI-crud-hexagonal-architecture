from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton

from src.users.application.create.create_user import CreateUser
from src.users.application.delete.delete_user_by_id import DeleteUserById
from src.users.application.get.get_user_by_id import GetUserById
from src.users.application.get.get_users import GetUsers
from src.users.application.update.update_user_by_id import UpdateUserById
from src.users.domain.models.user import User
from src.users.infrastructure.repositories.sqlite_user_repository import SQLiteDBUserRepository


class UserRepositoryContainer(DeclarativeContainer):
    user = Singleton(
        SQLiteDBUserRepository,
        user=User,
    )


class UserControllerContainer(DeclarativeContainer):
    get_users = Singleton(GetUsers, user_repository=UserRepositoryContainer.user)
    create_user = Singleton(CreateUser, user_repository=UserRepositoryContainer.user)
    get_user_by_id = Singleton(GetUserById, user_repository=UserRepositoryContainer.user)
    update_user_by_id = Singleton(UpdateUserById, user_repository=UserRepositoryContainer.user)
    delete_user_by_id = Singleton(DeleteUserById, user_repository=UserRepositoryContainer.user)

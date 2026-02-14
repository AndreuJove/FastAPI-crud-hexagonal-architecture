from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def get_users(self, db, limit, page, search):
        pass

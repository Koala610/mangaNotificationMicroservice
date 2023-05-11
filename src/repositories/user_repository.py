from src.logger import logger
from .crud_repository import CRUDRepository
from typing import Type
from ..models.protocols.entity_protocol import DatabaseEntity
from ..models.user import User

class UserRepository(CRUDRepository):
    def __init__(self, dsn: str):
        super().__init__(User, dsn)
        logger.info("UserRepository initialized...")
    
    def check_if_subscribed(self, user_id):
        user = self.find_by_id(user_id)
        return True if user.is_subscribed else False

    def find_by_subscription(self, is_subscribed) -> object:
        with self.Session() as session:
            users = session.query(self.Object).filter_by(is_subscribed=is_subscribed).all()
            return users


def main():
    pass

if __name__ == "__main__":
    main()
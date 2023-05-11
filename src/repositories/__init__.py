from user_repository import UserRepository
from ..config import DSN

user_repository: UserRepository = UserRepository(DSN)
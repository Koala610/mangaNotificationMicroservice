from .user_repository import UserRepository
from .admin_repository import AdminRepository
from ..config import DSN

user_repository: UserRepository = UserRepository(DSN)
admin_repository: AdminRepository = AdminRepository(DSN)
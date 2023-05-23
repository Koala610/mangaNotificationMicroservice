from core_repository.admin_repository import AdminRepository
from core_repository.user_repository import UserRepository
from ..config import DSN

user_repository: UserRepository = UserRepository(DSN)
admin_repository: AdminRepository = AdminRepository(DSN)
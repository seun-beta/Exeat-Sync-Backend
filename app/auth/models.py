import enum

from sqlalchemy import Boolean, Column, Enum, Integer, String

from app.commons.base_model import TimeStampedBaseModel


class UserRole(enum.Enum):
    STUDENT = "student"
    ADMIN = "admin"
    SUPER_ADMIN = "super admin"


class User(TimeStampedBaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)
    email_address = Column(String(256), nullable=False, unique=True)
    phone_number = Column(String(30), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(UserRole))

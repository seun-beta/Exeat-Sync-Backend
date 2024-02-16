from datetime import datetime

from sqlalchemy import Column, DateTime, func

from app.database import Base


class TimeStampedBaseModel(Base):
    __abstract__ = True
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        server_onupdate=func.now(),
    )

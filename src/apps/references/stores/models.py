from src.core.db import Base
from sqlalchemy import Column, String, Integer


class Store(Base):
    __tablename__ = "ref_store"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(100), nullable=False)
    address = Column(String(250))


stores = Store.__table__

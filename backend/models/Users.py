from sqlalchemy import Column, VARCHAR, UUID
from sqlalchemy.dialects.postgresql import TEXT
from database.base import Base
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "users"
    id = Column(UUID, primary_key=True)
    username = Column(VARCHAR(length=255), unique=True, index=True)
    email = Column(VARCHAR(length=255), unique=True, index=True)
    password = Column(TEXT)
    
    cities = relationship("Cities", backref="Cities", lazy=True)
    
    def __init__(self, id:str, username:str, email:str, password:str) -> None:
        self.id = id
        self.username = username
        self.email = email
        self.password = password
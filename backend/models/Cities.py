from sqlalchemy import Column, Integer, VARCHAR, FLOAT, UUID, ForeignKey
from database.base import Base

class Cities(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID, ForeignKey("users.id"),  nullable=False )
    name = Column(VARCHAR(length=255), nullable=False)
    state = Column(VARCHAR(length=2), nullable=False)
    lat = Column(FLOAT, nullable=False)
    lon = Column(FLOAT, nullable=False)
    
    def __init__(self, name:str, state:str, lat:float, lon:float) -> None:
        self.name = name
        self.state = state,
        self.lat = lat
        self.lon = lon
    
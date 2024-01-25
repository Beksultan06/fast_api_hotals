from sqlalchemy import Column, Date, Integer, ForeignKey, CheckConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base

Base = declarative_base()

class Bookings(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_days = Column(Integer, CheckConstraint("total_days >= 0"), nullable=False, server_default=text("(date_to - date_from)"))

    # total_cost = Column(Integer, CheckConstraint("total_cost >= 0"), nullable=False, server_default=text("(date_to - date_from) * price"))
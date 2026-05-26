from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer,primary_key=True)
    user_name = Column(String)
    user_role = Column(String)
    user_email = Column(String)
    user_password = Column(String)

    risks = relationship("Risk",back_populates="user")

class Risk(Base):
    __tablename__ = "risks"

    risk_id = Column(Integer, primary_key=True)
    risk_title = Column(String)
    risk_description = Column(String)
    risk_priority = Column(String)
    risk_status = Column(String)
    risk_type = Column(String)
    risk_category = Column(String)
    created_by = Column(Integer)
    risk_allocation = Column(Integer)
    assigned_to = Column(Integer, ForeignKey("users.user_id"))
    due_date = Column(String)

    user = relationship("User", back_populates= "risks")




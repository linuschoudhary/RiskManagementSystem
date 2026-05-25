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
    risk_description = Column(String)
    risk_priority = Column(String)
    risk_status = Column(String)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    risk_type = Column(String)


    user = relationship("User", back_populates= "risks")

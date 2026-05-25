from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine("sqlite:///Model/database.db", echo=False)


Session = sessionmaker(bind= engine)

session = Session()
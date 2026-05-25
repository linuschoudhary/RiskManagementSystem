from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine("sqlite:///Model/database.db", echo=False)


Session = sessionmaker(bind= engine)

def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()
        

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


db_url = "postgresql://postgres:acecse15@localhost:5432/FastApi"

engine = create_engine(db_url)

session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

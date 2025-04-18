from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# user postgres, password 07052003, database trangvang_db
DATABASE_URL = "postgresql+psycopg2://postgres:07052003@localhost:5432/trangvang_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

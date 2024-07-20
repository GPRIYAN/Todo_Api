from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlalchemy_database_url = "sqlite:///./sqlite.db"
engine_sql = create_engine(sqlalchemy_database_url, connect_args={"check_same_thread": False})
session_sql = sessionmaker(autocommit=False, autoflush=False, bind=engine_sql)
Base = declarative_base()
# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "postgresql://todofastsapi_user:X4n5Jbs0g9RcXFgcr4QdVAl2UxipaWor@dpg-d0qrb4p5pdvs73asd4h0-a.singapore-postgres.render.com/todofastsapi"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

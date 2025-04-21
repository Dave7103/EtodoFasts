# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "postgresql://todofastapi_v2g7_user:erMWTu3PyspcAuQn76vUJKyI5egFmo7f@dpg-d02udcje5dus73c5rdgg-a/todofastapi_v2g7"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

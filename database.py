# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "postgresql://fastsapi_user:P2PUAADQYAH1vCj7VRojdXSfBb6w3nXR@dpg-d0qr4druibrs73es7h2g-a.virginia-postgres.render.com/fastsapi"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

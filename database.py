from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#db_url = "postgresql://postgres:vivuvi@localhost:5432/pos"
db_url = "postgresql://postgres.tbdnwbgettbiqmbnlhfp:197346Pos_12@aws-1-eu-north-1.pooler.supabase.com:5432/postgres"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False,autoflush=False,bind = engine)

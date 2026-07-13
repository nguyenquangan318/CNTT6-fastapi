from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


URL = "mysql+pymysql://root:Quangan310820@localhost:3306/test_db"

engine = create_engine(URL)

Base = declarative_base()

LocalSession = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
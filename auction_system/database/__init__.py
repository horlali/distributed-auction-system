from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from auction_system.utils.directories import BASE_DIR

sqlite_file_name = "db.sqlite3"
sqlite_url = f"sqlite:///{BASE_DIR}/{sqlite_file_name}"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    from auction_system.database.models import Auction, Base, Bid, User

    Base.metadata.create_all(
        engine,
        tables=[User.__table__, Auction.__table__, Bid.__table__],
    )


Session = sessionmaker(bind=engine)
session = Session()

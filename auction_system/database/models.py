from enum import Enum

from sqlalchemy import Column, DateTime
from sqlalchemy import Enum as db_enum
from sqlalchemy import Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, relationship

Base = declarative_base()


class UserType(Enum):
    SELLER: str = "seller"
    BIDDER: str = "bidder"


class AuctionStatus(Enum):
    ACTIVE: str = "active"
    CLOSED: str = "closed"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    user_type = Column(db_enum(UserType), nullable=False)


class Token(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True)
    token = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    users = relationship("User", backref="token", lazy=True)


class Auction(Base):
    __tablename__ = "auctions"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    starting_price = Column(Float, nullable=False)
    reserved_price = Column(Float, nullable=False)
    seller = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(
        db_enum(AuctionStatus),
        default=AuctionStatus.ACTIVE,
        nullable=False,
    )

    users = relationship("User", backref="auction", lazy=True)


class Bid(Base):
    __tablename__ = "bids"
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    auction_id = Column(Integer, ForeignKey("auctions.id"), nullable=False)

    users = relationship("User", backref="bid", lazy=True)


sqlite_url = "sqlite:///db.sqlite3"
engine = create_engine(sqlite_url)
session = Session(engine)

Base.metadata.create_all(engine)

import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class UserType(enum.Enum):
    SELLER: str = "seller"
    BIDDER: str = "bidder"


class AuctionStatus(enum.Enum):
    ACTIVE: str = "active"
    CLOSED: str = "closed"
    SOLD: str = "sold"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    user_type = Column(Enum(UserType), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)


class Auction(Base):
    __tablename__ = "auctions"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    starting_price = Column(Float, nullable=False)
    reserved_price = Column(Float, nullable=False)
    seller_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(Enum(AuctionStatus), default=AuctionStatus.ACTIVE, nullable=False)

    # users = relationship("User", backref="auction", lazy=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)


class Bid(Base):
    __tablename__ = "bids"
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    bidder_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    auction_id = Column(Integer, ForeignKey("auctions.id"), nullable=False)

    # users = relationship("User", backref="bid", lazy=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

from datetime import datetime
from enum import Enum

from beanie import Document, PydanticObjectId
from pydantic import EmailStr, Field


class UserType(str, Enum):
    BUYER = "buyer"
    SELLER = "seller"


class AuctionStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SOLD = "sold"


class User(Document):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    email: EmailStr
    password_hash: str
    user_type: UserType


class Token(Document):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    token: str
    user_id: PydanticObjectId


class Auction(Document):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    title: str
    description: str
    start_time: datetime
    end_time: datetime
    starting_price: float
    reserved_price: float
    seller: PydanticObjectId
    status: AuctionStatus


class Bid(Document):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    amount: float
    user_id: PydanticObjectId
    auction_id: PydanticObjectId

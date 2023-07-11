import marshmallow as ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

from auction_system.server.database import session
from auction_system.server.database.models import (
    Auction,
    AuctionStatus,
    Bid,
    User,
    UserType,
)


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        include_relationships = True
        sqla_session = session

    user_type = ma.fields.Enum(UserType)
    created_at = auto_field(load_only=True)


class AuctionSchema(SQLAlchemyAutoSchema):
    status = ma.fields.Enum(AuctionStatus)

    class Meta:
        model = Auction
        load_instance = True
        include_relationships = True
        include_fk = True
        sqla_session = session


class BidSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Bid
        load_instance = True
        include_relationships = True
        include_fk = True
        sqla_session = session

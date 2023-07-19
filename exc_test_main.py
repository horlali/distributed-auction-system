from datetime import datetime

from faker import Faker
from werkzeug.security import generate_password_hash

from auction_system.server.database import create_db_and_tables, session
from auction_system.server.database.models import (
    Auction,
    AuctionStatus,
    Bid,
    User,
    UserType,
)
from auction_system.server.database.schemas import AuctionSchema, BidSchema, UserSchema

fake = Faker()
user_schema = UserSchema()
auction_schema = AuctionSchema()
bid_schema = BidSchema()


def main():
    print("==================USER===================")
    user = User(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        phone=fake.phone_number(),
        email=fake.email(),
        password_hash=generate_password_hash(fake.password()),
        user_type=UserType.BIDDER,
    )

    session.add(user)
    session.commit()

    user = session.query(User).get(user.id)
    user.user_type = UserType.BIDDER
    session.commit()

    users = session.query(User).filter_by(id=user.id)

    for x in users:
        print(user_schema.dump(x))

    print("==================AUCTION===============")
    auction = Auction(
        title="My first auction",
        description="My first auction description",
        start_time=datetime.now(),
        end_time=datetime.now(),
        starting_price=100,
        reserved_price=200,
        seller_id=user.id,
        status=AuctionStatus.ACTIVE,
    )

    session.add(auction)
    session.commit()

    auctions = session.query(Auction).all()
    for y in auctions:
        print(auction_schema.dump(y))

    print("==================BID====================")
    bid = Bid(amount=100, bidder_id=user.id, auction_id=auction.id)

    session.add(bid)
    session.commit()

    bids = session.query(Bid).all()
    for z in bids:
        print(bid_schema.dump(z))


# Run the main function
if __name__ == "__main__":
    create_db_and_tables()
    main()

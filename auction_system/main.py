from auction_system.auth.authenticator import Authenticator
from auction_system.database.models import (
    Auction,
    AuctionStatus,
    Base,
    Bid,
    Token,
    User,
    UserType,
    engine,
    session,
)

Base.metadata.create_all(engine)


if __name__ == "__main__":
    auth = Authenticator()
    # a = auth.register(
    #     email="admin2@example.com",
    #     password="admin",
    #     user_type=UserType.SELLER,
    # )
    # b = auth.login(
    #     email="admin2@example.com",
    #     password="admin",
    # )

    c = auth.logout("5422aba5-1bfd-4f8e-801a-11ba3d174b0f")

    user = session.query(User).filter_by(email="admin2@example.com").first()
    
    print(user.token)

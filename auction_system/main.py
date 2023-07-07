from auction_system.auth.authenticator import Authenticator
from auction_system.database.models import Base, UserType, engine

Base.metadata.create_all(engine)


if __name__ == "__main__":
    auth = Authenticator()
    auth.register(
        email="admin2@example.com",
        password="admin",
        user_type=UserType.SELLER,
    )

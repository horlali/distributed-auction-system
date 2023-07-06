from sqlmodel import Field, Session, SQLModel, create_engine


# Define the SQLModel classes for the tables
class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    password: str
    role: str


class Auction(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    item_name: str
    starting_price: float
    reserve_price: float
    start_time: str
    end_time: str
    seller_id: int


class Bid(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    auction_id: int
    bidder_id: int
    amount: float


# Create the database engine and session
sqlite_url = "sqlite:///auction_system.db"
engine = create_engine(sqlite_url)
session = Session(engine)

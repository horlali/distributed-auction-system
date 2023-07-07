from auction_system.database import Base, engine

Base.metadata.create_all(engine)

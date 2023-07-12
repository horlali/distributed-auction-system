import logging

import Pyro4

from auction_system.server.database import create_db_and_tables
from auction_system.server.remote_objects.auctions_bids import AuctionBidObject
from auction_system.server.remote_objects.authenticator import Authenticator
from auction_system.utils.constants import AUCTION_OBJECT_ID, AUTH_OBJECT_ID, HOST, PORT

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


remote_objects = {
    AUCTION_OBJECT_ID: AuctionBidObject,
    AUTH_OBJECT_ID: Authenticator,
}


if __name__ == "__main__":
    create_db_and_tables()
    daemon = Pyro4.Daemon(host=HOST, port=PORT)
    for object_id, object_class in remote_objects.items():
        uri = daemon.register(object_class(), objectId=object_id)
        logger.info(f"Auction System Server Ready. Object URI: {uri}")

    daemon.requestLoop()

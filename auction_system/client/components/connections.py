import Pyro4

from auction_system.utils.constants import AUCTION_OBJECT_ID, AUTH_OBJECT_ID, HOST, PORT

AUCTION_URI = f"PYRO:{AUCTION_OBJECT_ID}@{HOST}:{PORT}"
AUTH_URI = f"PYRO:{AUTH_OBJECT_ID}@{HOST}:{PORT}"

auction_bid_object = Pyro4.Proxy(AUCTION_URI)
auth_object = Pyro4.Proxy(AUTH_URI)

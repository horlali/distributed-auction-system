import os

import Pyro4

from auction_system.utils.constants import (
    AUCTION_OBJECT_ID,
    AUTH_OBJECT_ID,
    BASE_DIR,
    HOST,
    PORT,
)

AUCTION_URI = f"PYRO:{AUCTION_OBJECT_ID}@{HOST}:{PORT}"
AUTH_URI = f"PYRO:{AUTH_OBJECT_ID}@{HOST}:{PORT}"

auction_bid_object = Pyro4.Proxy(AUCTION_URI)
auth_object = Pyro4.Proxy(AUTH_URI)

cart_image = os.path.join(BASE_DIR, "auction_system/client/assets/biz.svg")

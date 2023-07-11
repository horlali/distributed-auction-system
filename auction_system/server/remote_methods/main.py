from datetime import datetime, timedelta

from auction_system.server.database.models import AuctionStatus
from auction_system.server.remote_methods.auctions_bid_objects import AuctionBidObject

auc_bid_obj = AuctionBidObject()

auction_data = {
    "title": "test auction",
    "description": "test auction description",
    "start_time": datetime.now(),
    "end_time": datetime.now() + timedelta(days=1),
    "starting_price": 100,
    "reserved_price": 1000,
    "seller_id": 1,
    "status": AuctionStatus.ACTIVE,
}

bid_data = {
    "amount": 100,
    "bidder_id": 1,
    "auction_id": 1,
}


print("============create_auction_data=================")
create_auction_data = auc_bid_obj.create_auction(auction_data)
print(create_auction_data)


print("============get_single_auction_data=================")
get_single_auction_data = auc_bid_obj.get_single_auction(create_auction_data["id"])
print(get_single_auction_data)


print("============get_all_active_auctions=================")
print(auc_bid_obj.get_all_active_auctions())

print("============close_auction=================")


print("============place_bid=================")


print("============get_my_bids=================")


print("============get_my_auctions=================")


print("============get_bidders_for_my_auctions=================")


print("============get_auction_winner=================")

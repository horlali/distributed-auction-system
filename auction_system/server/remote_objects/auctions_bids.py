import Pyro4

from auction_system.server.database import session
from auction_system.server.database.models import Auction, AuctionStatus, Bid
from auction_system.server.database.schemas import AuctionSchema, BidSchema, UserSchema


@Pyro4.expose
class AuctionBidObject(object):
    def __init__(self):
        self.session = session
        self.user_schema = UserSchema()
        self.auction_schema = AuctionSchema()
        self.bid_schema = BidSchema()

    def create_auction(self, auction_data):
        print(auction_data)
        auction = Auction(**auction_data)
        self.session.add(auction)
        self.session.commit()

        return self.auction_schema.dump(auction)

    def get_single_auction(self, auction_id):
        auction = self.session.query(Auction).filter_by(id=auction_id).first()

        return self.auction_schema.dump(auction)

    def get_all_active_auctions(self):
        auctions = (
            self.session.query(Auction).filter_by(status=AuctionStatus.ACTIVE).all()
        )

        return self.auction_schema.dump(auctions, many=True)

    def close_auction(self, auction_id):
        auction = self.session.query(Auction).filter_by(id=auction_id).first()
        auction.status = AuctionStatus.CLOSED
        self.session.commit()

        return self.auction_schema.dump(auction)

    def place_bid(self, bid_data):
        bid = Bid(**bid_data)
        self.session.add(bid)
        self.session.commit()

        return self.bid_schema.dump(bid)

    def get_my_bids(self, user_id):
        bids = self.session.query(Bid).filter_by(bidder_id=user_id).all()

        return self.bid_schema.dump(bids, many=True)

    def get_my_auctions(self, user_id):
        auctions = self.session.query(Auction).filter_by(seller_id=user_id).all()

        return self.auction_schema.dump(auctions, many=True)

    def get_bidders_for_my_auctions(self, user_id):
        auctions = self.session.query(Auction).filter_by(seller_id=user_id).all()
        bidders = []
        for auction in auctions:
            bids = self.session.query(Bid).filter_by(auction_id=auction.id).all()
            for bid in bids:
                bidders.append(bid.bidder_id)

        return self.user_schema.dump(bidders, many=True)

    def get_auction_winner(self, auction_id):
        bids = self.session.query(Bid).filter_by(auction_id=auction_id).all()
        reserved_price = (
            self.session.query(Auction).filter_by(id=auction_id).first().reserved_price
        )

        if bids:
            highest_bid = max(bids, key=lambda x: x.amount)
            if reserved_price > highest_bid.amount:
                return self.user_schema.dump(highest_bid.bidder_id)
            else:
                return "Reserved price not met"

        else:
            return None

    def check_bid_status(self, auction_id, bidder_id):
        bids = self.session.query(Bid).filter_by(auction_id=auction_id).all()
        auction = self.session.query(Auction).filter_by(id=auction_id).first()

        reserved_price = auction.reserved_price
        auction_status = auction.status

        if bids:
            highest_bid = max(bids, key=lambda x: x.amount)

            if auction_status == AuctionStatus.ACTIVE:
                return "Auction is still active, check back later."

            # if bids.count(highest_bid) > 1:
            #     return "There are ties in the bids, please check back later."

            if highest_bid.bidder_id == bidder_id:
                if reserved_price >= highest_bid.amount:
                    return "Your bid won this auction and the reserved price is met."
                else:
                    return "Your bid won this auction but the reserved price is not met."

            else:
                return "Bid lost."

        else:
            return "No bids found for this auction."

    def withdraw_bid(self, bid_id):
        bid = self.session.query(Bid).filter_by(id=bid_id).first()
        auction = self.session.query(Auction).filter_by(id=bid.auction_id).first()

        if auction.status == AuctionStatus.CLOSED:
            return "You cannot withdraw a bid for a closed auction."

        self.session.delete(bid)
        self.session.commit()

        return "Bid withdrawn successfully"

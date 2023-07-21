import streamlit as st
from Pyro4.errors import CommunicationError

from auction_system.client.components.connections import auction_bid_object
from auction_system.client.components.states import authentication_state

st.set_page_config(page_title="Buyer", page_icon="👋", layout="wide")
st.write("## Manage Your Bids Here 👋")

authentication_state()


def show_my_bids():
    st.divider()

    try:
        auctions = []
        bids = auction_bid_object.get_my_bids(user_id=st.session_state["user_id"])

        for bid in bids:
            auction = auction_bid_object.get_single_auction(auction_id=bid["auction_id"])
            auction["bid_amount"] = bid["amount"]
            auctions.append(auction)

            col1, col2 = st.columns([2, 1.2])

            with col1:
                st.write(f"**Item title:** {auction['title']}")
                st.write(f"**Item description:** {auction['description']}")
                st.write(f"**Auction status:** {auction['status']}")
                st.write(f"**Starting price:** {auction['starting_price']}")
                st.write(f"**Bid amount:** {auction['bid_amount']}")

            with col2:
                if st.button("**Check Bid Status**", key=f"{bid['id']}_"):
                    bid_status = auction_bid_object.check_bid_status(
                        auction_id=auction["id"],
                        bidder_id=st.session_state["user_id"],
                    )
                    st.write(f"**Bid Status:** {bid_status}")

                if auction["status"] == "ACTIVE":
                    st.divider()

                    if st.button("**Withdraw Bid**", key=f"{bid['id']}__"):
                        auction_bid_object.withdraw_bid(bid["id"])
                        st.success("Bid withdrawn successfully")

                        if st.button("Refresh"):
                            st.experimental_rerun()

            st.divider()

    except CommunicationError:
        st.error("Server is not running. Please start the server first.")
        st.divider()


if __name__ == "__main__":
    if st.session_state["authenticated"]:
        show_my_bids()

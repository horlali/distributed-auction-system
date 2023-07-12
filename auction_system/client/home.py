import streamlit as st

from auction_system.client.components.connections import auction_bid_object

st.set_page_config(page_title="Auction System", page_icon="👋", layout="wide")
st.write("# Welcome to the Special Auction System 👋")


# write a function to show all the auctions
def show_auctions():
    # get all the auctions from the server
    st.write("## All Auctions")
    auctions = auction_bid_object.get_all_active_auctions()

    # list the auctions in a grid view
    for auction in auctions:
        st.write(f"### {auction['title']}")
        st.write(f"### {auction['description']}")
        st.write(f"### {auction['reserved_price']}")
        st.write(f"### {auction['starting_price']}")
        st.write(f"### {auction['status']}")
        st.write(f"### {auction['seller_id']}")
        st.write(f"### {auction['created_at']}")
        st.write(f"### {auction['id']}")

        # create a button to place a bid
        if st.button("Place a bid", key=auction["id"]):
            # show a form to place a bid
            bid_amount = st.number_input("Enter your bid amount", min_value=0.0)
            # create a bid object
            if bid_amount:
                bid_data = {
                    "amount": bid_amount,
                    "bidder_id": auction["seller_id"],
                    "auction_id": auction["id"],
                }
                # place the bid
                bid = auction_bid_object.place_bid(bid_data)
                st.success(f"Your bid has been placed successfully: {bid}")
                # refresh the page
                st.experimental_rerun()


if __name__ == "__main__":
    show_auctions()

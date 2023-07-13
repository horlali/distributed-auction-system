from datetime import datetime
from typing import Dict, List

import streamlit as st

from auction_system.client.components.connections import auction_bid_object, cart_image

st.set_page_config(page_title="Auction System", page_icon="👋", layout="wide")
st.write("# Welcome to the Special Auction System 👋")


def show_auctions():
    st.write("#### Recent Active Auctions")
    st.divider()
    auctions: List[Dict] = auction_bid_object.get_all_active_auctions()

    for auction in auctions:
        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            st.image(cart_image, width=150)

        with col2:
            start_time = datetime.fromisoformat(
                auction["start_time"],
            ).strftime("%B %d, %Y %I:%M %p")

            end_time = datetime.fromisoformat(
                auction["end_time"],
            ).strftime("%B %d, %Y %I:%M %p")

            st.text(f"Item title: {auction['title']}")
            st.text(f"Item description: {auction['description']}")
            st.text(f"Starting price: {auction['starting_price']}")
            st.text(f"Auction status: {auction['status']}")
            st.text(f"Auction started at: {start_time}")
            st.text(f"Auction ends at: {end_time}")
            st.text(f"Seller ID: {auction['seller_id']}")

        with col3:
            # create a button to place a bid
            if st.button("Place a bid", key=auction["id"]):
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
                    st.write(bid)
                    st.success(f"Your bid has been placed successfully: {bid}")

                    # refresh the page
                    st.experimental_rerun()
        st.divider()


if __name__ == "__main__":
    show_auctions()

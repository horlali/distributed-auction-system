from datetime import datetime
from typing import Dict, List

import streamlit as st
from Pyro4.errors import CommunicationError

from auction_system.client.components.connections import auction_bid_object, cart_image
from auction_system.client.components.states import authentication_state

st.set_page_config(page_title="Auction System", page_icon="👋", layout="wide")
st.write("# Welcome to the Group 8's Auction System 👋")

authentication_state()


def show_auctions():
    st.write("#### Recent Active Auctions")
    st.divider()

    try:
        auctions: List[Dict] = auction_bid_object.get_all_active_auctions()

        # TODO: Sort auctions by end time
        # auctions = sorted(auctions, key=lambda x: x["end_time"])

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

                st.write(f"**Item title:** {auction['title']}")
                st.write(f"**Item description:** {auction['description']}")
                st.write(f"**Starting price:** {auction['starting_price']}")
                st.write(f"**Auction status:** {auction['status']}")
                st.write(f"**Auction started at:** {start_time}")
                st.write(f"**Auction ends at:** {end_time}")

            with col3:
                bid_amount = st.number_input(
                    "Enter your bid amount", min_value=0.0, key=auction["id"]
                )

                if st.button("Checkout", key=f"{auction['id']}_"):
                    if bid_amount < auction["starting_price"]:
                        st.error(
                            f"Your bid amount should be greater than or equal to {auction['starting_price']}"  # noqa: E501
                        )

                    elif datetime.now() > datetime.fromisoformat(auction["end_time"]):
                        st.error(f"Sorry, the auction ended on {end_time}")

                    elif auction["seller_id"] == st.session_state["user_id"]:
                        st.error("You cannot bid on your own auction")

                    else:
                        bid_data = {
                            "amount": bid_amount,
                            "bidder_id": st.session_state["user_id"],
                            "auction_id": auction["id"],
                        }

                        bid = auction_bid_object.place_bid(bid_data)
                        st.success(
                            f"Your successfully placed a bid of **{bid['amount']}** for this item"  # noqa: E501
                        )

            st.divider()

    except CommunicationError:
        st.error("Server is not running. Please start the server first.")
        st.divider()


if __name__ == "__main__":
    if st.session_state["authenticated"]:
        show_auctions()

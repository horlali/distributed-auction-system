from datetime import datetime
from typing import Dict, List

import streamlit as st
from Pyro4.errors import CommunicationError

from auction_system.client.components.connections import auction_bid_object

st.set_page_config(page_title="Seller", page_icon="👋", layout="wide")
st.write("## Manage Your Auctions Here 👋")


def get_all_my_auctions():
    """get all the auctions created by the seller"""

    st.write("#### All My Auctions")
    st.divider()

    try:
        auctions: List[Dict] = auction_bid_object.get_my_auctions(1)

        for auction in auctions:
            col1, col2, col3 = st.columns([2, 2, 1.2])

            with col1:
                st.write("**Auction Details**")
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

            with col2:
                st.write("**Bidders**")
                bidders = auction_bid_object.get_bidders_for_my_auctions(1)
                for bidder in bidders:
                    st.write(
                        f"**Name:** {bidder['name']} **Amount:** {bidder['bid_amount']}"
                    )

            with col3:
                st.write("**Actions**")
                if st.button("Close Auction", key=f"{auction['id']}_"):
                    auction_bid_object.close_auction(auction["id"])
                    st.success("Auction closed successfully")

                    if st.button("Refresh"):
                        st.experimental_rerun()

            st.divider()

    except CommunicationError:
        st.error("Failed to connect to the server")


def add_auction():
    """add a new auction"""

    st.write("#### Add New Auction")

    with st.form(key="add_auction_form", clear_on_submit=False):
        title = st.text_input("Title")
        description = st.text_area("Description")
        col1, col2 = st.columns([1, 1])

        with col1:
            start_date = st.date_input("Start Date", min_value=datetime.now())
            end_date = st.date_input("End Date", min_value=datetime.now())

        with col2:
            start_time = st.time_input("Start Time")
            end_time = st.time_input("End Time")

        starting_price = st.number_input("Starting Price", min_value=0.0)
        reserved_price = st.number_input("Reserved Price", min_value=0.0)
        seller_id = st.number_input("Seller ID", step=1, format="%i")
        submit_form = st.form_submit_button(label="Submit Auction")

        # combine date and time
        start_date_val = datetime.combine(start_date, start_time)
        end_date_val = datetime.combine(end_date, end_time)

        if submit_form:
            form_data = {
                "title": title,
                "description": description,
                "start_time": start_date_val,
                "end_time": end_date_val,
                "starting_price": starting_price,
                "reserved_price": reserved_price,
                "seller_id": seller_id,
                "status": "ACTIVE",
            }

            try:
                auction_bid_object.create_auction(form_data)
                st.success("Auction created successfully")

            except CommunicationError:
                st.error("Failed to connect to the server")


if __name__ == "__main__":
    add_auction()
    st.divider()
    get_all_my_auctions()

from datetime import datetime

import streamlit as st
from Pyro4.errors import CommunicationError

from auction_system.client.components.connections import auction_bid_object

st.set_page_config(page_title="Seller", page_icon="👋", layout="wide")
st.write("## Manage Your Auctions Here 👋")


def get_all_my_auctions():
    """get all the auctions created by the seller"""

    st.write("#### All My Auctions")
    try:
        auction_bid_object.get_my_auctions(1)

    except CommunicationError:
        st.error("Failed to connect to the server")


def close_auction():
    """close the auction if the deadline is reached"""
    ...


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

        starting_price = st.number_input("Starting Price")
        reserved_price = st.number_input("Reserved Price")
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
                response = auction_bid_object.create_auction(form_data)

            except CommunicationError:
                st.error("Failed to connect to the server")


def proces_add_auction_form(
    title,
    description,
    start_time,
    end_time,
    starting_price,
    reserved_price,
    seller_id,
    status,
):
    response = auction_bid_object.create_auction(
        title,
        description,
        start_time,
        end_time,
        starting_price,
        reserved_price,
        seller_id,
        status,
    )

    if response:
        st.success("Auction added successfully")

    else:
        st.error("Failed to add auction")


# pick a winner for the auction
def pick_auction_winner():
    ...


# get bidders for the auction (secondary functionality)
def get_bidders():
    ...


if __name__ == "__main__":
    add_auction()

from datetime import datetime
from typing import Dict, List

import streamlit as st
from Pyro4.errors import CommunicationError

from auction_system.client.components.connections import auction_bid_object, cart_image
from auction_system.server.database.models import AuctionStatus

st.set_page_config(page_title="Seller", page_icon="👋", layout="wide")
st.write("## Manage Your Auctions Here 👋")

# get all my auctions
def get_all_my_auctions():
    st.write("#### All My Auctions")
    if st.button("Add New Auction", key="add_auction"):
        add_auction()
    
    headers = ["Title", "Description", "Start Time", "End Time", "Starting Price", "Reserved Price", "Seller ID", "Status"]
    data = auction_bid_object.get_my_auctions(1)
    st.dataframe(data)

# close the auction if the deadline is reached

# add a new auction
def add_auction():
    st.write("#### Add New Auction")
    with st.form(key="add_auction_form", clear_on_submit=False):
        title = st.text_input("Title")
        description = st.text_input("Description")
        col1, col2 = st.columns([1, 1])
        with col1:
            start_date = st.date_input("Start Date")
            end_date = st.date_input("End Date")
        with col2:
            start_time = st.time_input("Start Time")
            end_time = st.time_input("End Time")
        starting_price = st.number_input("Starting Price")
        reserved_price = st.number_input("Reserved Price")
        seller_id = st.number_input("Seller ID", format="%i")
        status = st.radio("Status", ('active', AuctionStatus.CLOSED))
        submit_form = st.form_submit_button(label="Submit", help="Click to register!")
        
        print(start_date)
        print(start_time)
        #combine date and time
        start_date_val = datetime.combine(start_date, start_time)
        end_date_val = datetime.combine(end_date, end_time)
        print(start_date_val)
        if submit_form:
            form_data = {
                "title": title, 
                "description": description, 
                "start_time": start_date_val, 
                "end_time": end_date_val, 
                "starting_price": starting_price, 
                "reserved_price":reserved_price,
                "seller_id": seller_id, 
                "status":status
            }
            
            print("submit button clicked", form_data)
            response = auction_bid_object.create_auction(form_data)   
            print(response)
        #proces_add_auction_form(title, description, start_time, end_time, starting_price, reserved_price, seller_id, status)
    
def proces_add_auction_form(title, description, start_time, end_time, starting_price, reserved_price, seller_id, status):
    response = auction_bid_object.create_auction(title, description, start_time, end_time, starting_price, reserved_price, seller_id, status)   
    print(response)
    if response:
        st.success("Auction added successfully")
    else:
        st.error("Failed to add auction")

#title
#description
#start_time
#end_time
#starting_price
#reserved_price
#seller_id
#status radio button

# pick a winner for the auction
def pick_auction_winner():
    ...

# get bidders for the auction (secondary functionality)
def get_bidders():
    ...


if __name__ == "__main__":
    #get_all_my_auctions()
    add_auction()
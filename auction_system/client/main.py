import Pyro4
import streamlit as st

# Connect to the Pyro4 server
auction_server = Pyro4.Proxy("PYRO:auction.server@localhost:50001")


# Seller interface
def seller_interface():
    st.title("Seller Interface")

    # Login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Authenticate the seller
        # ...
        ...

    if seller_authenticated:
        # Seller actions
        if st.button("Create Auction"):
            # Auction creation form
            item_name = st.text_input("Item Name")
            starting_price = st.number_input("Starting Price")
            reserve_price = st.number_input("Reserve Price")
            duration = st.number_input("Duration (in minutes)")
            if st.button("Create"):
                # Create a new auction
                auction_server.create_auction(
                    seller_id, item_name, starting_price, reserve_price, duration
                )
                st.success("Auction created successfully!")

            # Display active auctions
            st.subheader("Active Auctions")
            active_auctions = auction_server.get_active_auctions()
            for auction in active_auctions:
                st.write(auction)

            # Auction closure
            auction_id = st.text_input("Enter Auction ID to close")
            if st.button("Close Auction"):
                # Close the auction
                auction_server.close_auction(seller_id, auction_id)
                st.success("Auction closed successfully!")


# Main program
if __name__ == "__main__":
    seller_interface()

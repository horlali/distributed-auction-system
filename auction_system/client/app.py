import Pyro4

# Connect to the Pyro4 server
auction_server = Pyro4.Proxy("PYRO:auction.server@localhost:50001")

import Pyro4


@Pyro4.expose
class Server(object):
    def __init__(self):
        self._auctions = {}

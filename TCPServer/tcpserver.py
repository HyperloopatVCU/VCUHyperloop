from queue import Queue
from socket import *


class TCPComm(object):

    def __init__(self, host='localhost', port=8000):

        print("[+] Initializing Communication")

        self.packets = Queue()
        self.host = host
        self.port = port

        self.client = None

        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((self.host, self.port))

    def connect(self):
        self.server.listen(4)
        print("[+] Listening on port", self.port)

        self.client = self.server.accept()

    def start(self):
        while True:
            data = self.client.recv(4096)

            if not data:
                break

            self.packets.put(data)


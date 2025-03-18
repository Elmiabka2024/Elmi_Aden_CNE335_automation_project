#Elmi Aden
#CNE335 - 3/9/2025
# working on to ping the EC2 in code
import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip, key_pair=None):
        # TODO -

            self.server_ip = server_ip
            self.key_pair = key_pair

    def ping(self):
        # TODO - Use os module to ping the server
        response = os.system(f'ping -n 5 {self.server_ip}')
        return response == 0


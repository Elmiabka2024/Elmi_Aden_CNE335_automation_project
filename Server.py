#Elmi Aden
#CNE335 - 3/9/2025
# working on to ping the EC2 in code
import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_dns, key_pair=None):
        # TODO -

            self.server_dns = server_dns
            self.key_pair = key_pair

    def ping(self):
        # TODO - Use os module to ping the server
        print(f"pinging {self.server_dns}")
        response = os.system(f'ping -n 5 {self.server_dns}')
        return response == 0


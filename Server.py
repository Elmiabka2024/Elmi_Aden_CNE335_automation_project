#Elmi Aden
#CNE335 - 3/9/2025
# working on to ping the EC2 in code
import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip, key_pair ):
        # TODO -
        self.server_ip = server_ip
        self.server_ip = server_ip
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.key = paramiko.RSAKey.from_private_key_file(key_pair)

    def ping(self):
        # TODO - Use os module to ping the server
        if os.system(f'ping -n 5 {self.server_ip}') == 0:
            return True
        else:
            return False

        def run_command(self, command):
            try:
                self.ssh.connect(hostname=self.server_ip, username='ubuntu', pkey=self.key)
                stdin, stdout, stderr = self.ssh.exec_command(command)
                print(stdout.read().decode())
                print(stderr.read().decode())
            finally:
                self.ssh.close()
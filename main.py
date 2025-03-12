#Elmi Aden
#CNE335 - 3/9/2025
# working on to ping the EC2 in code

# This is the template code for the CNE335 Final Project
# Justin Ellis
# CNE 335 Fall
from Server import Server
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Elmi")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    ec2 = Server("34.219.24.30")
    # TODO - Call Ping method and print the results
    ec2.ping()
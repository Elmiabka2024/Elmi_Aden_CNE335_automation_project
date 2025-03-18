#Elmi Aden
#CNE335 - 3/9/2025
# working on to ping the EC2 in code


from Server import Server
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Elmi")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    server_dns = "ec2-34-219-24-30.us-west-2.compute.amazonaws.com"
    key_pair = r"C:\Users\warah\Downloads\Elmi_CNE335.pem"
    ec2 = Server(server_dns, key_pair)
    # TODO - Call Ping method and print the results
    if ec2.ping():
        print(f"Server {ec2.server_dns} is reachable!")
    else:
        print(f"Server {ec2.server_dns} is not reachable.")
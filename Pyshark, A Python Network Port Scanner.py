import socket


def input_int(prompt: str = "") -> int:
    """Prompt user for an integer value until success."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer. Try again.")


def is_valid_port_number(port: int) -> bool:
    """Checks if the port number is valid."""
    return 1 <= port <= 65535


def is_port_open(host: str, port: int) -> bool:
    """Test if the port at the host is open."""
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # 1-second timeout
        result = sock.connect_ex((host, port))
    return result == 0  # 0 means the connection was successful


#
# Start of main program
#
print("Welcome to pyshark, your friendly Python network port scanner")

while True:
    print("\n--- Begin Port Scan Sequence ---")

    host = input("Enter host name of server to test: ")
    port = input_int(f"Enter port number on {host} to test: ")

    if not is_valid_port_number(port):
        print("Invalid port number, please try again")
        continue

    if is_port_open(host, port):
        port_status = "open"
    else:
        port_status = "closed"
    print(f"Port {port} on {host} is {port_status}")

    print("--- End Port Scan Sequence ---")

    usr_input = input("\nType 'y' or 'yes' to begin another port scan sequence: ")
    if not (usr_input == "y" or usr_input == "yes"):
        break

print("\nThank you for using pyshark, your friendly Python network port scanner")

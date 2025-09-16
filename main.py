import socket


def input_int(prompt: str = "") -> int:
    """Prompt user for an integer value until success.

    Calls input() with prompt until the user enters a valid integer.

    Returns:
        An integer value converted from the string input from user.

    Args:
        prompt: An optional text string pased into the input() statement.
    """
    raise NotImplementedError


def is_valid_port_number(port: int) -> bool:
    """Tests to make sure port number is within the valid range

    Tests to make sure that the port is greater or equal to 1 and less
    than 65,536.

    Returns:
        True if the port number is valid, else False.

    Args:
        port: port number to test
    """
    raise NotImplementedError


def is_port_open(host: str, port: int) -> bool:
    """Test port at host to see if it is open.

    A simple network port tester using the socket Python standard library
    to attempt to open the specified host/port.

    Returns:
        True if open, False for anything else

    Args:
        host: Host name of the target server.
        port: Number of the port to be tested.
    """
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
    return result == 0  # result of 0 indicates that connection succeeded


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

import socket

def input_int(prompt=""):
    while True:
        val = input(prompt)
        try:
            return int(val)
        except ValueError:
            print(f"{val} is not an integer. Try again.")

def valid_port(port):
    return 1 <= port <= 65535

def valid_host(host):
    return host.strip() != ""

def port_open(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        return s.connect_ex((host, port)) == 0

print("Welcome to pyshark, your friendly Python network port scanner")

while True:
    print("\n--- Begin Port Scan Sequence ---")
    while True:
        host = input("Enter host name of server to test: ")
        if valid_host(host):
            break
        print("Invalid host name. Please enter a non-empty string.")

    port = input_int(f"Enter port number on {host} to test: ")
    if not valid_port(port):
        print("Invalid port number, please try again")
        continue

    status = "open" if port_open(host, port) else "closed"
    print(f"Port {port} on {host} is {status}")
    print("--- End Port Scan Sequence ---")

    if input("\nType 'y' or 'yes' to begin another port scan sequence: ").lower() not in ("y", "yes"):
        break

print("\nThank you for using pyshark, your friendly Python network port scanner")

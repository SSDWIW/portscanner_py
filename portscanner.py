#port scanner in py

import socket

address = input("Please enter the IP or domain you would like to scan: ")
firstPort = int(input("Please input the lowest port in the range to scan: "))
#ensures that the highest port is included in the scan instead of being the endpoint
lastPort = int(input("Please input the highest port in the range to scan: ")) + 1


def scanPorts(address, firstPort, lastPort):
    #array to put open ports in
    openPorts = []

    for port in range(firstPort, lastPort):
        try:
            #socket.AF_INET takes either ip address or domain name
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #sets timeout if closed and the script is hung
            sock.settimeout(1)
            result = sock.connect_ex((address, port))

            # adds port to list if open
            if result == 0:
                openPorts.append(port)

            sock.close()

        except socket.error:
            pass

    return openPorts

openPorts = scanPorts(address, firstPort, lastPort)

if openPorts:
    print(f"Open ports found on {address}:")
    for port in openPorts:
        print(port)
else:
    print(f"No open ports detected on {address}")

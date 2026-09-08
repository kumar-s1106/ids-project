import socket
import datetime

target = input("Enter IP to scan: ")
print("Scanning " + target)
print("Started at: " + str(datetime.datetime.now()))
print("-" * 40)

open_ports = []

for port in range(1, 1025):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print("PORT " + str(port) + " OPEN")
            open_ports.append(port)
        sock.close()
    except:
        continue

print("-" * 40)
print("Scan complete")
print("Open ports found: " + str(len(open_ports)))

import socket
import subprocess
import sys
from datetime import datetime

remoteServer = input("Enter a remote host to scan  ")
remoteServerIP = socket.gethostbyname(remoteServer)

print("-" * 60)
print("Please wait, scanning ", remoteServerIP)
print("-" * 60)

t1 = datetime.now()
print(t1)
try:
	for port in range(1, 1025):
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		print(port)

	if result == 0:
		print("Port {}: Open".format(port))
	sock.close()

except KeyboardInterrupt:
	print("You print Ctrl + C")
	sys.exit()

except socket.gaierror:
	print("Host name cannot be resolved, exiting")
	sys.exit()

t2 = datetime.now()

total = t2-t1

print("Scanning completed in ", total)

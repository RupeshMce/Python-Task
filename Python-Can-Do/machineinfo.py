import socket
import json
import getpass
from urllib.request import urlopen


# Read UserName of the Machine
username=getpass.getuser()
print("UserName : {}".format(username))

# Read HostName of the Machine
hostname=socket.gethostname()
print("HostName : {}".format(hostname))

# Get the Machine Ip
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("IpAddress:",s.getsockname()[0])
s.close()




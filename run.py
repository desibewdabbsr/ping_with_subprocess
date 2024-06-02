import subprocess

def ping(host):
    """
    Returns True if the host responds to a ping request.
    """
    param = '-n' if os.name == 'nt' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0

# Read IP addresses from the file
with open('C:\\Users\\imper\\OneDrive\\Desktop\\IP_Address.txt') as file:
    ip_addresses = file.read().splitlines()

# Ping each IP address
for ip in ip_addresses:
    if ping(ip):
        print(f"{ip} is up!")
    else:
        print(f"{ip} is down!")

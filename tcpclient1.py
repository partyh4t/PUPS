
import socket

target_host = "127.0.0.1"
target_port = 8080

# Creates a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connects to the client 
client.connect((target_host,target_port))

# Sends some data to the client
client.send(b"Testing!")

#store the response in a variable (max buffer of 4096)
response = client.recv(4096)

# decode & print the response since its in binary format
print(response.decode())

# print the length of the response in bytes
print(len(response))
client.close()
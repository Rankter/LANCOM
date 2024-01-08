import socket
import time

print(socket.gethostbyname_ex(socket.gethostname()))
print(socket.gethostbyname_ex(socket.gethostname())[2])
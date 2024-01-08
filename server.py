# sever.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 8088
s.bind((host, port))
try:
    while True:
        receive_data, addr = s.recvfrom(1024)
        print("来自服务器" + str(addr) + f"的消息: {receive_data.decode('utf-8')}")
        # print(receive_data.decode('utf-8'))
        msg = input('please input send to msg:')
        s.sendto(msg.encode('utf-8'), addr)
except:
    s.close()

import socket

SERVER_PORT = 9013
#insert ipv6 address of your device
SERVER_ADDR = 'fdee:f1e7:b9b5:10:b827:ebff:fe5e:6de'
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
server_addr = (SERVER_ADDR, SERVER_PORT, 0, 0)
sock.bind(server_addr)
print("Server started...")
while 1 :
    recv_data = sock.recvfrom(8)
    print(recv_data)
    sock.sendto(recv_data[0], recv_data[1])
sock.close()
del sock

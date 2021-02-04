import socket

#insert ipv6 address of your device
SERVER_ADDR = '2a02:8071:287:4e00:8525:7c01:71c0:6180'
SERVER_PORT = 9000
sequence_number = 1
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
payload = "Ping"
while sequence_number < 101 :
    sequence_payload = payload + str(sequence_number)
    data = bytes(sequence_payload, "UTF-8")
    sock.sendto(data, (SERVER_ADDR, SERVER_PORT, 0, 0))
    recv_data = sock.recvfrom(8)
    print(recv_data)
    rx_sequence_payload = recv_data[0]

    if sequence_payload != rx_sequence_payload.decode("UTF-8"):
        print("Sequence number mismatch!")
    sequence_number+= 1
sock.close()
del sock
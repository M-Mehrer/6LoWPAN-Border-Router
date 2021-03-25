import socket

#insert ipv6 address of your device
SERVER_ADDR = 'fdee:f1e7:b9b5:10:b827:ebff:fe5e:6de'
SERVER_PORT = 9013
sequence_number = 1
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
payload = "Ping"
while sequence_number < 101 :
    sequence_payload = payload + str(sequence_number)
    data = bytes(sequence_payload, "UTF-8")
    sock.sendto(data, (SERVER_ADDR, SERVER_PORT, 0, 0))
    print("sent...")
    recv_data = sock.recvfrom(8)
    print("received...")
    print(recv_data)
    rx_sequence_payload = recv_data[0]

    if sequence_payload != rx_sequence_payload.decode("UTF-8"):
        print("Sequence number mismatch!")
    sequence_number+= 1
sock.close()
del sock
import socket

#insert ipv6 address of your device
SERVER_ADDR = 'fd76:afe2:b6b0:0:b827:ebff:fe5e:6de'
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
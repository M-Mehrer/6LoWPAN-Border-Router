import socket
import time

SERVER_PORT_BLE = 9010
SERVER_ADDR_BLE = 'fdee:f1e7:b9b5:10:b827:ebff:fe5e:6de'
ble_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
server_addr_ble = (SERVER_ADDR_BLE, SERVER_PORT_BLE, 0, 0)

SERVER_PORT_WLAN = 9020
SERVER_ADDR_WLAN = '2003:e5:2722:bf00:2245:adce:3308:888c'
wlan_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
server_addr_wlan = (SERVER_ADDR_WLAN, SERVER_PORT_WLAN, 0, 0)

RESPONSE_PORT = 9030
RESPONSE_ADDR = '2003:e5:2722:bf00:855b:ebe4:2980:1e7c'
response_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
response_addr = (RESPONSE_ADDR, RESPONSE_PORT, 0, 0)
response_socket.bind(response_addr)

FILENAME = "TestPayload"

buff_size = [8, 32, 128, 1024, 8192, 32768, 131072]
for buff in buff_size:
    print("Start BLE with buffer size " + str(buff))
    f = open(FILENAME, 'rb')
    data = f.read(buff)
    start = time.time()
    while (data):
        ble_socket.sendto(data, server_addr_ble)
        try:
            response_socket.settimeout(20)
            recv_data = response_socket.recvfrom(buff)
            data = f.read(buff)
        except socket.timeout:
            print("Timeout")
    duration = time.time() - start
    print(str(duration))
    ble_socket.sendto(bytes("END", "UTF-8"), server_addr_ble)
    recv_data = response_socket.recvfrom(buff)
    f.close()

    print("Start WLAN with buffer size " + str(buff))
    f = open(FILENAME, 'rb')
    data = f.read(buff)
    start = time.time()
    while (data):
        wlan_socket.sendto(data, server_addr_wlan)
        try:
            wlan_socket.settimeout(2)
            recv_data = wlan_socket.recvfrom(buff)
            data = f.read(buff)
        except socket.timeout:
            print("Timeout")
    duration = time.time() - start
    print(str(duration))
    wlan_socket.sendto(bytes("END", "UTF-8"), server_addr_wlan)
    recv_data = wlan_socket.recvfrom(buff)
    f.close()
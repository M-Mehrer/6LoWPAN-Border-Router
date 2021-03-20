import socket

SERVER_PORT_BLE = 9010
SERVER_ADDR_BLE = 'fdee:f1e7:b9b5:10:b827:ebff:fe5e:6de'
ble_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
server_addr_ble = (SERVER_ADDR_BLE, SERVER_PORT_BLE, 0, 0)
ble_socket.bind(server_addr_ble)

SERVER_PORT_WLAN = 9020
SERVER_ADDR_WLAN = '2003:e5:2722:bf00:2245:adce:3308:888c'
wlan_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
server_addr_wlan = (SERVER_ADDR_WLAN, SERVER_PORT_WLAN, 0, 0)
wlan_socket.bind(server_addr_wlan)

RESPONSE_PORT = 9030
RESPONSE_ADDR = '2003:e5:2722:bf00:855b:ebe4:2980:1e7c'
response_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
response_addr = (RESPONSE_ADDR, RESPONSE_PORT, 0, 0)

print("Server started...")

buff_size = [8, 32, 128, 1024, 2048, 4096, 8192, 32768, 131072]
while 1 :
    print("Ready for test")
    for buff in buff_size:
        # receiving = True
        # while receiving:
        #     try:
        #         ble_socket.settimeout(20)
        #         recv_data = ble_socket.recvfrom(buff)
        #         if(recv_data[0] == "END".encode("UTF-8")):
        #             receiving = False
        #         response_socket.sendto(recv_data[0], response_addr)
        #     except socket.timeout:
        #         print("Timeout")
        receiving = True
        while receiving:
            try:
                wlan_socket.settimeout(2)
                recv_data = wlan_socket.recvfrom(buff)
                if(recv_data[0] == "END".encode("UTF-8")):
                    receiving = False
                wlan_socket.sendto(recv_data[0], recv_data[1])
            except socket.timeout:
                print("Timeout")


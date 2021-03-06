from socket import *
import struct
from functools import partial

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 100

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    msg = input('>>> ').strip()
    if not msg: continue
    if msg == 'break': break
    tcp_client.send(msg.encode('utf-8'))

    # 解決黏包
    data_length = tcp_client.recv(4)
    length_tuple = struct.unpack('i', data_length)
    length = length_tuple[0]

    # recv_size = 0
    # recv_msg = b''
    # while recv_size < length:
    #     recv_msg += tcp_client.recv(buffer_size)
    #     recv_size = len(recv_msg)
    # print('服務端發來的信息 ', recv_msg.decode('BIG5'))

    recv_msg = ''.join(iter(partial(tcp_client.recv, 1024), b''))
    print('服務端發來的信息 ', recv_msg.decode('BIG5'))

tcp_client.close()
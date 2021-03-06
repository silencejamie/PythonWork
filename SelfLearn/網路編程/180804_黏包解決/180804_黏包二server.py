from socket import *

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)  # 創建socket服務器
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 這行會重啟ip和端口，這樣就不會造成地址被占用的錯誤
tcp_server.bind(ip_port)  # 將地址綁到服務器
tcp_server.listen(back_log)  # 監聽鏈結


conn, addr = tcp_server.accept()  # 接收客戶端鏈結，並得到 (連結, 地址)

data1 = conn.recv(1)
print('第一次接收數據 ', data1)

data2 = conn.recv(5)
print('第二次接收數據 ', data2)

data3 = conn.recv(5)
print('第三次接收數據 ', data3)

conn.close()
tcp_server.close()
import socket

HOST = '192.168.1.33'
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

data = "여기에 입력할 데이터 적어주세요"

data_send = data.encode()

client_socket.sendall(data_send)

client_socket.close()
import socket
import ssl

context = ssl._create_unverified_context()

sock = socket.socket()
secure_sock = context.wrap_socket(sock, server_hostname="localhost")

secure_sock.connect(("127.0.0.1", 4444))

secure_sock.send(b"Hello secure server!")

data = secure_sock.recv(1024)
print("Server says:", data.decode())

secure_sock.close()
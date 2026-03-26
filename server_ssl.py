import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

sock = socket.socket()
sock.bind(("0.0.0.0", 4444))
sock.listen(5)

print("🔐 SSL Server running on port 4444...")

while True:
    client, addr = sock.accept()
    secure_conn = context.wrap_socket(client, server_side=True)

    data = secure_conn.recv(1024)
    print(f"[SECURE] Received from {addr}: {data.decode()}")

    secure_conn.send(b"Secure connection established!")

    secure_conn.close()
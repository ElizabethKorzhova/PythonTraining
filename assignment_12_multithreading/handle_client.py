"""Web server that serves multiple clients simultaneously."""
import sys
from typing import Tuple
import socket
import threading

HOST = "127.0.0.1"
PORT = 8080


def handle_client(client_socket, client_address: Tuple) -> None:
    """Handle a single client's HTTP request."""
    sys.stdout.write(f"Client connected: {client_address}")

    request = client_socket.recv(1024).decode()
    sys.stdout.write(request)

    response_body = "Hello! This is a multithreaded web server."
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "\r\n"
        f"{response_body}"
    )

    client_socket.sendall(response.encode())
    client_socket.close()

    sys.stdout.write(f"Client disconnected: {client_address}")



if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    sys.stdout.write(f"Server running on http://{HOST}:{PORT}")

    while True:
        socket, address = server_socket.accept()

        thread = threading.Thread(target=handle_client, args=(socket, address))
        thread.start()
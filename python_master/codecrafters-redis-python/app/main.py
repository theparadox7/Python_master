import socket  # noqa: F401


def main():
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    # server_socket.accept() # wait for client
    # client,addr = server_socket.accept()
    # client.send(b"+PONG\r\n")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    # server_socket.accept()  # wait for client
    client, addr = server_socket.accept()
    client.send(b"+PONG\r\n")

if __name__ == "__main__":
    main()

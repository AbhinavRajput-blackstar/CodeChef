import socket

def server_sock():
    host = socket.gethostname()  # to get the host name
    port = 8888  # initiating port no. above 1024
    print("Creating socket.... ")
    server_socket = socket.socket()  # Create socket
    print("Socket created, now binding with host - {} and port - {}".format(host, port))
    server_socket.bind((host, port))  # Binding host address with port address
    print("Socket Bound")

    server_socket.listen(1)  # Server listening to one client
    print("Listening.... ")
    conn, address = server_socket.accept()  # accepting new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. It won;t accept data packet greater than 1024 bytes.
        data = conn.recv(1024).decode()
        if data == 'bye':
            print("From connected user: " + str(data))
            break
        print("From connected user: " + str(data))

        data = "Echo confirmed, thank you for Connecting!"
        conn.send(data.encode())  # Send data to the client

    print("Closing Connection... ")
    conn.close()  # close the connection


if __name__ == "__main__":
    server_sock()

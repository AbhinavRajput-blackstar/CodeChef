import socket


def client_sock():
    host = socket.gethostname()        # As both code are running on same pc
    port = 8888                       # Socket server port number
    print("Creating socket.... ")
    client_socket = socket.socket()    # Instantiate
    print("Socket created, now binding with host - {} and port - {}".format(host, port))
    client_socket.connect((host, port))   # Connect to the server
    print("Socket Bound")

    message = input("Enter echo message to the send (under 1024 bytes): ")

    while message.lower().strip() != 'bye':  # termination check
        print("Sending Message.... ")
        client_socket.send(message.encode())       # send message
        data = client_socket.recv(1024).decode()   # receive response
        print("Received from server: {}".format(data))   # Show in terminal
        message = input("Enter 'bye' to end or another message: ")
        if message == 'bye':
            client_socket.send(message.encode())

    print("Closing Connection... ")
    client_socket.close()     # close the connection


if __name__ == "__main__":
    client_sock()

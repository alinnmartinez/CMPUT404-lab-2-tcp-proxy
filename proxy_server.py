import socket
from threading import Thread

BYTES_TO_READ = 4096
PROXY_SERVER_HOST = "127.0.0.1"
PROXY_SERVER_PORT = 8080

# accepts request, relays them to a target, recives what the target returns, then sends that response to the person who sent the request
# has both server and client sockets bc it's a client for the google server and bc it's a server for the client

def send_request(host, port, request_data):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # sending data to google
        client_socket.connect((host, port))
        client_socket.send(request_data)
        client_socket.shutdown(socket.SHUT_WR)
        # Getting response from google
        data = client_socket.recv(BYTES_TO_READ)
        result = b'' + data
        while len(data) > 0:
            data = client_socket.recv(BYTES_TO_READ)
            return result

def handle_connection(conn, addr):

    with conn:
        print(f"Connected by: {addr}")
        request = b''
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            request += data

        response = send_request("www.google.com", 80, request)
        conn.sendall(response)

def start_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_SERVER_HOST, PROXY_SERVER_PORT))
        # allows a socket to be rebound to the same address
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # level of protocal stack, option name, true
        server_socket.listen(2)  # param tells program how many connections is allowed? two connections then the rest gets qeued?
        conn, addr = server_socket.accept()

def start_threaded_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_SERVER_HOST, PROXY_SERVER_PORT))
        # allows a socket to be rebound to the same address
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # level of protocal stack, option name, true
        server_socket.listen(2)

    while True:
        conn, addr = server_socket.accept()
        thread = Thread(target=handle_connection, args=(conn, addr))
        thread.run()


#start_server()
start_threaded_server()


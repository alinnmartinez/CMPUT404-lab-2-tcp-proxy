#!/usr/bin/env python3
import socket
import time

#define address & buffer size
HOST = "127.0.0.1"
#PORT = 8001
PORT = 8080
BUFFER_SIZE = 1024

# def handle_connection(conn, addr):
#
#     with conn:
#         print(f"Connected by {addr}")
#               while True:
#                 data = conn.recv(BUFFER_SIZE)
#                 if not data:
#                     break
#                 print(data)
#                 conn.sendall(data)  # sending back from the server we recived it from (echo)
#                 # send doesn't garuantee all ur data gets sendt, sendall will return an errror if data wasn't recived
#
#
# def start_server():
#
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         # allows a socket to be rebound to the same address
#         s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # level of protocal stack, option name, true
#         s.listen()
#
#         conn, addr = s.accept()
#         handle_connection(conn, addr)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            #recieve data, wait a bit, then send it back
            full_data = conn.recv(BUFFER_SIZE)
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()

if __name__ == "__main__":
    main()

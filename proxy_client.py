import socket

BYTES_TO_READ = 4096


def get(host, port):
    # sending raw bytes by using b""
    request = b"GET / HTTP1.1\www.google.com\n\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(request)
        # shuts down the right part of the socket  (client.py --> google) tells it we're done transmitting
        s.shutdown(socket.SHUT_WR)

        print("Waiting for response")
        chunk = s.recv(BYTES_TO_READ)  # receive stuff from google
        result = b'' + chunk

        while len(chunk) > 0:
            chunk = s.recv(BYTES_TO_READ)
            result += chunk

        return result

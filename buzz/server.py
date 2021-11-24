import socket

SERVER_PORT = ''
SERVER_IP = ''

try:

    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
except socket.error, e:
    print("[ERROR] %s\n" % e[1])

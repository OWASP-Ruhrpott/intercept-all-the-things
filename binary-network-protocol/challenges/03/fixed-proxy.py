#!/usr/bin/python

import socket
from hashlib import md5
import socket
import sys
import threading

def modify(message):
    print("\033[91m[!]\033[00m Start modification of request...")
    #### START IMPLEMENTING YOUR LOGIC HERE

    

    #### END
    response = message
    print("\033[91m[!]\033[00m Modified request:", response)
    return response

def sendTCPMessage(ip, port, message):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    client.send(message)
    response = client.recv(4096)
    return response

def handle_client_connection(client_socket, ip, dst_port):
    request = client_socket.recv(1024)
    print("\033[92m[+] Receive from client:\033[00m", request)

    modified_request = modify(request)

    response = sendTCPMessage(ip, dst_port, modified_request)
    print("\033[91m[+] Response from server:\033[00m", response)

    client_socket.send(response)
    client_socket.close()

def main(argv):
    src_port = 6665
    ip = '0.0.0.0'
    dst_port = 9999

    if(argv != [] and len(argv) == 3):
        src_port = int(argv[0])
        ip = argv[1]
        dst_port = int(argv[2])
    else:
        print("Help: fixed-proxy <src_port> <ip> <dst_port>")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, src_port))
    server.listen(5)  # max backlog of connections

    print('\033[92m[+] Listening to client on '+ip+":"+str(src_port)+"\033[00m")
    print('\033[91m[+] Sending intercepted packets to server on'+ip+':'+str(dst_port)+"\033[00m")

    while True:
        try:
            client_sock, address = server.accept()
            print()
            print("\033[96m[+] Accepted connection from "+address[0]+":"+str(address[1])+"\033[00m")
            client_handler = threading.Thread(
                target=handle_client_connection,
                args=(client_sock,ip,dst_port)
            )
            client_handler.start()
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main(sys.argv[1:])

import socket
import ssl
import time

HOST = '127.0.0.1' # Local computer IP
PORT = 65432 # Arbitrary port number

protocol = ssl.PROTOCOL_SSLv23 # Here you can specify the encryption protocol
cipher = '' # Ciphers supported by that protocol can be specified as well

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    with ssl.wrap_socket(sock, ssl_version = protocol, ciphers = cipher) as ssock:
        print('Connected using algorithm:', ssock.cipher()) # Outputs which cipher was used to make the handshake
        data = ssock.recv(1024).decode()

        while data is not None: # Run loop indefinitely to output what gets received from server
            data = None

            try:
                data = ssock.recv(1024).decode() # Decode received data as it comes in as byte objects
                print('Received:', data)
                time.sleep(5)
            except (Exception) as ex:
                temp = '\nError Type: {0} \nArguments: {1!r}'
                message = temp.format(type(ex).__name__, ex.args)
                print(message)
                print('Closing socket...')
                ssock.close()
                break

        sock.close()
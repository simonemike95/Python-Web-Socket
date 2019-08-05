import socket
import ssl
import time

HOST = '127.0.0.1' # Local computer IP
PORT = 65432 # Arbitrary port number

protocol = ssl.PROTOCOL_SSLv23 # Here you can specify the encryption protocol
cipher = '' # Ciphers supported by that protocol can be specified as well

print('Listening on port {0}...'.format(PORT))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    with ssl.wrap_socket(sock, ssl_version = protocol, ciphers = cipher) as ssock:
        conn, addr = ssock.accept()

        while True: # Runs loop indefinitely to send data to client every 5 seconds
            try:
                print('Connected client {0}'.format(addr))
                dataToSend = 'Hello!'
                conn.send(bytes(dataToSend, encoding = 'utf-8')) # Encodes dataToSend string as byte object
                time.sleep(5)
            except (Exception) as ex:
                temp = '\nError Type: {0} \nArguments: {1!r}'
                message = temp.format(type(ex).__name__, ex.args)
                print(message)
                print('Closing socket...')
                ssock.close()
                break
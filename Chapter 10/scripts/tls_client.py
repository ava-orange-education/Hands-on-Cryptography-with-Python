import socket
import ssl

def create_tls_client():
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the socket with TLS
    context = ssl.create_default_context()
    tls_client_socket = context.wrap_socket(client_socket, server_hostname='localhost')

    # Connect to the server
    tls_client_socket.connect(('localhost', 8443))
    print("Connected to the TLS server.")

    # Receive data from the server
    message = tls_client_socket.recv(1024)
    print("Received message from server:", message.decode('utf-8'))

    # Close the connection
    tls_client_socket.close()
    print("Connection closed.")

if __name__ == "__main__":
    create_tls_client()
import socket
import ssl

def create_tls_server():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8443))
    server_socket.listen(5)
    print("Server is listening on port 8443...")

    # Wrap the socket with TLS
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    # Accept incoming connections
    while True:
        # Accept a new connection
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} accepted.")

        # Wrap the client socket with TLS
        try:
            tls_client_socket = context.wrap_socket(client_socket, server_side=True)
            print("TLS handshake completed successfully.")
            
            # Send a message to the client
            tls_client_socket.send(b"Hello, TLS Client! You are connected securely.\n")
        except ssl.SSLError as e:
            print(f"TLS handshake failed: {e}")
        finally:
            # Close the connection
            tls_client_socket.close()
            print("Connection closed.")

if __name__ == "__main__":
    create_tls_server()
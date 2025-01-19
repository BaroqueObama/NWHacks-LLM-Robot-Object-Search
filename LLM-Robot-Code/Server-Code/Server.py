import socket

class Server:
    def __init__(self, host="206.87.203.235", port=5111):
        self.host = host
        self.port = port
        self.server_socket = None
        self.connection = None
        self.address = None

    def start(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(1)
            print(f"Server listening on {self.host}:{self.port}")
        except Exception as e:
            print(f"Error starting server: {e}")

    def accept_connection(self):
        try:
            self.connection, self.address = self.server_socket.accept()
            print(f"Connected by {self.address}")
        except Exception as e:
            print(f"Error accepting connection: {e}")

    def receive(self):
        try:
            if self.connection:
                buffer = b""  # Use a buffer to accumulate chunks
                while True:
                    chunk = self.connection.recv(1024)
                    if not chunk:  # No more data to read
                        break
                buffer += chunk
                data = buffer.decode()
                print(f"Received from client: {data}")
                return data
            else:
                print("No active connection.")
        except Exception as e:
            print(f"Error receiving data: {e}")

    def send(self, message):
        try:
            if self.connection:
                self.connection.sendall(message.encode())
                print(f"Sent to client: {message}")
            else:
                print("No active connection to send data.")
        except Exception as e:
            print(f"Error sending data: {e}")

    def close_connection(self):
        try:
            if self.connection:
                self.connection.close()
                print("Connection with client closed.")
                self.connection = None
            else:
                print("No active connection to close.")
        except Exception as e:
            print(f"Error closing connection: {e}")

    def stop(self):
        try:
            if self.server_socket:
                self.server_socket.close()
                print("Server stopped.")
            else:
                print("Server is not running.")
        except Exception as e:
            print(f"Error stopping server: {e}")
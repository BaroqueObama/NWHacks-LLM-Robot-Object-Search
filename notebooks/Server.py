import socket

class Server:
    def __init__(self, host="", port=8081):
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
                data = self.connection.recv(1024).decode()
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

server = Server()
server.start()
server.accept_connection()
data = server.receive()
if data:
    server.send("hello")
server.close_connection()
server.stop()
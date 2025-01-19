import socket

class Client:
    def __init__(self, host="206.87.203.235", port=5000):
        self.host = host
        self.port = port
        self.client_socket = None

    def connect(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            print("Connected to server")
        except Exception as e:
            print(f"Error connecting to server: {e}")

    def send(self, message):
        try:
            if self.client_socket:
                self.client_socket.sendall(message.encode())
                print(f"Sent to server: {message}")
            else:
                print("Client is not connected to the server.")
        except Exception as e:
            print(f"Error sending message: {e}")

    def receive(self):
        try:
            if self.client_socket:
                response = self.client_socket.recv(1024).decode()
                print(f"Received from server: {response}")
                return response
            else:
                print("Client is not connected to the server.")
        except Exception as e:
            print(f"Error receiving message: {e}")

    def disconnect(self):
        try:
            if self.client_socket:
                self.client_socket.close()
                print("Connection closed.")
                self.client_socket = None
            else:
                print("Client is not connected to the server.")
        except Exception as e:
            print(f"Error disconnecting: {e}")
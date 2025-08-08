import socket
import json
import time

class RPSClient:
    def __init__(self, ip, name):
        self.server_ip = ip
        self.server_port = 12345
        self.name = name
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def connect(self):
        try:
            self.client_socket.connect((self.server_ip, self.server_port))
            self.connected = True
            print(f"[CLIENT] Đã kết nối đến server {self.server_ip}:{self.server_port}")
            self.client_socket.send(self.name.encode())
        except Exception as e:
            print(f"[LỖI] Không thể kết nối: {e}")
            self.connected = False

    def send_choice(self, choice):
        if not self.connected:
            print("[LỖI] Chưa kết nối đến server.")
            return None
        try:
            self.client_socket.send(choice.encode())
            data = self.client_socket.recv(1024).decode()
            return json.loads(data)
        except Exception as e:
            print(f"[LỖI] Khi gửi/nhận dữ liệu: {e}")
            return None

    def close(self):
        self.client_socket.close()


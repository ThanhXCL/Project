import socket
import threading
import random
from match_handler import MatchHandler

HOST = '0.0.0.0'
PORT = 12345

waiting_clients = []
lock = threading.Lock()

def log_result(name1, choice1, name2, choice2, result):
    with lock:
        print(f"{name1} ({choice1}) vs {name2} ({choice2}) => {result}")

def accept_clients():
    print(f"[SERVER] Listening on {HOST}:{PORT}")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[CONNECTED] {addr}")

        try:
            name = client_socket.recv(1024).decode().strip()
            print(f"[INFO] Người chơi tên: {name}")
            with lock:
                waiting_clients.append((client_socket, name))
                if len(waiting_clients) >= 2:
                    random.shuffle(waiting_clients)
                    (c1, name1) = waiting_clients.pop(0)
                    (c2, name2) = waiting_clients.pop(0)
                    handler = MatchHandler(c1, c2, name1, name2, callback=log_result)
                    threading.Thread(target=handler.handle, daemon=True).start()
        except Exception as e:
            print(f"[ERROR - Nhận tên người chơi] {e}")

if __name__ == '__main__':
    accept_clients()

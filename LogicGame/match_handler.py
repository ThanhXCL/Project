import json
from game_logic import determine_winner

class MatchHandler:
    def __init__(self, client1, client2, name1, name2, callback=None):
        self.client1 = client1
        self.client2 = client2
        self.name1 = name1
        self.name2 = name2
        self.callback = callback

    def handle(self):
        try:
            while True:
                choice1 = self.client1.recv(1024).decode().strip().lower()
                if not choice1:
                    break  # client1 đóng kết nối
                choice2 = self.client2.recv(1024).decode().strip().lower()
                if not choice2:
                    break  
                print(f"[DEBUG] {self.name1} chọn {choice1} - {self.name2} chọn {choice2}")

                result1 = determine_winner(choice1, choice2)
                result2 = determine_winner(choice2, choice1)

                # Gửi kết quả cho client1
                self.client1.send(json.dumps({
                    "your_name": self.name1,
                    "opponent_name": self.name2,
                    "your_choice": choice1,
                    "opponent_choice": choice2,
                    "result": result1
                }).encode())

                # Gửi kết quả cho client2
                self.client2.send(json.dumps({
                    "your_name": self.name2,
                    "opponent_name": self.name1,
                    "your_choice": choice2,
                    "opponent_choice": choice1,
                    "result": result2
                }).encode())

                print(f"[MATCH] {self.name1} ({choice1}) vs {self.name2} ({choice2}) => {result1.upper()} / {result2.upper()}")

                if self.callback:
                    self.callback(self.name1, choice1, self.name2, choice2, result1)

        except Exception as e:
            print("[ERROR - MatchHandler]", e)

        finally:
            print(f"[CLOSED] {self.name1} hoặc {self.name2} đã rời phòng.")
            self.client1.close()
            self.client2.close()

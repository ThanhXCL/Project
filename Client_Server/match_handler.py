import json

class MatchHandler:
    def __init__(self, client1, client2, name1, name2, callback=None):
        self.client1 = client1
        self.client2 = client2
        self.name1 = name1
        self.name2 = name2
        self.callback = callback

    def handle(self):
        try:
            choice1 = self.client1.recv(1024).decode()
            choice2 = self.client2.recv(1024).decode()

            from game_logic import determine_winner
            result = determine_winner(choice1, choice2)

            result1 = json.dumps({
                "your_name": self.name1,
                "opponent_name": self.name2,
                "your_choice": choice1,
                "opponent_choice": choice2,
                "result": result
            })

            result2 = json.dumps({
                "your_name": self.name2,
                "opponent_name": self.name1,
                "your_choice": choice2,
                "opponent_choice": choice1,
                "result": result
            })

            self.client1.send(result1.encode())
            self.client2.send(result2.encode())

            print(f"[MATCH] {self.name1} ({choice1}) vs {self.name2} ({choice2}) => {result}")

            if self.callback:
                self.callback(self.name1, choice1, self.name2, choice2, result)

        except Exception as e:
            print("[ERROR - MatchHandler]", e)
        finally:
            self.client1.close()
            self.client2.close()

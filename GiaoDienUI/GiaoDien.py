import tkinter as tk
from tkinter import ttk, messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")
        
        self.player_name = tk.StringVar()
        self.round_type = tk.StringVar(value="Bo3")
        self.player_score = 0
        self.opponent_score = 0
        self.rounds_played = 0

        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Enter your name:").pack()
        tk.Entry(self.root, textvariable=self.player_name).pack(pady=5)

        tk.Label(self.root, text="Choose match type:").pack()
        ttk.Combobox(self.root, textvariable=self.round_type, values=["Bo1", "Bo3", "Bo5"]).pack(pady=5)

        tk.Label(self.root, text="Choose your move:").pack(pady=10)
        for move in ["Rock", "Paper", "Scissors"]:
            tk.Button(self.root, text=move, width=20, command=lambda m=move: self.play_round(m)).pack(pady=2)
        
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
        
        self.score_label = tk.Label(self.root, text="Score: 0 - 0")
        self.score_label.pack()

    def play_round(self, player_move):
        opponent_move = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(player_move, opponent_move)

        self.rounds_played += 1
        if result == "player":
            self.player_score += 1
            message = f"You win! {player_move} beats {opponent_move}."
        elif result == "opponent":
            self.opponent_score += 1
            message = f"You lose! {opponent_move} beats {player_move}."
        else:
            message = f"It's a draw! You both chose {player_move}."

        self.result_label.config(text=message)
        self.score_label.config(text=f"Score: {self.player_score} - {self.opponent_score}")
        self.check_end_game()

    def determine_winner(self, move1, move2):
        if move1 == move2:
            return "draw"
        elif (move1 == "Rock" and move2 == "Scissors") or \
             (move1 == "Scissors" and move2 == "Paper") or \
             (move1 == "Paper" and move2 == "Rock"):
            return "player"
        else:
            return "opponent"

    def check_end_game(self):
        limit = {"Bo1": 1, "Bo3": 2, "Bo5": 3}[self.round_type.get()]
        if self.player_score == limit or self.opponent_score == limit:
            winner = self.player_name.get() if self.player_score > self.opponent_score else "Opponent"
            messagebox.showinfo("Game Over", f"{winner} wins the match!")
            self.reset_game()

    def reset_game(self):
        self.player_score = 0
        self.opponent_score = 0
        self.rounds_played = 0
        self.score_label.config(text="Score: 0 - 0")
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()

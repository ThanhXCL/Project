import tkinter as tk
from tkinter import ttk, messagebox
import random

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")

        self.player_name = ""
        self.game_mode = ""
        self.rounds_to_win = 1
        self.player_score = 0
        self.computer_score = 0
        self.round_count = 0

        self.setup_start_screen()

    def setup_start_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Enter your name:").pack(pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text="Choose match type:").pack(pady=5)
        self.mode_var = tk.StringVar()
        mode_dropdown = ttk.Combobox(self.root, textvariable=self.mode_var, state="readonly")
        mode_dropdown['values'] = ("Bo1", "Bo3", "Bo5")
        mode_dropdown.current(0)
        mode_dropdown.pack()

        tk.Button(self.root, text="Start Game", command=self.start_game).pack(pady=10)

    def start_game(self):
        self.player_name = self.name_entry.get().strip()
        if not self.player_name:
            messagebox.showwarning("Missing name", "Please enter your name.")
            return

        mode = self.mode_var.get()
        self.rounds_to_win = {"Bo1": 1, "Bo3": 2, "Bo5": 3}[mode]
        self.player_score = 0
        self.computer_score = 0
        self.round_count = 0

        self.setup_game_screen()

    def setup_game_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Player: {self.player_name}", font=("Arial", 12)).pack(pady=5)
        self.score_label = tk.Label(self.root, text=self.get_score_text(), font=("Arial", 12))
        self.score_label.pack(pady=5)

        tk.Label(self.root, text="Choose your move:", font=("Arial", 12)).pack(pady=5)

        for move in ["Rock", "Paper", "Scissors"]:
            tk.Button(self.root, text=move, command=lambda m=move: self.play_round(m), width=20).pack(pady=2)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

    def get_score_text(self):
        return f"{self.player_name}: {self.player_score} | Computer: {self.computer_score}"

    def play_round(self, player_move):
        comp_move = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(player_move, comp_move)

        if result == "Win":
            self.player_score += 1
            msg = f"You chose {player_move}, computer chose {comp_move}. You win!"
        elif result == "Lose":
            self.computer_score += 1
            msg = f"You chose {player_move}, computer chose {comp_move}. You lose!"
        else:
            msg = f"You both chose {player_move}. It's a draw!"

        self.round_count += 1
        self.score_label.config(text=self.get_score_text())
        self.result_label.config(text=msg)

        if self.player_score == self.rounds_to_win or self.computer_score == self.rounds_to_win:
            self.end_game()

    def determine_winner(self, player, computer):
        win_map = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
        if player == computer:
            return "Draw"
        elif win_map[player] == computer:
            return "Win"
        else:
            return "Lose"

    def end_game(self):
        winner = self.player_name if self.player_score > self.computer_score else "Computer"
        messagebox.showinfo("Game Over", f"{winner} wins the game!")
        self.setup_start_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()

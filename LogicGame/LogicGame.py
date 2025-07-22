def determine_winner(move1, move2):
    if move1 == move2:
        return "draw"
    elif (move1 == "rock" and move2 == "scissors") or \
         (move1 == "scissors" and move2 == "paper") or \
         (move1 == "paper" and move2 == "rock"):
        return "player1"
    else:
        return "player2"
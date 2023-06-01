import math
import random

def evaluate(state):
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]  
    ]

    for line in lines:
        a, b, c = line
        if state[a] == state[b] == state[c]:
            if state[a] == 'X':
                return 1  
            elif state[a] == 'O':
                return -1  

    if ' ' not in state:
        return 0  

    return None  

def print_board(state):
    print("---------")
    print("|", state[0], state[1], state[2], "|")
    print("|", state[3], state[4], state[5], "|")
    print("|", state[6], state[7], state[8], "|")
    print("---------")


def player_move(player):
    row = int(input(f"Player {player}'s turn. Enter the row (0-2): "))
    col = int(input("Enter the column (0-2): "))

    index = row * 3 + col
    if initial_state[index] == ' ':
        initial_state[index] = player
        print(f"Player {player}'s Move:")
        print_board(initial_state)
        return True
    else:
        print("Invalid move! Try again.")
        return False


def computer_move(player):
    print(f"Player {player}'s turn.")

    
    moves = []
    for i in range(9):
        if initial_state[i] == ' ':
            moves.append(i)

    
    if moves:
        index = random.choice(moves)
        initial_state[index] = player
        print(f"Player {player}'s Move:")
        print_board(initial_state)
    else:
        print("No valid moves left!")


initial_state = [" "] * 9  
print("Initial State:")
print_board(initial_state)


mode = input("Select game mode (1 for Player vs. Player, 2 for Player vs. Computer): ")
while mode != "1" and mode != "2":
    mode = input("Invalid input. Select game mode (1 for Player vs. Player, 2 for Player vs. Computer): ")

game_status = None
current_player = 'X'

while game_status is None:
    if mode == "1" or current_player == 'X':
        while not player_move(current_player):
            pass
    else:
        computer_move(current_player)

    game_status = evaluate(initial_state)

    if game_status is not None:
        break

    current_player = 'O' if current_player == 'X' else 'X'


if game_status == 1:
    print(f"Player X wins!")
elif game_status == -1:
    print(f"Player O wins!")
else:
    print("It's a draw!")

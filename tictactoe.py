import random
import time
import psutil
import uuid

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a win
def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

# Function to check for a tie
def check_tie(board):
    for row in board:
        if "-" in row:
            return False
    return True

# Function for the computer's move
def computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == "-":
            board[row][col] = "X"
            break

# Function for the user's move
def user_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        move = int(move) - 1
        row, col = divmod(move, 3)
        if board[row][col] == "-":
            board[row][col] = "O"
            break
        else:
            print("Invalid move. Try again.")

# Main function to play the game
def play_game():
    board = [["-" for _ in range(3)] for _ in range(3)]
    print_board(board)
    while True:
        computer_move(board)
        print("Computer's move:")
        print_board(board)
        if check_win(board, "X"):
            print("Computer wins!")
            break
        if check_tie(board):
            print("It's a tie!")
            break
        user_move(board)
        print("Your move:")
        print_board(board)
        if check_win(board, "O"):
            print("You win!")
            break
        if check_tie(board):
            print("It's a tie!")
            break

# Function to get the MAC address
def get_mac_address():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])
    return mac

# Function to get memory usage
def get_memory_usage():
    process = psutil.Process()
    mem_info = process.memory_info()
    return mem_info.rss

# Main function
if __name__ == "__main__":
    start_time = time.time()
    play_game()
    end_time = time.time()
    mac_address = get_mac_address()
    memory_used = get_memory_usage()
    time_taken = end_time - start_time

    print(f"MAC Address: {mac_address}")
    print(f"Memory Used: {memory_used / (1024 * 1024):.2f} MB")
    print(f"Time Taken: {time_taken:.2f} seconds")


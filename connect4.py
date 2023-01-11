# this program plays connect four. 
# this program was written by chatGPT, not me. 

board = [[' ' for _ in range(7)] for _ in range(6)]
player = 'X'  # Move the player variable definition here

def print_board():
    for row in board:
        print('|'.join(row))

def play():
    global player   # to inform the use of global player
    while True:
        print_board()
        col = int(input(f'{player}, select a column (0-6) to drop a token: '))
        if not (0 <= col < 7):
            print('Invalid column')
            continue
        if board[0][col] != ' ':
            print('Column is full')
            continue
        for i in range(6):
            if board[i][col] != ' ':
                board[i-1][col] = player
                break
        else:
            board[-1][col] = player
        if check_win():
            print(f'Player {player} wins!')
            return
        if check_draw():
            print('Draw')
            return
        player = 'O' if player == 'X' else 'X'

def check_win():
    for i in range(6):
        for j in range(7):
            if board[i][j] == ' ':
                continue
            if j <= 3 and board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3]:
                return True
            if i <= 2 and board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j]:
                return True
            if i <= 2 and j <= 3 and board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
                return True
            if i <= 2 and j >= 3 and board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3]:
                return True
    return False

def check_draw():
    for i in range(6):
        for j in range(7):
            if board[i][j] == ' ':
                return False
    return True

play()

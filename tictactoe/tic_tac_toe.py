import random


def create_game() -> dict:
    return {
        'board': [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ], # could be better board[1, 1]
        'turn': 'X',
        'counter': 0,
    }

def draw_board(game):
    print("  0 1 2")
    counter = 0
    for row in game['board']:
        print(counter, ' '.join(row))
        counter += 1
    print()

def input_location_h(game, x_or_o):
    while True:
        temp_x = int(input(f'Enter Row number for {x_or_o}: '))
        if not 0 <= temp_x <= 2:
            print(f"x not range")
            continue
        temp_y = int(input(f'Enter column number for {x_or_o}: '))
        if not 0 <= temp_y <= 2:
            print("y not range")
            continue
        if game["board"][temp_x][temp_y] == '_':
            return temp_x,temp_y
        print("taken")
def input_location_c(game, x_or_o):
    while True:
        temp_x = random.randint(0,2)
        temp_y = random.randint(0,2)
        if game["board"][temp_x][temp_y] == '_':
            return temp_x,temp_y

def check_win(game, x_o: str) -> bool:
    row = any([all([True if i == x_o else False for i in game["board"][j]]) for j in range(3)])
    column = any([all([True if game["board"][j][i] == x_o else False for i in range(3)]) for j in range(3)])
    diagonal1 = any([all([True if game["board"][i][i] == x_o else False for i in range(3)])])
    diagonal2 = any([all([True if game["board"][2-i][i] == x_o else False for i in range(2,-1,-1)])])

    return row or column or diagonal1 or diagonal2

def check_tie(game) -> bool:
    return game['counter'] >= 9

def make_human_turn(game: dict, turn:str) -> bool:
    draw_board(game)
    x, y = input_location_h(game, turn)
    game['board'][x][y] = turn
    game['counter'] += 1
    if check_win(game, turn):
        print(f"{turn} won the game")
        return True
    #   board is full (counter == 9), tie
    if check_tie(game):
        print("The game is tied")
        return True

def make_computer_turn(game: dict, turn:str) -> bool:
    x, y = input_location_c(game, turn)
    game['board'][x][y] = turn
    game['counter'] += 1
    if check_win(game, turn):
        print(f"{turn} won the game")
        return True
    #   board is full (counter == 9), tie
    if check_tie(game):
        print("The game is tied")
        return True
def is_computer_input() -> bool:
    while True:
        try:
            temp_input = int(input("Enter 1 to verse the computer or 0 for 2 players: "))
            if temp_input == 0 or temp_input == 1:
                return bool(temp_input)
        except ValueError:
            print("String entered, 0/1 only")
            continue
        print("0/1 only")
def play_x_o():
    # prepare_game
    my_game: dict = create_game()
    is_computer: bool = is_computer_input()
    is_computer_starting: bool = random.choice([True,False])
    if is_computer_starting and is_computer:
        print("Computer starts!")
    while True:
        if not is_computer:
            if make_human_turn(my_game,"X"):
                break
            if make_human_turn(my_game,"O"):
                break
        else:
            if is_computer_starting:
                if make_computer_turn(my_game,"X"):
                    break
                if make_human_turn(my_game, "O"):
                    break
            else:
                if make_human_turn(my_game, "X"):
                    break
                if make_computer_turn(my_game,"O"):
                    break

play_x_o()

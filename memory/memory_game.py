import random


def init_game() -> dict:
    game_data = {
        'board_size': 0,
        'board_list': [],
        'board_result': [],
        'incorrect_guesses': 0
    }
    return game_data


def is_game_over(game_data) -> bool:
    return all(game_data['board_result'])


def display_board(game_data):
    board_size: int = game_data['board_size']
    for i in range(board_size):
        print(f"{i * board_size:02}-{i * board_size + board_size:02} |", end=" ")
        for j in range(board_size):
            print(game_data['board_list'][i * board_size + j] if game_data['board_result'][i * board_size + j] else "_",
                  end=" ")
        print()


def display_board_guesses(game_data, guess_1: int, guess_2: int):
    board_size: int = game_data['board_size']

    for i in range(board_size):
        print(f"{i * board_size:02}-{i * board_size + board_size:02} |", end=" ")
        for j in range(board_size):
            if i * board_size + j == guess_1:
                print(game_data['board_list'][i * board_size + j], end=" ")
            elif i * board_size + j == guess_2:
                print(game_data['board_list'][i * board_size + j], end=" ")
            else:
                print(game_data['board_list'][i * board_size + j] if game_data['board_result'][
                    i * board_size + j] else "_", end=" ")
        print()


def handle_guess(game_data, guess_1: int, guess_2: int) -> bool:
    if game_data['board_list'][guess_1 - 1] == game_data['board_list'][guess_2 - 1]:
        game_data['board_result'][guess_1 - 1] = True
        game_data['board_result'][guess_2 - 1] = True
        return True
    game_data['incorrect_guesses'] += 1
    return False


def is_flipped(game_data, guess: int) -> bool:
    return game_data['board_result'][guess]


def validate_board_size() -> int:
    while True:
        try:
            board_size = int(input("Enter board size: "))
            if board_size % 2 == 0 and board_size > 0:
                return board_size
            print("Board size has to be positive and even.")
        except ValueError:
            print("Please enter a number.")


def start_game(game_data):
    board_size = validate_board_size()
    game_data['board_size'] = board_size
    numbers: list[int] = list(range(1, (board_size ** 2) // 2 + 1)) * 2
    random.shuffle(numbers)
    game_data['board_list'] = numbers
    game_data['board_result'] = list(False for _ in range(board_size ** 2))

    display_board(game_data)

    while not is_game_over(game_data):
        guess1 = 0
        guess2 = 0
        while True:
            try:
                guess1 = int(input("Guess1: "))
                if guess1 > board_size ** 2 or guess1 < 1:
                    print("Guess 1 not in range")
                    continue
                if is_flipped(game_data, guess1 - 1):
                    print("Guess 1 already flipped.")
                    continue
                guess2 = int(input("Guess2: "))
                if guess2 > board_size ** 2 or guess1 < 1:
                    print("Guess 2 not in range")
                    continue
                if is_flipped(game_data, guess2 - 1):
                    print("Guess 2 already flipped.")
                    continue
                if guess1 == guess2:
                    print("Enter Different guesses ")
                    continue
                break
            except ValueError:
                print("Please enter only numbers.")
                continue
        print()
        display_board_guesses(game_data, guess1 - 1, guess2 - 1)
        print("Correct!" if handle_guess(game_data, guess1, guess2) else "Incorrect, try again.")
    else:
        print(f"You won with {game_data['incorrect_guesses']} incorrect guesses!")

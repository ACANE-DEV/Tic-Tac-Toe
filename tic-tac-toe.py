import random

position = {'X': [], 'O': []}
mark = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]


def show_board():
    print(' {} | {} | {}'.format(mark[6], mark[7], mark[8]))
    print(' {} | {} | {}'.format(mark[3], mark[4], mark[5]))
    print(' {} | {} | {}'.format(mark[0], mark[1], mark[2]))


def check_win(status):
    win_sol = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [7, 8, 9], [4, 5, 6], [1, 2, 3], [1, 5, 9], [7, 5, 3]]
    for n in win_sol:
        if all(i in position[status] for i in n):
            return True
    return False


def check_draw():
    if len(position['X']) + len(position['O']) == 9:
        return True
    return False


def player_input():
    try:
        data = int(input('Choose your box : '))
        if data in position['X'] or data in position['O']:
            print('*** This box has already filled ***')
            show_board()
            return player_input()
        elif data < 1 or data > 9:
            print('*** Choose only 1 - 9 ***')
            show_board()
            return player_input()
        return data
    except ValueError:
        print('*** Wrong Input ***')
        show_board()
        return player_input()


def value_of_game(x):
    try:
        value = int(input('>>> ').strip())
        if value == 0:
            if x == 1:
                return game_one_player()
            else:
                return game_two_players()
        elif value == 1:
            return tic_tac_toe()
        else:
            print('****************************')
            print('Try again ? (Press 0)')
            print('Select Another Mode (Press 1)')
            return value_of_game(x)
    except ValueError:
        print('*** Wrong Input ***')
        return value_of_game(x)


def game_two_players():
    position['X'].clear()
    position['O'].clear()
    global mark
    mark = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
    player_status = 'X'
    while True:
        show_board()
        player_pos = player_input()
        mark[player_pos - 1] = player_status
        position[player_status].append(player_pos)

        if check_win(player_status):
            show_board()
            print('Mr.' + player_status, 'WIN!!!')
            print('----------------------------')
            print('Try again ? (Press 0)')
            print('Select Another Mode (Press 1)')
            value_of_game(2)

        if check_draw():
            show_board()
            print('Draw!')
            print('----------------------------')
            print('Try again ? (Press 0)')
            print('Select Another Mode (Press 1)')
            value_of_game(2)

        if player_status == 'X':
            player_status = 'O'
        elif player_status == 'O':
            player_status = 'X'


def game_one_player():
    position['X'].clear()
    position['O'].clear()
    global mark
    mark = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
    bot_choices = [num for num in range(1, 10)]
    player_value = bool()
    bot_value = ''
    bot_status = ''
    print('Do you wanna play first?')
    print('----------------------------')
    print('Press X to play first')
    print('Press O if not')
    player_status = input('>>> ').upper().strip()

    if player_status == 'X':
        player_value = True
        bot_value = False
        bot_status = 'O'
    elif player_status == 'O':
        player_value = False
        bot_value = True
        bot_status = 'X'
    else:
        game_one_player()

    while True:
        show_board()
        if player_value:
            player_pos = player_input()
            bot_choices.remove(player_pos)
            mark[player_pos - 1] = player_status
            position[player_status].append(player_pos)
            player_value = False
            bot_value = True
        elif bot_value:
            bot_pos = random.choice(bot_choices)
            bot_choices.remove(bot_pos)
            print('Stupid Bot choose box', bot_pos)
            mark[bot_pos - 1] = bot_status
            position[bot_status].append(bot_pos)
            player_value = True
            bot_value = False

        if check_win(player_status):
            show_board()
            print('Mr.' + player_status, 'WIN!!!')
            print('----------------------------')
            print('Play again ? (Press 0)')
            print('Select Another Mode (Press 1)')
            value_of_game(1)

        if check_win(bot_status):
            show_board()
            print('Mr.' + player_status, 'LOSE!!!')
            print('----------------------------')
            print('Try again ? (Press 0)')
            print('Select Another Mode (Press 1)')
            value_of_game(1)

        if check_draw():
            show_board()
            print('Draw!')
            print('----------------------------')
            print('Try again ? (Press 0)')
            print('Select Another Mode (Press 1)')
            value_of_game(1)


def tic_tac_toe():
    print('----------------------------')
    print('Press 1 for One-Player-Mode')
    print('Press 2 for Two-Players-Mode')
    try:
        mode = int(input('Select Mode : ').strip())
        if mode == 1:
            return game_one_player()
        elif mode == 2:
            return game_two_players()
        return tic_tac_toe()
    except ValueError:
        print('*** Wrong input ***')
        tic_tac_toe()


print('--- Welcome to my Tic-Tac-Toe ---')
print('Rule :')
print(' 7 | 8 | 9')
print(' 4 | 5 | 6')
print(' 1 | 2 | 3')
print('Press any number to choose box')
print('And try to get three in a row. EASY!!')

tic_tac_toe()
import random

WIN_CONDITION = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (2, 5, 8), (0, 4, 8),
                 (1, 4, 7), (2, 4, 6))
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
board = [str(i) for i in range(1, 10)]
mark = 'O'  # Стартовое значение


def switch_mark():  # Функция для передачи хода
    global mark  # Добавляем в пределы функции переменную mark, которая была
    # определена за пределами функции
    if mark == 'X':  # Передача хода
        mark = 'O'
    else:
        mark = 'X'


def enemy_mark():  # Бот
    global mark
    if mark == 'X':
        return 'O'
    else:
        return 'X'


def show_board(board: list):  # Рисуем доску (^x - форматирование)
    print(f'\n{board[0]:^3}║{board[1]:^3}║{board[2]:^3}')
    print('═══╬═══╬═══')
    print(f'{board[3]:^3}║{board[4]:^3}║{board[5]:^3}')
    print('═══╬═══╬═══')
    print(f'{board[6]:^3}║{board[7]:^3}║{board[8]:^3}')


def game():
    while any(list(map(lambda x: x.isdigit(), board))) and not check_win():
        # Просим цикл while пройтись по board и проверить, все ли элементы
        # нашего списка board - числа с помощью isdigit() и что игра не
        # закончена победой или ничьей
        switch_mark()  # Начало нашего хода
        show_board(board)  # Показывает нашу доску
        turn = play_turn() if mark == 'X' else bot_turn(board)  # Наш ход
        # будет когда mark == X, в противном случае бот делает свой ход
        board[turn] = mark
    show_board(board)
    if check_win():  # Если после хода условие победы было выполнено,
        # то победителю выводится сообщение
        print(f'\nПоздравляем, {mark}, вы победили.')
    else:
        print('\nНичья')


def bot_turn(board: list) -> int:
    if board[4].isdigit():  # Стандартный выбор бота это 4 элемент доски (5)
        return 4
    else:  # Если стандартный выбор не доступен (если цифра 5 была заменена
        # уже на X или О
        turn = pre_win(board, mark)
        enemy_turn = pre_win(board, enemy_mark())
        if turn:
            return turn
        elif enemy_turn:
            return enemy_turn
        else:
            while any(list(map(lambda x: board[x].isdigit(), [0, 2, 6, 8]))):
                turn = random.choice([0, 2, 6, 8])
                if board[turn].isdigit():
                    return turn
            while True:
                turn = random.randint(0, 8)
                if board[turn].isdigit():
                    return turn


def pre_win(board: list, cur_mark: str) -> int:
    for win in WIN_CONDITION:
        if (board[win[0]] == board[win[1]] == cur_mark) and \
                board[win[2]].isdigit():
            return win[2]
        elif (board[win[1]] == board[win[2]] == cur_mark) and \
                board[win[0]].isdigit():
            return win[0]
        else:
            (board[win[0]] == board[win[2]] == cur_mark) and \
            board[win[1]].isdigit()
            return win[1]
    return False


def check_win():  # Функция для проверки выигрыша в игре
    for win in WIN_CONDITION:  # Берёт по одному набору кортежей
        if board[win[0]] == board[win[1]] == board[win[2]]:
            return True
    return False


def play_turn() -> int:  # Проверка того, что пользователь вводит число
    while True:
        turn = input(f'\n{mark}, Ваш ход: ')
        if turn.isdigit() and 0 < int(turn) < 10 and \
                board[int(turn) - 1].isdigit():
            return int(turn) - 1  # - 1 нужен из-за того, что вводимое число
            # 1 будет указывать на цифру 2 в нашей игре, так как 0 индекс это 1
            # элемент

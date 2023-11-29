"""
Задача
Написать игру в “Крестики-нолики”. Можете использовать
любые парадигмы, которые посчитаете наиболее
подходящими. Можете реализовать доску как угодно - как
одномерный массив или двумерный массив (массив массивов).
Можете использовать как правила, так и хардкод, на своё
усмотрение. Главное, чтобы в игру можно было поиграть через
терминал с вашего компьютера.
"""

from colorama import Fore
import random


class GameMaster:
    def __init__(self):
        self.board: Board = Board()
        self.available_places: set = set(self.board.fields.copy())
        self.players: list[Player] = [Player('x'), Player('0')]

        self.players[0].next_p, self.players[1].next_p = \
            self.players[1], self.players[0]

        self.player_colors = {1: Fore.RED,
                              2: Fore.BLUE,
                              3: Fore.GREEN,
                              4: Fore.YELLOW}

        self.WIN_PATTERNS = ([1, 2, 3], [4, 5, 6], [7, 8, 9],
                             [1, 4, 7], [2, 5, 8], [3, 6, 9],
                             [1, 5, 9], [3, 5, 7])

    def _show_board(self):
        print(f'\n'
              f'═════════════\n'
              f'║{self.board.fields[0]:^3}'
              f'║{self.board.fields[1]:^3}'
              f'║{self.board.fields[2]:^3}║\n'
              f'════╬═══╬════\n'
              f'║{self.board.fields[3]:^3}'
              f'║{self.board.fields[4]:^3}'
              f'║{self.board.fields[5]:^3}║\n'
              f'════╬═══╬════\n'
              f'║{self.board.fields[6]:^3}'
              f'║{self.board.fields[7]:^3}'
              f'║{self.board.fields[8]:^3}║\n'
              f'═════════════'
              f'\n')

    def _player_turn(self, player):
        if not self.available_places:
            print('Ничья!')
            return
        try:
            self._show_board()
            if not player.is_bot:
                turn = int(input(
                    f'{player.name}, выберите одну из доступных клеток:\n'
                    f'{[i for i in self.available_places if 0 < i < 10]}\n'
                    f'-> '))
            else:
                turn = random.randint(1, 9)
            if turn in self.available_places:
                player.moves.append(turn)
                self.available_places.remove(turn)
                self.board.fields[turn - 1] = player.side
            else:
                print('Это поле уже занято! Ваш ход пропущен.')
            if not self._check_win(player):
                self._player_turn(player.next_p)
            else:
                print(f'{player.name} победил!')
        except ValueError:
            print(f'Нет такого значения, попробуйте ещё раз.')
            self._player_turn(player)

    def _check_win(self, player):
        player.moves.sort()
        return player.moves in self.WIN_PATTERNS

    def play(self):
        for player in self.players:
            if not player.is_bot:
                self._configure_player(player)
        self._player_turn(self.players[0])

    def _configure_player(self, player):
        player.name = input('Введите имя игрока -> ')
        self._choose_color(player)

    def _choose_color(self, player):
        try:
            new_color = int(input(
                f'Выберите цвет имени для {player.name}:\n'
                f'1. Красный\n'
                f'2. Синий\n'
                f'3. Зелёный\n'
                f'4. Жёлтый\n'
                f'-> '))
            if not 0 < new_color < 5:
                raise ValueError
            player.change_color(self.player_colors.get(new_color))
        except ValueError:
            print('Такого у нас нет!')
            self._choose_color(player)

    def _clear_board(self):
        self.board.clear()
        self.available_places = self.board.fields.copy()

    def start(self):
        while True:
            choice = input('Список опций:\n'
                           '1. Начать игру (PVP)\n'
                           '2. Начать игру (PVE)\n'
                           '3. Выйти\n'
                           'Выберите действие -> ')
            match choice:
                case '1':
                    self._clear_board()
                    self.play()
                case '2':
                    self._clear_board()
                    self.players[1].is_bot = True
                    self.play()
                case '3':
                    print('Пока!')
                    break
                case _:
                    print('Такой опции нет!')
                    self.start()


class Board:
    def __init__(self):
        self.fields = [_ for _ in range(1, 10)]

    def clear(self):
        self.fields = [_ for _ in range(1, 10)]


class Player:
    def __init__(self,
                 side: str,
                 next_p=None,
                 name: str = 'Игрок',
                 is_bot: bool = False):
        self.side: str = side
        self.name: str = name
        self.moves = []
        self.next_p = next_p
        self.is_bot = is_bot

    def change_color(self, color: str):
        self.name = color + self.name


if __name__ == '__main__':
    GameMaster().start()

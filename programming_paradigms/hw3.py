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


class GameMaster:
    def __init__(self):
        self.board = Board()
        self.available_places = self.board.fields.copy()
        self.players = (Player('x'), Player('0'))
        self.player_colors = {'1': Fore.RED,
                              '2': Fore.BLUE,
                              '3': Fore.GREEN,
                              '4': Fore.YELLOW}
        self.WIN_PATTERNS = (['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
                             ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
                             ['1', '5', '9'], ['3', '5', '7'])

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

    def _player1_turn(self, player):
        if self.available_places:
            self._show_board()
            turn = input(f'{player.name}, выберите одну из доступных клеток:\n'
                         f'{[i for i in self.available_places if 0 < i < 10]}\n'
                         f'-> ')
            if turn.isdigit() and 0 < int(turn) < 10:
                if int(turn) in self.available_places:
                    player.moves.append(turn)
                    self.available_places.remove(int(turn))
                    self.board.fields[int(turn) - 1] = player.side
                else:
                    print('Это поле уже занято! Ваш ход пропущен.')
                if not self._check_win(player):
                    self._player2_turn(self.players[1])
                else:
                    print(f'{player.name} победил!')
            else:
                print('Таких клеток на поле нет!')
                self._player1_turn(player)
        else:
            print('Ничья!')

    def _player2_turn(self, player):
        if self.available_places:
            self._show_board()
            turn = input(f'{player.name}, выберите одну из доступных клеток:\n'
                         f'{[i for i in self.available_places if 0 < i < 10]}\n'
                         f'-> ')
            if turn.isdigit() and 0 < int(turn) < 10:
                if int(turn) in self.available_places:
                    player.moves.append(turn)
                    self.available_places.remove(int(turn))
                    self.board.fields[int(turn) - 1] = player.side
                else:
                    print('Это поле уже занято! Ваш ход пропущен.')
                if not self._check_win(player):
                    self._player1_turn(self.players[0])
                else:
                    print(f'{player.name} победил!')
            else:
                print('Таких клеток на поле нет!')
                self._player2_turn(player)
        else:
            print('Ничья!')

    def _check_win(self, player):
        return sorted(player.moves) in self.WIN_PATTERNS

    def play(self):
        self._configure_players()
        self._player1_turn(self.players[0])

    def _configure_players(self):
        self.players[0].name = input('Введите имя Первого игрока -> ')
        self._choose_color(self.players[0])
        self.players[1].name = input('Введите имя Второго игрока -> ')
        self._choose_color(self.players[1])

    def _choose_color(self, player):
        new_color = input(f'Выберите цвет имени для {player.name}:\n'
                          f'1. Красный\n'
                          f'2. Синий\n'
                          f'3. Зелёный\n'
                          f'4. Жёлтый\n'
                          f'-> ')
        if new_color.isdigit() and 0 < int(new_color) < 5:
            player.change_color(self.player_colors.get(new_color))
        else:
            print('Такого у нас нет!')
            self._choose_color(player)

    def _clear_board(self):
        self.board.clear()
        self.available_places = self.board.fields.copy()

    def receive_human_input(self):
        while True:
            choice = input('Список опций:\n'
                           '1. Начать игру\n'
                           '2. Выйти\n'
                           'Выберите действие -> ')
            match choice:
                case '1':
                    self._clear_board()
                    self.play()
                case '2':
                    print('Пока!')
                    break
                case _:
                    print('Такой опции нет!')
                    self.receive_human_input()


class Board:
    def __init__(self):
        self.fields = [_ for _ in range(1, 10)]

    def clear(self):
        self.fields = [_ for _ in range(1, 10)]


class Player:
    def __init__(self, side: str,
                 name: str = 'Игрок'):
        self.side: str = side
        self.name: str = name
        self.moves = []

    def change_color(self, color: str):
        self.name = color + self.name


if __name__ == '__main__':
    GameMaster().receive_human_input()

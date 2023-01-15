# TODO здесь писать код

class Player:

    def __init__(self, name, position, figure):
        self.name = name
        self.position = position
        self.figure = figure


class Cell:

    def __init__(self, number):
        self.number = number
        self.free = True


class Board:
    positions = {'1. Левый верхний угол': [0, 0], '2. Середина сверху': [0, 2], '3. Правый верхний угол': [0, 4],
                 '4. Середина слева': [2, 0], '5. Центр': [2, 2], '6. Середина справа': [2, 4],
                 '7. Левый нижний угол': [4, 0], '8. Середина снизу': [4, 2], '9. Правый нижний угол': [4, 4]}
    board = [[' ', '|', ' ', '|', ' '],
             ['-', '-', '-', '-', '-'],
             [' ', '|', ' ', '|', ' '],
             ['-', '-', '-', '-', '-'],
             [' ', '|', ' ', '|', ' ']]

    def print_cells(self):
        print()
        for i in self.board:
            for j in i:
                print(j, end=' ')
            print('')

    def print_positions(self):
        for element in self.positions.keys():
            print(element)

    def print_figures_on_bord(self, player):
        row, element = '', ''
        if player.position == 1:
            row, element = self.positions['1. Левый верхний угол']
            self.positions.pop('1. Левый верхний угол')
        elif player.position == 2:
            row, element = self.positions['2. Середина сверху']
            self.positions.pop('2. Середина сверху')
        elif player.position == 3:
            row, element = self.positions['3. Правый верхний угол']
            self.positions.pop('3. Правый верхний угол')
        elif player.position == 4:
            row, element = self.positions['4. Середина слева']
            self.positions.pop('4. Середина слева')
        elif player.position == 5:
            row, element = self.positions['5. Центр']
            self.positions.pop('5. Центр')
        elif player.position == 6:
            row, element = self.positions['6. Середина справа']
            self.positions.pop('6. Середина справа')
        elif player.position == 7:
            row, element = self.positions['7. Левый нижний угол']
            self.positions.pop('7. Левый нижний угол')
        elif player.position == 8:
            row, element = self.positions['8. Середина снизу']
            self.positions.pop('8. Середина снизу')
        elif player.position == 9:
            row, element = self.positions['9. Правый нижний угол']
            self.positions.pop('9. Правый нижний угол')
        self.board[row][element] = player.figure

    def determine_the_winner(self):
        end = 'end'
        winner = 'winner'
        if self.board[0][0] == self.board[0][2] == self.board[0][4] and \
                (self.board[0][0] and self.board[0][2] and self.board[0][4] != ' '):
            return winner
        elif self.board[2][0] == self.board[2][2] == self.board[2][4] and \
                (self.board[2][0] and self.board[2][2] and self.board[2][4] != ' '):
            return winner
        elif self.board[4][0] == self.board[4][2] == self.board[4][4] and \
                (self.board[4][0] and self.board[4][2] and self.board[4][4] != ' '):
            return winner
        elif self.board[0][0] == self.board[2][0] == self.board[4][0] and \
                (self.board[0][0] and self.board[2][0] and self.board[4][0] != ' '):
            return winner
        elif self.board[0][2] == self.board[2][2] == self.board[4][2] and \
                (self.board[0][2] and self.board[2][2] and self.board[4][2] != ' '):
            return winner
        elif self.board[0][4] == self.board[2][4] == self.board[4][4] and \
                (self.board[0][4] and self.board[2][4] and self.board[4][4] != ' '):
            return winner
        elif self.board[0][0] == self.board[2][2] == self.board[4][4] and \
                (self.board[0][0] and self.board[2][2] and self.board[4][4] != ' '):
            return winner
        elif self.board[4][0] == self.board[2][2] == self.board[0][4] and \
                (self.board[4][0] and self.board[2][2] and self.board[0][4] != ' '):
            return winner
        elif (self.board[0][0] != ' ' and self.board[0][2] != ' ' and self.board[0][4] != ' ' and
              self.board[2][0] != ' ' and self.board[2][2] != ' ' and self.board[2][4] != ' ' and
              self.board[4][0] != ' ' and self.board[4][2] != ' ' and self.board[4][4] != ' '):
            return end
        return False


first_name = input('Введите имя 1-го игрока: ')
second_name = input('Введите имя 2-го игрока: ')
answer = int(input('{} должен выбрать какой фигурой будет играть 1 - X, 2 - O: '.format(first_name)))
if answer == 1:
    first_figure = 'X'
    second_figure = 'O'
    print('{} играет фигурой X, {} играет О'.format(first_name, second_name))
else:
    first_figure = 'O'
    second_figure = 'X'
    print('{} играет фигурой О, {} играет - Х'.format(first_name, second_name))
board = Board()
board.print_cells()
while True:
    print('\n{}, где рисуем {}?'.format(first_name, first_figure))
    board.print_positions()
    first_position = int(input('Введите соответствующую цифру: '))
    first_player = Player(first_name, first_position, first_figure)
    board.print_figures_on_bord(first_player)
    board.print_cells()
    if board.determine_the_winner() == 'end':
        print('\nНичья!')
        break
    if board.determine_the_winner() == 'winner':
        print('\nПобедил {}'.format(first_name))
        break
    print('\n{}, где рисуем {}?'.format(second_name, second_figure))
    board.print_positions()
    second_position = int(input('Введите соответствующую цифру: '))
    second_player = Player(second_name, second_position, second_figure)
    board.print_figures_on_bord(second_player)
    board.print_cells()
    if board.determine_the_winner() == 'winner':
        print('\nПобедил {}'.format(second_name))
        break




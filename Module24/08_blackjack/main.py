# TODO здесь писать код

import random


class Computer:
    cards = []
    score = 0

    def computer_score(self):
        return self.score


class Player:

    score = 0
    cards = []

    def __init__(self, user):
        self.name = user

    def player_cards_and_score(self):
        print('Ваши карты:', end=' ')
        for element in self.cards:
            print(element, end=', ')
        print('всего очков {}'.format(self.score))
        return self.score


class Card:

    def __init__(self, card_suit, card_rank):
        self.suit = card_suit
        self.rank = card_rank


class Desk:

    desk = {'Черви': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Король', 'Дама', 'Туз'],
            'Буби': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Король', 'Дама', 'Туз'],
            'Крести': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Король', 'Дама', 'Туз'],
            'Пики': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Король', 'Дама', 'Туз']}

    def choice_card_and_calculate_score(self, participant):
        Card.suit = random.choice(['Черви', 'Буби', 'Крести', 'Пики'])
        Card.rank = random.choice(self.desk[Card.suit])
        self.desk[Card.suit].remove(Card.rank)
        participant.cards.append(Card.rank + ' - ' + Card.suit)
        if Card.rank in ['Валет', 'Король', 'Дама']:
            participant.score += 10
        elif Card.rank == 'Туз':
            if participant.score > 21:
                participant.score += 1
            else:
                participant.score += 11
        else:
            participant.score += int(Card.rank)
        return Card.suit, Card.rank


name = input('Введите имя игрока: ')
player = Player(name)
computer = Computer()
desk = Desk()
for _ in range(2):
    suit, rank = desk.choice_card_and_calculate_score(player)
    card = Card(suit, rank)
for _ in range(2):
    suit, rank = desk.choice_card_and_calculate_score(computer)
    card = Card(suit, rank)
player_score = player.player_cards_and_score()
answer = int(input('1 - взять еще карту, 2 - остановиться: '))
while answer != 2:
    suit, rank = desk.choice_card_and_calculate_score(player)
    card = Card(suit, rank)
    player_score = player.player_cards_and_score()
    answer = int(input('1 - взять еще карту, 2 - остановиться: '))
computer_score = computer.computer_score()
while computer_score < 21:
    suit, rank = desk.choice_card_and_calculate_score(computer)
    card = Card(suit, rank)
    computer_score = computer.computer_score()
if (computer_score < player_score <= 21) or (player_score <= 21 < computer_score):
    print('Вы выиграли. У вас {} очков, у компьютера {} очков'.format(player_score, computer_score))
elif (player_score < computer_score <= 21) or (computer_score <= 21 < player_score):
    print('Вы проиграли. У вас {} очков, у компьютера {} очков'.format(player_score, computer_score))
elif computer_score == player_score:
    print('Ничья. У вас {} очков, у компьютера {} очков'.format(player_score, computer_score))
else:
    print('Обы игрока проиграли. У вас {} очков, у компьютера {} очков'.format(player_score, computer_score))



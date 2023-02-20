import random
# suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] * 3
# ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] * 3

# deck = []

# # Iterate over each suit and rank to create a full deck of cards
# for suit in suits:
#     for rank in ranks:
#         card = f"{rank} of {suit}"
#         deck.append(card)

# random.shuffle(deck)
# print(deck[0])


class Card():
    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks

class Blackjack():
    def __init__(self):
        self.deck = []

    def shuffle_deck(self):
        card = Card(['Hearts', 'Diamonds', 'Clubs', 'Spades'] * 3, ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] * 3)
        for suit in card.suits:
            for rank in card.ranks:
                deal = f'{rank} of {suit}'
                self.deck.append(deal)
        random.shuffle(self.deck)
        return self.deck

    def dealer(self, num_cards, num_players):
        hands = [[] for i in range(num_players)]
        for i in range(num_cards):
            for j in range(num_players):
                card = self.deck.pop(0)
                hands[j].append(card)
        self.hands = hands
        print(hands) 

    def bust_or_not(self):
        values = []
        for hand in self.hands:
            hand_value = 0
            for card in hand:
                rank = card.split()[0]
                if rank in ['King', 'Queen', 'Jack']:
                    card_value = 10
                elif rank == 'Ace':
                    card_value = 11
                else:
                    card_value = int(rank)
                hand_value += card_value
            values.append(hand_value)
        print(f'Value of your cards are {values}')

    def hit(self):
        card = self.deck.pop(0)
        self.hands.append(card)
        

game_on = Blackjack()
while True:
    start = input('Deal [1] or Cash-out [2]: ')
    if start == '1':
        game_on.shuffle_deck()
        game_on.dealer(2, 1)
        game_on.bust_or_not()
        hit = input('Would you like to Hit [1] or Stay [2]? ')
        if hit == '1':
            game_on.hit()
            
    elif start == '2':
        print('Thank you for playing! ')
        break
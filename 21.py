import random

class Deck:
    def __init__(self):
        self.cards = [(rank, suit) for rank in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player:
    RANK_VALUES = {
        'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10
    }

    def __init__(self):
        self.hand = []

    def hit(self, card):
        self.hand.append(card)

    def stand(self):
        pass

    def get_value(self):
        value = sum([self.RANK_VALUES[card[0]] for card in self.hand])
        if value > 21:
            for card in self.hand:
                if card[0] == 'Ace':
                    value -= 10
                    if value <= 21:
                        break
        return value

    def has_busted(self):
        return self.get_value() > 21

    def has_busted(self):
        return self.get_value() > 21

class Dealer:
    def __init__(self):
        self.hand = []

    def hit(self, card, hidden=False):
        if hidden:
            self.hand.append(('Hidden', 0))
        else:
            self.hand.append(card)

    def get_value(self):
        value = sum([self.card_value(card[0]) for card in self.hand])
        if value > 21:
            for card in self.hand:
                if card[0] == 'Ace' and self.card_value(card[0]) == 11:
                    value -= 10
                    if value <= 21:
                        break
        return value - self.card_value(self.hand[0][0]) if self.hand[0][0] == 'Hidden' else value

    def has_busted(self):
        return self.get_value() > 21

    def card_value(self, rank):
        if rank in ['King', 'Queen', 'Jack']:
            return 10
        elif rank == 'Ace':
            return 11
        else:
            return int(rank)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        self.deck.shuffle()
        self.player.hit(self.deck.deal())
        self.dealer.hit(self.deck.deal())
        self.player.hit(self.deck.deal())
        self.dealer.hit(self.deck.deal())
        # Show the player's hand and one of the dealer's cards
        print(f"Player's hand: {self.player.hand}")
        print(f"Dealer's hand: {self.dealer.hand[0]}, Hidden Card")
    
    def print_hand_values(self):
        print(f"Player's hand value: {self.player.get_value()}")
        print(f"Dealer's hand value: {self.dealer.get_value()}")

    def hit(self):
        self.player.hit(self.deck.deal())
        print(f"Player's hand: {self.player.hand}")
        self.print_hand_values()
        if self.player.has_busted():
            print("Player has busted")

    def stand(self):
        self.dealer.hit(self.deck.deal(), hidden=False)
        print(f"Dealer's hand: {self.dealer.hand}")
        self.print_hand_values()
        while self.dealer.get_value() < 17:
            self.dealer.hit(self.deck.deal())
            print(f"Dealer's hand: {self.dealer.hand}")
        if self.dealer.has_busted():
            print("Dealer has busted")
        else:
            if self.player.get_value() > self.dealer.get_value():
                print("Player wins")
            elif self.player.get_value() < self.dealer.get_value():
                print("Dealer wins")
            else:
                print("It's a tie")

game = Game()
game.start()

while True:
    choice = input("Do you want to hit or stand? ")
    if choice.lower() == "hit":
        game.hit()
        if game.player.has_busted():
            print("Dealer wins")
            break
    elif choice.lower() == "stand":
        game.stand()
        break

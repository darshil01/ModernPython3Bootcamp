from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for value in values for suit in suits]

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def _deal(self, num_cards):
        if self.count() > 0:
            to_remove = min(self.count(), num_cards)
            hand = self.cards[0:to_remove]
            del self.cards[0:to_remove]
            return hand
        else:
            raise ValueError("All cards have been dealt")

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self):
        return self._deal(5)

d = Deck()
print(d.count())
print(d.deal_card())
print(d.count())
print(d.deal_hand())
print(d.count())
print(d)
# pdb.set_trace()
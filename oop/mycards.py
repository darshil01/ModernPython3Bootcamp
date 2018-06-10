import random

class Card:

    def __init__(self, card_val, suit_val):
        self.card_val = card_val
        self.suit_val = suit_val

    def __repr__(self):
        return "{} of {}".format(self.card_val, self.suit_val)

class Deck:
    deck_count = 52
    card_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck_list = []

    def __init__(self):
        for suit in Deck.card_suits:
            for val in Deck.card_values:
                Deck.deck_list.append(Card(val, suit))
    
    def __repr__(self):
        return "Deck of {} cards".format(Deck.deck_count)

    def _deal(self, deal_numb):
        if Deck.deck_count - deal_numb >=0:
            Deck.deck_count -= deal_numb
            t = Deck.deck_list[0:deal_numb]
            del Deck.deck_list[0:deal_numb]
            return t
        else:
            raise ValueError("All cards have been dealt.")

    def shuffle(self):
        if Deck.deck_count == 52:
            random.shuffle(Deck.deck_list)
        else:
            raise ValueError("Only full decks can be shuffled")

    def deal_card(self, numb):
        t = self._deal(numb)
        return t[0]

    def deal_hand(self, numb):
        t = self._deal(numb)
        return t


my_deck = Deck()
print(my_deck)
my_deck.shuffle()
card = my_deck.deal_card(1)
print(card)
hand = my_deck.deal_hand(5)
print(hand)
print(my_deck)

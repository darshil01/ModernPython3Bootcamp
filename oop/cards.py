from random import shuffle

class Card:

    def __init__(self, card_val, suit_val):
        self.value = card_val
        self.suit = suit_val

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    def __init__(self):
        card_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(val, suit) for suit in card_suits for val in card_values]
    
    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def count(self):
        return len(self.cards)

    def _deal(self, deal_numb):
        count = self.count()
        actual = min([count,deal_numb])
        if count == 0:
            raise ValueError("All cards have been dealt.")
        cards = self.cards[:-actual]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return(self._deal(1)[0])

    def deal_hand(self, hand_size):
        return(self._deal(hand_size))

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self


# my_deck = Deck()
# print(my_deck)
# my_deck.shuffle()
# card = my_deck.deal_card(1)
# print(card)
# hand = my_deck.deal_hand(5)
# print(hand)
# print(my_deck)

d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(5)
card2 = d.deal_card()
print(card2)
print(d.cards)
card2 = d.deal_card()
import random
class Deck(object):
    SUIT = ['SPADE', 'CLUBS', 'HEARTS', 'DIAMONDS']
    FACE = ['ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']

    def __init__(self):
        self.no_of_cards = 52
        self.card = []
        self.deck = self.card   
    
    def card(self):
        for suit in self.SUIT:
            for face in self.FACE:
                self.card.append((suit, face)) 
                    
    def shuffle(self):
        return self.deck[random.randint(1,52)]


deck = Deck()
print deck.SUIT
print deck.shuffle

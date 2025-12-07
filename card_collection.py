import collections # importing the collections package

Card = collections.namedtuple('Card', ['rank', 'suit']) #creating a named tuple object named card.

class FrenchDeck: #creating a french deck class
    ranks = [str(n) for n in range(2,11)] + list('JQKA') # List comprehension for card ranks.
    suits = 'spades diamonds clubs hearts'.split() # split method for suits.

    def __init__(self): # Init method, List comprehension for suits and ranks.
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self): # Dunder len for length of cards.
        return len(self.cards)

    def __getitem__(self, position): # returning the card position in dunder position.
        return self.cards[position]

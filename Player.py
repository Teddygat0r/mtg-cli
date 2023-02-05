import random
class Player:

    def __init__(self, deck):
        self.library = deck # deck is probably an array of cards
        random.shuffle(self.library)
        self.life = 20
        self.counters = {}
        self.hand = []
        self.graveyard = []
        self.exile = []
        self.battlefield = []

    def drawCards(self, x: int):
        for i in range(x):
            self.draw()
    def draw(self):
        print('death')
            
    
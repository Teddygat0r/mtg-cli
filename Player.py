import random
import copy

class Player:
    def __init__(self, deck, name):
        self.library = deck # deck is probably an array of cards
        random.shuffle(self.library) # self.library[0] = top card of library
        self.life = 20
        self.name = name
        self.counters = {}
        self.hand = []
        self.graveyard = []
        self.exile = []
        self.battlefield = []
        self.mana_pool = {}
        self.drew_from_empty = False

    def drawCards(self, x: int):
        for i in range(x):
            self.draw()
    def draw(self):
        if len(self.library) == 0:
            self.drew_from_empty = True
        else:
            self.hand.append(copy.deepcopy(self.library[0]))
            self.hand[-1].zone = "hand"
            del self.library[0]
            
    def loseGame(self):
        print(f'death {self.name}')
            
    
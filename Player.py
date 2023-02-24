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
        self.max_hand_size = 7 # idk how to handle reliquary tower
        self.drew_from_empty = False

    def drawCards(self, x: int):
        for i in range(x):
            self.draw()
            
    def draw(self):
        if len(self.library) == 0:
            self.drew_from_empty = True
        else:
            self.hand.append(self.library.pop(0))
            self.hand[-1].zone = "Hand"
            
    def loseGame(self):
        print(f'death {self.name}')

    def shuffleLibrary(self):
        #trigger cosi's trickster here
        random.shuffle(self.library)
        
    def counterCount(self, counterType):
        if counterType in self.counters:
            return self.counters[counterType]
        else:
            return 0
            

    #def moveZone(self, obj, d)
            
    
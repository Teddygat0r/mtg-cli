import random
import copy

class Player:
    def __init__(self, deck, name):
        self.library = deck # deck is probably an array of cards
        random.shuffle(self.library) # self.library[0] = top card of library
        self.life = 20
        self.game = None # Will be a reference to the game object containing the players
        self.name = name
        self.counters = {}
        self.hand = []
        self.graveyard = []
        self.exile = []
        self.battlefield = []
        self.mana_pool = {}
        self.max_hand_size = 7 # idk how to handle reliquary tower
        self.lands_played = 0
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
    #TODO: implement this
    #will take in a dictionary(manaCost) and prompt the player to use mana from their mana pool to satisfy requirements, will return True if cost was successfully paid and False otherwise
    def payMana(manaCost):
        initialManaPool = self.mana_pool.copy()
        remainingCost = manaCost.copy()
        while remainingCost != {}:
            print("Mana to pay:")
            printManaPool(remainingCost)
            print("\nYour current mana pool:")
            printManaPool(self.mana_pool)
            print("Enter two characters, representing the mana you will pay from your mana pool and the mana pip you will fill with that mana.")
            a = input().split()
            #do input here idk i lost all of my motivation
        else:
            return True
            
        self.mana_pool
        return False
    
    #Returns True or False based on whether the mana variable(a char) could be used to pay for manaPip(a string)
    #TODO: work
    def manaCanFit(mana, manaPip):
        return True
        
    #Prints a mana pool.
    def printManaPool(pool):
        for i in pool:
            print(pool[i] + " " + i + " mana")
    #def moveZone(self, obj, d)
            
    
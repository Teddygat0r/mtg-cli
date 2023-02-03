class Player:
    hand = []
    graveyard = []
    exile = []
    deck = []
    battlefield = []
    lands = []

    def __init__(self, deck):
        self.deck = deck

    def drawCards(self, x: int):
        for i in range(x):
            self.draw()
    def draw(self):
        if(len(self.deck) == 0):
            return Player.die()
        
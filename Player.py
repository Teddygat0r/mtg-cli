class Player:
    life = 20
    counters = {} # poison is in standard
    hand = []
    graveyard = []
    exile = []
    deck = []
    battlefield = [] # having a lands array is redundant because it doesn't help with mana tapping
    #lands = []

    def __init__(self, deck):
        self.deck = deck

    def drawCards(self, x: int):
        for i in range(x):
            self.draw()
    def draw(self):
    """
    This should not be in player class because players losing the game from drawing is a state-based action, it doesn't happen instantaneously
        if(len(self.deck) == 0):
            return Player.lose()
            """
            
    
from Card import Card
import Player

class Goblin(Card):
    
    def __init__(self, currentzone: str, ownerplayer: Player):
        super().__init__("Goblin", {"R": 1}, "Creature", currentzone, ownerplayer, 1, 1)

    
    

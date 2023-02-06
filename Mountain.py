from Card import Card
from Player import Player

class Mountain(Card):
    
    def __init__(self, currentzone: str, ownerplayer: Player):
        super().__init__("Mountain", None, ["Land"], ["Mountain"], currentzone, ownerplayer)

    def manaTap(self):
        self.runPreventionAndReplacementEffects(self.manaTap)

        if not self.tapped:
            self.tapped = True
            if 'R' not in self.controller.mana_pool:
                self.controller.mana_pool['R'] = 1
            else:
                self.controller.mana_pool['R'] += 1
    

import Player

class Card:  
    
    
    """
    types of mana: 
    WUBRG, generic, snow, colorless, X(WUBRG, generic, S, C, X)
    10 hybrid 5 twobrid (W/U, 2/W)
    5 regular phyrexian, 10 hybrid phyrexian(R/P, R/G/P)
    using https://media.wizards.com/2023/downloads/MagicCompRules%2020230203.pdf 107.4(page 15) to determine mana order
    """
    
    def __init__(self, name: str, cost: dict[str, int], types: list[str], currentzone: str, ownerplayer: Player, power: int=0, toughness: int=0):
        self.name = name
        self.mana_cost = cost
        self.typeline = types
        self.zone = currentzone
        self.controller = ownerplayer
        self.owner = ownerplayer

        self.counters: dict[str, int] = {}
        self.abilities = []

        self.misc_effects: object = {} # for cleave, kicker, serra paragon, soulbond, etc
        self.attached: list[Card] = [] # for stuff attached to this card

        self.is_copy: bool = False # to help with SBA 704.5e https://media.wizards.com/2023/downloads/MagicCompRules%2020230203.pdf
        self.tapped: bool = False
        self.transformed: bool = False
        self.facedown: bool = False
        self.etb_this_turn: bool = False # needed for cards like Mirrex
        self.flipped: bool = False # this isn't relevant to standard

        self.power = power
        self.toughness = toughness

    def __str__(self):
        return self.name
    
    def getPower(self):
        return self.power + self.counters['+1/+1'] - self.counters['-1/-1']
    
    def getToughness(self):
        return self.toughness + self.counters['+1/+1'] - self.counters['-1/-1']
    

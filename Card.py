import Player

class Card:
    name: str = "Uninitalized Card"
    mana_cost: dict[str, int] = {}
    
    typeline: list[str] = []
    
    is_copy: bool = False # to help with SBA 704.5e https://media.wizards.com/2023/downloads/MagicCompRules%2020230203.pdf
    tapped: bool = False
    transformed: bool = False
    facedown: bool = False
    etb_this_turn: bool = False # needed for cards like Mirrex
    
    counters: dict[str, int] = {}
    zone: str = "Library" # this could probably just be a string
    controller: Player = None # will be set to a player object
    owner: Player = None
    
    abilities = []
    misc_effects: object = {} # for cleave, kicker, serra paragon, soulbond, etc
    attached: list[Card] = [] # for stuff attached to this card
    """
    types of mana: 
    WUBRG, generic, snow, colorless, X(WUBRG, generic, S, C, X)
    10 hybrid 5 twobrid (W/U, 2/W)
    5 regular phyrexian, 10 hybrid phyrexian(R/P, R/G/P)
    using https://media.wizards.com/2023/downloads/MagicCompRules%2020230203.pdf 107.4(page 15) to determine mana order
    """
    
    flipped: bool = False # this isn't relevant to standard
    
    
    def __init__(self, name: str, cost: dict[str, int], types: list[str], currentzone: str, ownerplayer: Player):
        self.name = name
        self.mana_cost = cost
        self.typeline = types
        self.zone = currentzone
        self.controller = ownerplayer
        self.owner = ownerplayer

    def __str__(self):
        return self.name
    

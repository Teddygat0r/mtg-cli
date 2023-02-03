class Card:
    name = "Uninitalized Card"
    mana_cost = {}
    
    typeline = []
    
    tapped = False
    transformed = False
    facedown = False
    etb_this_turn = False # needed for cards like Mirrex
    
    counters = {}
    zone = "Library" # this could probably just be a string
    controller = None # will be set to a player object
    owner = None
    
    abilities = []
    misc_effects = {} # for cleave, kicker, serra paragon, soulbond, etc
    """
    types of mana: 
    WUBRG, generic, snow, colorless, X(WUBRG, generic, S, C, X)
    10 hybrid 5 twobrid (W/U, 2/W)
    5 regular phyrexian, 10 hybrid phyrexian(R/P, R/G/P)
    using https://media.wizards.com/2023/downloads/MagicCompRules%2020230203.pdf 107.4(page 15) to determine mana order
    """
    
    flipped = False # this isn't relevant to standard
    
    
    def __init__(self, name, cost, types, currentzone, ownerplayer):
        self.name = name
        self.mana_cost = cost
        self.typeline = types
        self.zone = currentzone
        self.controller = ownerplayer
        owner = ownerplayer
    def __str__(self):
        return self.name
    

"""
Parts of a card:
Name - done xd
Mana Cost
Typeline(supertypes and subtypes)
Text Box
P/T if creature
Counters
Tapped/Untapped
Transformed/untransformed(daybound/nightbound, disturb, sagas, etc)
Face up/Face down(like 3 cards in standard care about this)
What zone it's in(for effects like cult conscript)

Not relevant in standard:
Flipped/Unflipped(only for OG kamigawa)
"""
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
    
    misc_effects = {} # for cleave, kicker, serra paragon, soulbond, etc
    """
    types of mana: 
    WUBRG, generic, snow, colorless, X(WUBRG, generic, S, C, X)
    10 hybrid 5 twobrid (W/U, 2/W)
    5 regular phyrexian, 10 hybrid phyrexian(R/P, R/G/P)
    using https://media.wizards.com/2023/downloads/MagicCompRules%2020230203.pdf 107.4(page 15) to determine mana order
    """
    
    flipped = False # this isn't relevant to standard
    
    
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    

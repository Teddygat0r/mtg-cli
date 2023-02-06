import Player


class Card:  

    """
    types of mana: 
    WUBRG, generic, snow, colorless, X(WUBRG, generic, S, C, X)
    10 hybrid 5 twobrid (W/U, 2/W)
    5 regular phyrexian, 10 hybrid phyrexian(R/P, R/G/P)
    using https://media.wizards.com/2023/downloads/MagicCompRules%2020230203.pdf 107.4(page 15) to determine mana order
    """
    
    """
    Constructor requires:
    Name(str)
    Cost(dict)
    Supertypes(array of strings)
    Subtypes(array of strings)
    Current zone(string)
    Owner(Player)
    Power(int)
    Toughness(int)
    """
    def __init__(self, name: str, cost: dict[str, int], supertypeline: list[str], subtypeline: list[str],currentzone: str, ownerplayer: Player, power: int=0, toughness: int=0):
        self.name = name
        self.mana_cost = cost
        self.supertypes = supertypeline
        self.subtypes = subtypeline
        self.zone = currentzone # zones will be Hand, Library, Graveyard, Exile, Command
        self.controller = ownerplayer
        self.owner = ownerplayer
        
        self.counters: dict[str, int] = {}
        self.abilities = []

        self.misc_effects: object = {} # for cleave, kicker, serra paragon, soulbond, etc
        self.attachedCards: list[Card] = [] # for stuff attached to this card
        self.attachedTo: Card = None # for something this card is attached to

        self.is_copy: bool = False # to help with SBA 704.5e https://media.wizards.com/2023/downloads/MagicCompRules%2020230203.pdf
        self.tapped: bool = False
        self.transformed: bool = False
        self.facedown: bool = False
        self.etb_this_turn: bool = False # needed for cards like Mirrex
        self.flipped: bool = False # this isn't relevant to standard
        self.damage: int = 0
        self.deathtouched: bool = False # whether this card was dealt damage by a source with deathtouch, to help with SBA 704.5h
        
        self.power = power
        self.toughness = toughness

        self.prevention: dict[str, list[function]] = {}
        self.replacement: dict[str, list[function]] = {}

    def __str__(self) -> str:
        currentlabel = self.name + " | "
        
        for counter in self.counters:
            if self.counters[counter] == 1:
                currentlabel += str(self.counters[counter]) + " " + counter + " counter, "
            else:
                currentlabel += str(self.counters[counter]) + " " + counter + " counters, "
        if len(self.counters) > 0:
            currentlabel = currentlabel[:-2] # to remove last comma and space
            currentlabel += " | "
            
        for effect in self.misc_effects:
            currentlabel += str(effect) + ", "
        if len(self.misc_effects) > 0:
            currentlabel = currentlabel[:-2] # to remove last comma and space
            
        if self.etb_this_turn:
            currentlabel += " | entered this turn"
        return currentlabel
    
    def getPower(self) -> int:
        currentPower = self.power
        if "+1/+1" in self.counters:
            currentPower += self.counters["+1/+1"]
        currentpower = self.power
        if "-1/-1" in self.counters:
            currentPower -= self.counters["-1/-1"]
        #TODO: apply modifiers from self.misc_effects(this is presumably where combat tricks go)
        return currentPower
    
    def getToughness(self) -> int:
        currentToughness = self.toughness
        if "+1/+1" in self.counters:
            currentToughness += self.counters["+1/+1"]
        currentToughness = self.power
        if "-1/-1" in self.counters:
            currentToughness -= self.counters["-1/-1"]
        #TODO: apply modifiers from self.misc_effects(this is presumably where combat tricks go)
        return currentToughness
    
    # Returns True if the creature was destroyed.
    def destroy(self) -> bool:
        #Trigger replacement effects
        if not self.runPreventionAndReplacementEffects(self.destroy):
            self.death()
            return True
        return False
        
    # Returns True if the creature actually died.  
    def death(self) -> bool:
        if not self.runPreventionAndReplacementEffects(self.death):
            self.zone = "Graveyard"
            #trigger "when this dies/when this is put in a graveyard from the battlefield"
            return True
        return False
    
    #Returns a boolean, whether the function's name is within a dictionary
    def getTriggerInDict(self, fcn, dictionary: dict) -> bool:
        return fcn.__name__ in dictionary
    
    #Runs all replacement effects within this card. Returns True if replacement or prevention effects exist within the card.
    def runPreventionAndReplacementEffects(self, fcn) -> bool:
        if(self.getTriggerInDict(fcn, self.prevention)):
            return True
        if(self.getTriggerInDict(fcn, self.replacement)):
            for x in self.replacement[fcn.__name__]:
                x()
            return True
        else:
            return False

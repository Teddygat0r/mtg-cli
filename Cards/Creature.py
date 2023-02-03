import Card

class Creature(Card):
    power = 0
    toughness = 0
    def __init__(self, name, cost, types, currentzone, ownerplayer, power, toughness):
        super(name, cost, types, currentzone, ownerplayer)
        self.power = power
        self.toughness = toughness

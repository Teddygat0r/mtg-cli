import Card
import Player

class Creature(Card):
    power = 0
    toughness = 0
    def __init__(self, name: str, cost: dict[str, int], types: list[str], currentzone: str, ownerplayer: Player, power: int, toughness: int):
        super(name, cost, types, currentzone, ownerplayer)
        self.power = power
        self.toughness = toughness

    def getPower(self) -> int:
        return power

    def getToughness(self) -> int:
        return toughness

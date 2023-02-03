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
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    

from Player import Player
from Card import Card
import random
import utils
import copy

class Game:

    
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.stack = []
        self.turnOrder = []
        self.turnNumber = 0
        self.gameEnded = False
        self.currentPhase = "Untap" # Untap, Upkeep, Draw, Main1, BeginCombat, 
        #DeclareAttacks, DeclareBlocks, CombatDamage, EndCombat, Main2, End, Cleanup
        
        
    #Moves a Card from one zone to another. Creates a new object, deletes the old one
    def moveZone(self, origin: list, result: list, oIn: int = 0, rIn: int = -1) -> bool:
        result.insert(type(origin[oIn]), rIn)


    #Rolls two dice. Tie handling is in pregame().
    def roll(self):
        p1roll, p2roll = random.randint(1, 6), random.randint(1, 6)
        print("Player 1 rolled a ", p1roll)
        print("Player 2 rolled a ", p2roll)
        return p1roll, p2roll
        
    def pregame(self):
        #Choose who gets first turn here maybe. I'm lazy and think we should randomly select outside the game object.
        #what if we just did it here so the game class is a full game
        
        p1roll, p2roll = self.roll()
        while p1roll == p2roll:
            p1roll, p2roll = self.roll()
        if p1roll > p2roll:
            #ask p1 whether to play or draw
            uIn = input('Player 1 wins the roll. Will they (P)lay or (D)raw?')
            if uIn.lower()[0] == 'p':
                self.turnOrder = [player1, player2]
            else:
                self.turnOrder = [player2, player1]
            pass
        else:
            #ask p2 whether to play or draw
            uIn = input('Player 2 wins the roll. Will they (P)lay or (D)raw?')
            if uIn.lower()[0] == 'p':
                self.turnOrder = [player2, player1]
            else:
                self.turnOrder = [player1, player2]
            pass
        #do whatever it is that determines whos turn it is first
        self.turnorder = []
        #Player 1 Mulligan
        for player in [self.player1, self.player2]:
            mull = True
            x = 7

            while mull and x > 0:
                self.player1.shuffleLibrary()
                self.player2.shuffleLibrary()
                player.drawCards(x)
                print(utils.formatList(player.hand))

                uIn = input('Will you keep this hand: (Y/N)')
                if(uIn.lower()[0] == 'Y'):
                    mull = False
                else:
                    for temp in range(x):
                        player.library.append(player.hand.pop(0))
                        player.library[-1].zone = "library"
                    x -= 1

    def runGame(self):
        while !self.gameEnded:
            self.turnNumber += 1
            print("Turn ", self.turnNumber)
            for player in self.turnOrder:
                turn(player)
                if self.gameEnded:
                    break
        
    def turn(self, activePlayerIndex):
        """
        run one turn of the game here, which consists of:
        Untap(do automatically because nobody gets priority)
        Upkeep
        Draw
        Main 1
        Beginning of Combat
        Declare Attackers
        Declare Blockers
        Combat Damage
        End of Combat
        Main 2
        End Step
        Cleanup Step
        Break immediately if somebody loses the game to SBAs and make self.gameEnded = True
        """
        activePlayer = self.turnOrder[activePlayerIndex]
        nonActivePlayer = self.turnOrder[1 - activePlayerIndex]
        #untap step, no one gets priority 
        self.currentPhase = "Untap"
        for card in self.turnOrder[activePlayerIndex].battlefield:
            card.untap()
            #TODO: handle unwinding clock-like effects here
        
        self.currentPhase = "Upkeep"
        #TODO: handle "at the beginning of your upkeep" stuff here
        phase(activePlayer, nonActivePlayer)
        
        self.currentPhase = "Draw"
        activePlayer.draw()
        phase(activePlayer, nonActivePlayer)
        
        self.currentPhase = "Main1"
        phase(activePlayer, nonActivePlayer)
        
        self.currentPhase = "BeginCombat"
        phase(activePlayer, nonActivePlayer)
        
        self.currentPhase = "DeclareAttacks"
        
        self.currentPhase = "DeclareBlocks"
        
        self.currentPhase = "CombatDamage"
        
        self.currentPhase = "EndCombat"
        
        self.currentPhase = "Main2"
        
        self.currentPhase = "End"
        
        self.currentPhase = "Cleanup"
        
    #Gives both players priority until both players pass and the stack is empty
    def phase(self, activePlayer, nonActivePlayer):
        print("\n----" + self.currentPhase + "----\n")
        phaseOver = False:
        while not phaseOver:
            if givePriority(activePlayer):
                continue
            else if givePriority(nonActivePlayer):
                continue
            else if len(self.stack) != 0:
                self.stack[-1].resolve(self)
                del self.stack[-1]
            else:
                phaseOver = False
    
    
    #Gets a list of every possible action the player could take and then prompts the player what to do.
    #Returns True if an action was taken and False if priority was passed.
    def givePriority(self, player) -> bool:
        stateBasedActions()
        return False
        
    
    def stateBasedActions(self):
        SBAperformed = False
        
        for player in [self.player1, self.player2]:
            player1lost = False
            player2lost = False
            
            #TODO: rework this so that theres a distinction between losing the game to damage, drawing from empty, or 10 poison
            if self.player1.life <= 0:
                #SBA 704.5a
                player1lost = True
            if self.player1.drew_from_empty:
                #SBA 704.5b
                player1lost = True
            if self.player2.life <= 0:
                #SBA 704.5a
                player2lost = True
            if self.player2.drew_from_empty:
                #SBA 704.5b
                player2lost = True
            
            #handle losing the game here?
            
            #TODO: make the zone arrays in the player classes also reflect a card being moved zones due to SBAs
            for zone in [player.hand, player.library, player.graveyard, player.exile]:
                for currentCard in zone:
                    if "Token" in currentCard.typeline or currentCard.is_copy:
                        #SBA 704.5d and 704.5e
                        #delete the card or something
                        zone.remove(currentCard)
                        SBAperformed = True
                        
            for currentCard in player.battlefield:
                if "Creature" in currentCard.typeline:
                    if currentCard.getToughness <= 0:
                        #SBA 704.5f
                        if currentCard.dies():
                            SBAperformed = True
                    elif currentCard.damage >= currentCard.getToughness or currentCard.deathtouched:
                        #SBA 704.5g and 704.5h
                        if currentCard.destroy():
                            SBAperformed = True
                
                
                if "Planeswalker" in currentCard.typeline:
                    if "Loyalty" not in currentCard.counters:
                        #SBA 704.5i, this assumes all values of 0 are removed from the counters dictionary
                        currentCard.dies()
                        SBAperformed = True
                if "+1/+1" in currentCard.counters and "-1/-1" in currentCard.counters:
                    #SBA 704.5q
                    if currentCard.counters["+1/+1"] > currentCard.counters["-1/-1"]:
                        currentCard.counters["+1/+1"] -= currentCard.counters["-1/-1"]
                        del currentCard.counters["-1/-1"]
                        SBAperformed = True
                    elif currentCard.counters["+1/+1"] < currentCard.counters["-1/-1"]:
                        currentCard.counters["-1/-1"] -= currentCard.counters["+1/+1"]
                        del currentCard.counters["+1/+1"]
                        SBAperformed = True
                    else:
                        del currentCard.counters["+1/+1"]
                        del currentCard.counters["-1/-1"]
                        SBAperformed = True
                

            
        if SBAperformed:
            self.stateBasedActions()
    
        """
        704.5. The state-based actions are as follows:
704.5a If a player has 0 or less life, that player loses the game.
704.5b If a player attempted to draw a card from a library with no cards in it since the last time
state-based actions were checked, that player loses the game.
704.5c If a player has ten or more poison counters, that player loses the game. Ignore this rule in
Two-Headed Giant games; see rule 704.6b instead.
704.5d If a token is in a zone other than the battlefield, it ceases to exist.
704.5e If a copy of a spell is in a zone other than the stack, it ceases to exist. If a copy of a card is in
any zone other than the stack or the battlefield, it ceases to exist.
704.5f If a creature has toughness 0 or less, it’s put into its owner’s graveyard. Regeneration can’t
replace this event.
704.5g If a creature has toughness greater than 0, it has damage marked on it, and the total damage
marked on it is greater than or equal to its toughness, that creature has been dealt lethal damage
and is destroyed. Regeneration can replace this event.
704.5h If a creature has toughness greater than 0, and it’s been dealt damage by a source with
deathtouch since the last time state-based actions were checked, that creature is destroyed.
Regeneration can replace this event.
704.5i If a planeswalker has loyalty 0, it’s put into its owner’s graveyard.
704.5j If two or more legendary permanents with the same name are controlled by the same player,
that player chooses one of them, and the rest are put into their owners’ graveyards. This is called
the “legend rule.”
704.5k If two or more permanents have the supertype world, all except the one that has had the
world supertype for the shortest amount of time are put into their owners’ graveyards. In the
event of a tie for the shortest amount of time, all are put into their owners’ graveyards. This is
called the “world rule.”
704.5m If an Aura is attached to an illegal object or player, or is not attached to an object or player,
that Aura is put into its owner’s graveyard.
704.5n If an Equipment or Fortification is attached to an illegal permanent or to a player, it becomes
unattached from that permanent or player. It remains on the battlefield.
704.5p If a creature is attached to an object or player, it becomes unattached and remains on the
battlefield. Similarly, if a permanent that’s neither an Aura, an Equipment, nor a Fortification is
attached to an object or player, it becomes unattached and remains on the battlefield.
704.5q If a permanent has both a +1/+1 counter and a -1/-1 counter on it, N +1/+1 and N -1/-1
counters are removed from it, where N is the smaller of the number of +1/+1 and -1/-1 counters
on it.
704.5r If a permanent with an ability that says it can’t have more than N counters of a certain kind
on it has more than N counters of that kind on it, all but N of those counters are removed from
it.
704.5s If the number of lore counters on a Saga permanent is greater than or equal to its final
chapter number and it isn’t the source of a chapter ability that has triggered but not yet left the
stack, that Saga’s controller sacrifices it. See rule 715, “Saga Cards.”
704.5t If a player’s venture marker is on the bottommost room of a dungeon card, and that dungeon
card isn’t the source of a room ability that has triggered but not yet left the stack, the dungeon
card’s owner removes it from the game. See rule 309, “Dungeons.”
704.5u If a permanent with space sculptor and any creatures without a sector designation are on the
battlefield, each player who controls one or more of those creatures and doesn’t control a
permanent with space sculptor chooses a sector designation for each of those creatures they
control. Then, each other player who controls one or more of those creatures chooses a sector
designation for each of those creatures they control. See 702.158, “Space Sculptor.”

Implemented:


"""
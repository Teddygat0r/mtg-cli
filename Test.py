from Player import Player
from Mountain import Mountain
from Goblin import Goblin
from Game import Game
import utils


myPlayer1 = Player([], 'player 1')
myPlayer2 = Player([], 'player 2')

myPlayer1.library = [Mountain('Library', myPlayer1)] * 24 + [Goblin('Library', myPlayer1)] * 36
myPlayer2.library = [Mountain('Library', myPlayer1)] * 24 + [Goblin('Library', myPlayer1)] * 36

game = Game(myPlayer1, myPlayer2)
game.pregame()

print('\n\n\n P1 Hand')
print(utils.formatList(game.player1.hand))
print(len(game.player1.library))



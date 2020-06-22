from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from src.game.game         import Game
from src.chess.chess_board import ChessBoard
from src.player.ai         import Ai
from src.player.human      import Human

class App:
    def start(self):
        Game(ChessBoard(), Human('black'), Ai('white')).start()

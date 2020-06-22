from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from abc import ABCMeta, abstractmethod
from src.chess.chess_move import ChessMove

class Player(metaclass=ABCMeta):
    def __init__(self, color):
        self.__color = color
    
    def color(self):
        return self.__color

    def is_white(self):
        return self.__color == 'white'

    @abstractmethod
    def next_chess_move(self) -> ChessMove:
        pass
        
from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from abc import ABCMeta, abstractmethod


class ChessPiece(metaclass=ABCMeta):
    def __init__(self, piece_type, color, number, y, x):
        self.__piece_type = piece_type
        self.__color = color
        self.__number = number
        self.__x = x
        self.__y = y

    def get_id(self):
        return self.__color + "_" + self.__piece_type + "_" + self.__number

    def color(self):
        return self.__color

    def get_type(self):
        return self.__piece_type

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def can_move(self):
        ##TODO: should be implemented
        return

    
    def move(self):
        ##TODO: should be implemented
        return
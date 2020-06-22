from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

class ChessMove:
    def __init__(self, chess_piece, destination_y, destination_x):
        self.__chess_piece = chess_piece
        self.__destination_x = destination_x
        self.__destination_y = destination_x
    
    def chess_piece(self):
        return self.__chess_piece
    
    def destination(self):
        return {
            'x': self.__destination_x,
            'y': self.__destination_y
        }
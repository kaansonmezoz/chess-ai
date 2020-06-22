from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from .player import Player
from src.chess.chess_move import ChessMove

class Ai(Player):
    def __init__(self, color):
        super().__init__(color)
    
    def next_chess_move(self, chess_board, game_screen) -> ChessMove:
        # TODO: bir sonraki hamleye ne kadar surede karar verdi ve ortalama suresi ne bunlari console'a bastiralim
        chess_piece = self.__select_chess_piece(chess_board, game_screen)
        return ChessMove(chess_piece, None, None)
    
    # debug amacli
    def __select_chess_piece(self, chess_board, game_screen):        
        invalid_selection = True
        x,y = None, None

        while invalid_selection:
            x,y = game_screen.click()
            
            chess_piece = chess_board.chess_piece(y, x)
            
            if chess_piece != 0 and self.__has_chess_piece(chess_piece):
                invalid_selection = False

        return chess_piece
    
    def __has_chess_piece(self, chess_piece):
        print("Player color: " + self.color())
        print("Chess piece color: " + chess_piece.color())
        return chess_piece.color() == self.color()


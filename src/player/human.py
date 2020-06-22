from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from .player import Player
from src.chess.chess_move import ChessMove

class Human(Player):
    def __init__(self, color):
        super().__init__(color)

    def next_chess_move(self, chess_board, game_screen) -> ChessMove:
        valid_move = False

        while not valid_move:
            chess_piece = self.__select_chess_piece(chess_board, game_screen)
            y, x = self.__select_destination(chess_board, game_screen) 
            chess_move = ChessMove(chess_piece, y, x)
            valid_move = chess_board.is_valid_move(chess_move)
            print('Move is valid: ' + str(valid_move))
        
        return chess_move
    
    def __select_chess_piece(self, chess_board, game_screen):        
        # burada soyle bir durum da var. secilen tas sah durumunu engelleyebilecek tas olmali ya da
        # destination belirlenirken onu o durumu kontrol etmemiz gerekiyor
        # tasin engelleyip engelleyemeyecegini bilmek için şahı engelleyebilen butun hamleleri bilmek lazim ki o tas kullanilabilir mi bilelim.
        # o yuzden sanki destination secildikten sonra sah durumu ortadan kalkıyor mu ona bir bakmak lazim

        # buradaki logici tekrar kurgulamak lazim

        invalid_selection = True
        x,y = None, None

        while invalid_selection:
            x,y = game_screen.click()            
            chess_piece = chess_board.chess_piece(y, x)
            
            if chess_piece != 0 and self.__has_chess_piece(chess_piece):
                invalid_selection = False

        game_screen.render_selected_chess_piece(chess_piece)
        return chess_piece
    
    def __has_chess_piece(self, chess_piece):
        print("Player color: " + self.color())
        print("Chess piece color: " + chess_piece.color())
        return chess_piece.color() == self.color()

    def __select_destination(self, chess_board, game_screen):
        invalid_selection = True

        while invalid_selection:
            x, y = game_screen.click()
            chess_piece = chess_board.chess_piece(y, x)

            if (chess_piece == 0) or (not self.__has_chess_piece(chess_piece)):
                invalid_selection = False
        
        print('Destination height: ' + str(y))
        print('Destination width: ' + str(x))
        return y, x
    
    def __display_possible_moves(self, chess_piece):
        ## will be implemented later
        return
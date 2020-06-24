from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from .player import Player
from src.chess.chess_move import ChessMove

class Ai(Player):
    def __init__(self):
        super().__init__('black')
        ## puanlar evaluation kisminda kullanilacak
        ## puanlama ai acisindan baz alinarak yani ai'in rengi siyah oldugu zaman baz alinarak yapiliyor.        
        ## ai kendisini lehine olacak sekilde board'u maximize edecek
        ## human icinse board'u minimize etmeye calisacak
        ## yani kendisi icin en kotu olabilecek hamleyi yapmis olacak human
        self.__points = {}
        self.__points['P'] = -100
        self.__points['N'] = -320
        self.__points['B'] = -330
        self.__points['R'] = -500
        self.__points['Q'] = -900
        self.__points['K'] = -20000        
        # bu da beyazlar şah yaparsa olan puan
        self.__points['white_check'] = -10000

        self.__points['p'] = 100
        self.__points['n'] = 320
        self.__points['b'] = 330
        self.__points['r'] = 500
        self.__points['q'] = 900
        self.__points['k'] = 20000        
        self.__points['black_check'] = 10000
    

    def next_chess_move(self, chess_board, game_screen) -> ChessMove:

        # TODO: bir sonraki hamleye ne kadar surede karar verdi ve ortalama suresi ne bunlari console'a bastiralim
        chess_piece = self.__select_chess_piece(chess_board, game_screen)
        return ChessMove(chess_piece, None, None)

    #def __create_possible_moves_tree(self, chess_board, game_screen):


    def __create_node(self, chess_move, ):
        node = {}
        node['children'] = []
        node['board_fen'] = '.....' ## board_fen'i kullanmak yeterli olabilir bunun icin
        node['value'] = 0
        node['chess_move'] ## bu node'a gelmek icin yapilan chess_move günün sonunda bu bizim icin onemli olacak

        ##

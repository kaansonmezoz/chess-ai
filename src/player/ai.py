from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from .player import Player
from src.chess.chess_move import ChessMove

import chess

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

        ## AI'ın kac hamle sonrasına bakarak karar verecegi
        self.__max_depth = 4
    

    def next_chess_move(self, chess_board, game_screen) -> ChessMove:
        board = chess.Board(chess_board.string_representation())
        #self.__create_possible_moves_tree(board)
        self.y(board)

        # TODO: bir sonraki hamleye ne kadar surede karar verdi ve ortalama suresi ne bunlari console'a bastiralim
        chess_piece = self.__select_chess_piece(chess_board, game_screen)
        return ChessMove(chess_piece, None, None)

    def y(self, chess_board: chess.Board):
        print('Ai started thinking !')
        print('Finding all possible moves within next ' + str(self.__max_depth) + ' moves')
        root = self.__create_node(None, chess_board.board_fen(), 'white', 0)
        self.__x(root, chess_board, 1)

        node = root
        i = 0
        while i < self.__max_depth:
            print('Move Count: ' + str(node['depth']))
            print('Player color:' + node['player_color'])
            print('Chess Move:' + str(node['chess_move']))
            print('Board Fen:' + node['board_fen'])
            print('Value: ' + str(node['value']))
            print('--------------------------------------')
            node = node['children'][0]
            i = i+1

        print('Move Count: ' + str(node['depth']))
        print('Player color:' + node['player_color'])
        print('Chess Move:' + str(node['chess_move']))
        print('Board Fen:' + node['board_fen'])
        print('Value: ' + str(node['value']))
        print('--------------------------------------')


    def __generate_chess_moves_tree(self, parent_node, chess_board: chess.Board, depth):
        player_color = 'black' if parent_node['player_color'] == 'white' else 'white'
        
        if chess_board.legal_moves.count == 0:
            ## parent'ın yapabilecegi hamle yok demek
            ## parent final node demek, o yüzden bu node icin gidip value hesaplanacak
            board_fen = parent_node['board_fen']
            value = self.__evaluate_chess_board(board_fen, chess_board.is_check(), parent_node['player_color'])
            parent_node['value'] = value


        if depth == self.__max_depth: ## buna benzer bir islemi eger herhangi bir legal moves yoksa da yapmak lazim ...
            for possible_move in list(chess_board.legal_moves):
                chess_board.push(possible_move)
                board_fen = chess_board.board_fen()                
                child = self.__create_node(possible_move, board_fen, player_color, depth)
                parent_node['children'].append(child)
                # her bir child icin value hesapla
                value = self.__evaluate_chess_board(board_fen, chess_board.is_check(), player_color)
                child['value'] = value
                chess_board.pop()

            ## parent_node icin value hesaplamak lazim
            ## burada bir islem yapacagiz
            ## value hesaplamasi yapabilir burada
            return    
    
        for possible_move in list(chess_board.legal_moves):
            chess_board.push(possible_move)
            board_fen = chess_board.board_fen()            
            child = self.__create_node(possible_move, board_fen, player_color, depth)
            parent_node['children'].append(child)
            self.__x(child, chess_board, depth + 1)
            chess_board.pop()
            #chess_board.set_board_fen(parent_node['board_fen']) alternative

    def __create_node(self, chess_move, board_fen, player_color, depth):
        node = {}
        node['children'] = []
        node['board_fen'] = board_fen
        node['value'] = 0 # bu en son hesaplanacak aslında ... bunun degeri degisebilir tam emin degilisim suanda 
        
        ## bu node'a gelmek icin yapilan chess_move, bu hamle yapılmıs ve sıra diger oyuncuya gecmis board_fen halini almis
        node['chess_move'] = chess_move 
        ## buna göre bu node minimize mı etmeye calisacak maximize mi etmeye calisacak ona karar verecegiz
        node['player_color'] = player_color
        # bu gerekli mi cok emin olamadim
        node['depth'] = depth

        return node

    def __evaluate_chess_board(self, board_fen, is_check, player_color):
        value = 0
        
        if is_check: ## şah var mı diye bakilir
            if player_color == 'white': ## hamle sirasi beyazda demek, o zaman şah yapan siyah demek value siyaha avantaj yaratacak sekilde artmali
                value += self.__points['black_check']
            else:
                value += self.__points['white_check'] 
        
        for i in range(len(board_fen)):
            char = board_fen[i]
            
            if char in self.__points:
                value += self.__points[char]
        
        return value
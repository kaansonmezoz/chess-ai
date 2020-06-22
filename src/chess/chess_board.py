from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from src.chess.chess_piece import ChessPiece
from src.chess.chess_move  import ChessMove
import chess

class ChessBoard:
    def __init__(self):
        # buradaki kucuk harfli olan rakamlar siyah anlamina geliyor
        self.__board_engine = chess.Board()
        self.__board = [[0] * 8 for _ in range(8)]
        self.__white_pieces = []
        self.__black_pieces = []
        self.__fill_board(self.__white_pieces, self.__black_pieces)
        self.__matrix_to_chess_mapper = self.__matrix_location_to_chess_board_mapper()

    def __fill_board(self, white_pieces, black_pieces):
        self.__put_black_chess_pieces(black_pieces)
        self.__put_white_chess_pieces(white_pieces)
    
    def __put_white_chess_pieces(self, white_pieces):
        self.__put_chess_pieces(white_pieces, 'white', 7, 6)

    def __put_black_chess_pieces(self, black_pieces):
        self.__put_chess_pieces(black_pieces, 'black', 0, 1)

    def __put_chess_pieces(self, pieces, color, y1, y2):
        self.__board[y1][0] = self.__create_chess_piece(pieces, ChessPiece, 'rook', color,'1', y1, 0)
        self.__board[y1][1] = self.__create_chess_piece(pieces, ChessPiece, 'knight', color, '1', y1, 1)
        self.__board[y1][2] = self.__create_chess_piece(pieces, ChessPiece, 'bishop', color, '1', y1, 2)
        self.__board[y1][3] = self.__create_chess_piece(pieces, ChessPiece, 'queen', color, '1', y1, 3)
        self.__board[y1][4] = self.__create_chess_piece(pieces, ChessPiece, 'king', color, '1' ,y1, 4)
        self.__board[y1][5] = self.__create_chess_piece(pieces, ChessPiece, 'bishop', color, '2', y1, 5)
        self.__board[y1][6] = self.__create_chess_piece(pieces, ChessPiece, 'knight', color, '2', y1, 6)
        self.__board[y1][7] = self.__create_chess_piece(pieces, ChessPiece, 'rook', color, '2', y1, 7)

        for x in range(8):
            self.__board[y2][x] = self.__create_chess_piece(pieces, ChessPiece, 'pawn', color, str(x+1), y2, x)

    def __create_chess_piece(self, pieces, creator, piece_type, color, number, y, x):
        piece = creator(piece_type, color, number, y, x)
        pieces.append(piece)
        return piece

    def __matrix_location_to_chess_board_mapper(self):
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        mapper = {0: {}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{} ,7:{}}

        for i in range(8):
            for j in range(8):
                mapper[i][j] = chars[j] + str(8-i)
        
        return mapper
 
    def white_pieces(self):
        return self.__white_pieces
    
    def black_pieces(self):
        return self.__black_pieces
    
    def chess_piece(self, y, x):
        return self.__board[y][x]

    def move_chess_piece(self, chess_move: ChessMove):      
        # buraya gelindiginde yapilan bir move'un valid oldugunu dusunuyoruz
        chess_notation = self.__create_chess_notation(chess_move)

        move = chess.Move.from_uci(chess_notation)
        self.__board_engine.push(move)

        self.__update_chess_board(chess_move)

        # TODO: Şah varsa ona göre bir tavir almak lazim.
        # TODO: Rok dediğimiz hareket nasil yapilacak ona bir bakmak lazim

        # TODO: Oyunculara belki de bir state koymak gerekebilir iste suan sana sah yapildi mi gibisiden cunku hamlen de ona gore bir karar vermen gerekiyor
        # TODO: Ai da buna gore karar verecek belki de puanlamasi vs degisecek o yuzden o sekilde bir hamle yapmak gerekiyor.

        # TODO: sah durumu vs varsa board farklı bir sekilde renderlanmali sanki
        # TODO: piyon en sona geldiği zaman kural olarak baska bir tasa evrilebiliyordu onu da eklemek gerek

        return

    def __create_chess_notation(self, chess_move):
        chess_piece = chess_move.chess_piece()
        destination = chess_move.destination()

        y_target = destination['y']
        x_target = destination['x']

        x = chess_piece.x()
        y = chess_piece.y()        

        return self.__matrix_to_chess_mapper[y][x] + self.__matrix_to_chess_mapper[y_target][x_target]

    def __update_chess_board(self, chess_move):
        chess_piece = chess_move.chess_piece()
        source_y, source_x = chess_piece.y(), chess_piece.x()

        destination = chess_move.destination()
        target_y, target_x = destination['y'], destination['x']

        self.__board[source_y][source_x] = 0        
        target_piece = self.__board[target_y][target_x]

        if target_piece != 0:
            self.__eat_opponents_chess_piece(target_piece)
        
        self.__board[target_y][target_x] = chess_piece
        chess_piece.set_position(target_y, target_x)

    def __eat_opponents_chess_piece(self, target_piece):
            print('Chess piece: ' + target_piece.get_id() + ' has been eaten.')
            
            if target_piece.color() == 'white':
                self.__white_pieces.remove(target_piece)
            else:
                self.__black_pieces.remove(target_piece)            
    
    def game_finished(self):
        # stalemate = pat anlamına geliyor 
        return self.__board_engine.is_checkmate() or self.__board_engine.is_stalemate()
    
    def is_valid_move(self, chess_move: ChessMove):
        chess_piece = chess_move.chess_piece()
        y, x = chess_piece.y(), chess_piece.x()
                
        source = self.__matrix_to_chess_mapper[y][x]
        
        destination = chess_move.destination()
        y, x = destination['y'], destination['x']        
        
        destination = self.__matrix_to_chess_mapper[y][x]

        if destination == source:
            return False

        move = chess.Move.from_uci(source + destination)

        print("Chess move: " + source + destination)

        return move in self.__board_engine.legal_moves
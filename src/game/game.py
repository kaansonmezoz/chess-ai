from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from src.game.game_screen import GameScreen
from src.player.player import Player

class Game:
    def __init__(self, chess_board, player_1: Player, player_2: Player):
        self.__validate_player_arg(player_1, 'player_1')
        self.__validate_player_arg(player_2, 'player_2')
        
        self.__game_screen = GameScreen()
        self.__chess_board = chess_board
        self.__game_screen.update(self.__chess_board.white_pieces(), self.__chess_board.black_pieces())
        self.__player_order = []
        
        if player_1.is_white():
            self.__player_order.append(player_1)
            self.__player_order.append(player_2)
        else:
            self.__player_order.append(player_2)
            self.__player_order.append(player_1)

    def start(self):        
        game_not_finished = True
        
        while game_not_finished: 
            ## buradaki logicler aslinda oyunculara yuklenmeli ai'da surec boyle islemeyecek mesela chess_board ve GameScreen verilmesi gerekecek gibi duruyor
            player = self.__player_order.pop(0)
            chess_move = player.next_chess_move(self.__chess_board, self.__game_screen)
            print('Chess piece: ' + chess_move.chess_piece().get_id())
            self.__move_chess_piece(chess_move)
            game_not_finished = self.__chess_board.game_not_finished()
            self.__player_order.append(player)

    def __validate_player_arg(self, obj, arg_name):
        if not isinstance(obj, Player):
            raise TypeError(arg_name + ' should be an instance of Player !')

    def __move_chess_piece(self, chess_move):
        self.__chess_board.move_chess_piece(chess_move)
        white_pieces = self.__chess_board.white_pieces()
        black_pieces = self.__chess_board.black_pieces()
        self.__game_screen.update(white_pieces, black_pieces)


# burada oyun icin gerekli diger dependecyler her sey yaratilmali
# suan her class kendi dependencysisini yaratiyor onu kaldırmak lazim

from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

import os

# buradaki mediayı farklı bir sekilde saklamak gerekli aslinda
# yani bu class sadece okumayı saglasin ve isi bitsin olmali
# asil game_board vs gibi bir seyde olmali sanki bu image'lar
# hatta iki tip image olsun. GameImages, MenuImages gibi
class GameImages:
    def __init__(self, pygame):
        self.__pygame = pygame
        self.__board = pygame.image.load(os.path.join(os.path.dirname(__file__), '../../assets/board.png')).convert()
        self.__square_width, self.__square_height = self.__get_board_square_size()
        self.__pieces = {'white': {}, 'black': {}}
        self.__load_images(pygame)

    def __get_board_square_size(self):
        size = self.board_size()
        return size[0]/8, size[1]/8

    def __load_images(self, pygame):
        self.__load_chess_move_images(pygame, self.__square_width, self.__square_height)
        self.__load_menu_images(pygame, self.__square_width, self.__square_height)
        self.__load_chess_piece_images(pygame, self.__square_width, self.__square_height)

    def __load_chess_piece_images(self, pygame, width, height):
        bishop = self.__load_image('../../assets/white_bishop.png', width, height)
        king = self.__load_image('../../assets/white_king.png', width, height)
        knight = self.__load_image('../../assets/white_knight.png', width, height)
        pawn = self.__load_image('../../assets/white_pawn.png', width, height)
        queen = self.__load_image('../../assets/white_queen.png', width, height)
        rook = self.__load_image('../../assets/white_rook.png', width, height)
        
        self.__pieces['white']['bishop'] = bishop
        self.__pieces['white']['king'] = king
        self.__pieces['white']['knight'] = knight
        self.__pieces['white']['pawn'] = pawn
        self.__pieces['white']['queen'] = queen
        self.__pieces['white']['rook'] = rook

        bishop = self.__load_image('../../assets/black_bishop.png', width, height)
        king = self.__load_image('../../assets/black_king.png', width, height)
        knight = self.__load_image('../../assets/black_knight.png', width, height)
        pawn = self.__load_image('../../assets/black_pawn.png', width, height)
        queen = self.__load_image('../../assets/black_queen.png', width, height)
        rook = self.__load_image('../../assets/black_rook.png', width, height)

        self.__pieces['black']['bishop'] = bishop
        self.__pieces['black']['king'] = king
        self.__pieces['black']['knight'] = knight
        self.__pieces['black']['pawn'] = pawn
        self.__pieces['black']['queen'] = queen
        self.__pieces['black']['rook'] = rook
        

    def __load_chess_move_images(self, pygame, width, height):                        
        self.__green_circle = self.__load_image('../../assets/Chess_Pieces_Sprite.png', width, height)
        self.__red_circle = self.__load_image('../../assets/red_circle_big.png', width, height)        
        self.__green_box = self.__load_image('../../assets/green_box.png', width, height)        
        self.__yellow_circle = self.__load_image('../../assets/yellow_circle_big.png', width, height)    
        self.__green_big_circle = self.__load_image('../../assets/green_circle_big.png', width, height)
        self.__chess_piece_selection = self.__load_image('../../assets/green_circle_neg.png', width, height)
        self.__yellow_box = self.__load_image('../../assets/yellow_box.png', width, height)

    def __load_menu_images(self, pygame, width, height):
        self.__friend = self.__load_image('../../assets/withfriend.png', width, height)
        self.__ai = self.__load_image('../../assets/withAI.png', width, height)
        self.__play_white = self.__load_image('../../assets/playWhite.png', width, height)    
        self.__play_black = self.__load_image('../../assets/playBlack.png', width, height)
        self.__flip_enabled = self.__load_image('../../assets/flipEnabled.png', width, height)
        self.__flip_disabled = self.__load_image('../../assets/flipDisabled.png', width, height)

    def __load_image(self, path, width, height):
        base_path = os.path.join(os.path.dirname(__file__))
        path = os.path.join(base_path, path)
        image = self.__pygame.image.load(path).convert_alpha()
        return self.__scale_image(image, width, height)

    def __scale_image(self, image, width, height):
        return self.__pygame.transform.scale(image, (int(width), int(height)))
    
    def board(self):
        return self.__board

    def board_size(self):
        return self.__board.get_rect().size
    
    def piece_image(self, color, name):
        # color = white | black
        # name = bishop | king | knight | pawn | queen | rock
        # bunları da piece'in üzerinden aliriz hem color, type, number seklinde olursa eger fieldlari ve get_id dedigimizde 
        # bunları concat ederek getirirsek sıkıntı olmaz
        return self.__pieces[color][name]    

    def chess_piece_selection(self):
        return self.__chess_piece_selection
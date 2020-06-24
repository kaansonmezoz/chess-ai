from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from src.game.game_images import GameImages

import pygame
from pygame.locals import *

import sys

class GameScreen:
    def __init__(self):
        self.__pygame = pygame
        self.__pygame.init()
        self.__screen = pygame.display.set_mode((600,600))
        self.__game_images = GameImages(pygame)        
        self.__init_screen()
        # butun degisiklikleri vs renderlamak icin bunu yapmak lazim yani update'i cagirtmak lazim        
        pygame.display.update() 
    
    def __init_screen(self):        
        size = self.__game_images.board_size()
        self.__pygame.display.set_caption('Checkmate')
        screen = self.__pygame.display.set_mode(size)
        screen.blit(self.__game_images.board(), (0, 0))
        
        board_size = self.__game_images.board_size()
        self.__square_width = board_size[0]//8
        self.__square_height = board_size[1]//8
        
        self.__screen = screen

    def update(self, white_pieces, black_pieces):
        self.__clear_screen()
        self.__screen.blit(self.__game_images.board(), (0, 0))

        self.__draw_chess_pieces(white_pieces, self.__square_width, self.__square_height)
        self.__draw_chess_pieces(black_pieces, self.__square_width, self.__square_height)

        self.__pygame.display.update()
    
    def __clear_screen(self):
        black = (0, 0, 0)
        self.__screen.fill(black)
    
    def __draw_chess_pieces(self, pieces, square_width, square_height):                
        for piece in pieces:
            location = (piece.x() * square_width, piece.y() * square_height)
            image = self.__game_images.piece_image(piece.color(), piece.get_type())
            self.__screen.blit(image, location)            

    def click(self):
        is_clicked = False

        while not is_clicked:        
            for event in self.__pygame.event.get():
                if event.type == self.__pygame.QUIT:
                    sys.exit(0)
                
                if event.type == self.__pygame.MOUSEBUTTONUP:
                    is_clicked = True
                    print('Mouse clicked !')
                    x,y = self.__pixel_to_board_coordinates(self.__pygame.mouse.get_pos())
                    print("Width: " + str(x))
                    print("Height: " + str(y))
        return x, y
    
    def __pixel_to_board_coordinates(self, location):
        x = location[0] // self.__square_width
        y = location[1] // self.__square_height
        return x,y
    
    def render_selected_chess_piece(self, chess_piece):
        print("Rendered")
        image = self.__game_images.chess_piece_selection()
        width = chess_piece.x() * self.__square_width
        height = chess_piece.y() * self.__square_height
        self.__screen.blit(image, (width, height))
        self.__pygame.display.update()

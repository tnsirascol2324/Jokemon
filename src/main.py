import pygame
from game import Game
from menu import Menu

if __name__ == '__main__':
    pygame.init()
    game = Game()
    menu = Menu()
    # menu.launching()
    # pygame.init()
    game.run()
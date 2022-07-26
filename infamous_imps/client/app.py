import sys

import pygame

from .mainclient import Game


def start():
    """Start function for client"""
    g = Game()
    g.intro_screen()
    g.new()
    while g.running:
        g.main()

    pygame.quit()
    sys.exit()

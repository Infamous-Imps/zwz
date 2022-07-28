# import sys

# import pygame

# from infamous_imps.client.core.game import Game
import asyncio

from infamous_imps.client.websocket.connection import connect


def start():
    """Start function for client"""
    asyncio.run(connect())
    # g = Game()
    # g.intro_screen()
    # g.new()
    # while g.running:
    #     g.main()

    # pygame.quit()
    # sys.exit()

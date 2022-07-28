import pygame

from infamous_imps.client.config import config


class Life(pygame.sprite.Sprite):
    """Pickable Life Item class"""

    def __init__(self, game, x, y):
        self.game = game
        self._layer = config.PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.pickups
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * config.TILE_SIZE
        self.y = y * config.TILE_SIZE
        self.width = config.TILE_SIZE
        self.height = config.TILE_SIZE
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(config.RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

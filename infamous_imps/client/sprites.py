import math

import pygame

from .config import config


class SpriteSheet:
    """SpriteSheet class"""

    def __init__(self, file):
        self.sheet = pygame.image.load(file)

    def get_sprite(self, x, y, width, height):
        """Get sprite function"""
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(config.WHITE)
        return sprite


class Player(pygame.sprite.Sprite):
    """Player class"""

    def __init__(self, game, x, y):
        self.game = game
        self._layer = config.PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.health = 100
        self.x = x * config.TILE_SIZE
        self.y = y * config.TILE_SIZE
        self.width = config.TILE_SIZE
        self.height = config.TILE_SIZE
        self.x_change = 0
        self.y_change = 0
        self.facing = "down"
        self.animation_loop = 1.0
        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """Update player"""
        self.movement()
        self.animate()
        self.rect.x += self.x_change
        self.collide_blocks("x")
        self.rect.y += self.y_change
        self.collide_blocks("y")
        self.pickups()
        self.x_change = 0
        self.y_change = 0

    def movement(self):
        """Calculate player movement"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += config.PLAYER_SPEED
            self.x_change -= config.PLAYER_SPEED
            self.facing = "left"
        if keys[pygame.K_d]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= config.PLAYER_SPEED
            self.x_change += config.PLAYER_SPEED
            self.facing = "right"
        if keys[pygame.K_w]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += config.PLAYER_SPEED
            self.y_change -= config.PLAYER_SPEED
            self.facing = "up"
        if keys[pygame.K_s]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= config.PLAYER_SPEED
            self.y_change += config.PLAYER_SPEED
            self.facing = "down"

    def collide_blocks(self, direction):
        """Detect objects"""
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.width
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def pickups(self):
        """Pick up item"""
        hits = pygame.sprite.spritecollide(self, self.game.pickups, True)
        if hits and self.health < 100:
            self.health += 10

    def animate(self):
        """Animate player"""
        down_animations = [
            self.game.character_spritesheet.get_sprite(0, 64, self.width, self.height),
            self.game.character_spritesheet.get_sprite(34, 64, self.width, self.height),
            self.game.character_spritesheet.get_sprite(66, 64, self.width, self.height),
        ]

        up_animations = [
            self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.character_spritesheet.get_sprite(32, 0, self.width, self.height),
            self.game.character_spritesheet.get_sprite(64, 0, self.width, self.height),
        ]

        left_animations = [
            self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.character_spritesheet.get_sprite(32, 96, self.width, self.height),
            self.game.character_spritesheet.get_sprite(64, 96, self.width, self.height),
        ]

        right_animations = [
            self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.character_spritesheet.get_sprite(32, 32, self.width, self.height),
            self.game.character_spritesheet.get_sprite(64, 32, self.width, self.height),
        ]
        if self.facing == "down":
            if self.y_change == 0:
                self.image = down_animations[0]
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop > 3:
                    self.animation_loop = 1
        if self.facing == "up":
            if self.y_change == 0:
                self.image = up_animations[0]
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop > 3:
                    self.animation_loop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = left_animations[0]
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop > 3:
                    self.animation_loop = 1

        if self.facing == "right":
            if self.x_change == 0:
                self.image = right_animations[0]
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop > 3:
                    self.animation_loop = 1


class Block(pygame.sprite.Sprite):
    """Block class"""

    def __init__(self, game, x, y):
        self.game = game
        self._layer = config.BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * config.TILE_SIZE
        self.y = y * config.TILE_SIZE
        self.width = config.TILE_SIZE
        self.height = config.TILE_SIZE

        self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Ground(pygame.sprite.Sprite):
    """Ground class"""

    def __init__(self, game, x, y):
        self.game = game
        self._layer = config.GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * config.TILE_SIZE
        self.y = y * config.TILE_SIZE
        self.width = config.TILE_SIZE
        self.height = config.TILE_SIZE

        self.image = self.game.terrain_spritesheet.get_sprite(64, 352, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Button:
    """Button class"""

    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font("infamous_imps/client/fonts/tnr.ttf", fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width / 2, self.height / 2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        """Detect if button is pressed"""
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            else:
                return False
        return False


class Healthbar(pygame.sprite.Sprite):
    """HealthBar class"""

    def __init__(self, game):
        self.game = game
        self._layer = 10
        self.groups = self.game.healthsprite
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = 18 * config.TILE_SIZE - 20
        self.y = 0.5 * config.TILE_SIZE
        self.width = config.TILE_SIZE
        self.height = config.TILE_SIZE
        self.image = pygame.Surface([64, 10])
        self.image.fill(config.RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Fog(pygame.sprite.Sprite):
    """Fog class"""

    def __init__(self, game, x, y):
        self.game = game
        self._layer = 4
        self.groups = self.game.all_sprites, self.game.fog
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * config.TILE_SIZE
        self.y = y * config.TILE_SIZE
        self.width = config.TILE_SIZE
        self.height = config.TILE_SIZE
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(config.GREY)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

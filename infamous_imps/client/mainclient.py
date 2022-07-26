import pygame

from .config import config, tilemap
from .pickupsprites import Life
from .sprites import Block, Button, Fog, Ground, Healthbar, Player, SpriteSheet


class Game:
    """Game class"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.WIN_WIDTH, config.WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font("infamous_imps/client/fonts/tnr.ttf", 32)
        self.character_spritesheet = SpriteSheet("infamous_imps/client/img/character.png")
        self.terrain_spritesheet = SpriteSheet("infamous_imps/client/img/terrain.png")
        self.intro_background = pygame.image.load("infamous_imps/client/img/introbackground.png")

    def create_tilemap(self):
        """Create the tiled map"""
        Healthbar(self)
        px = int(config.WIN_HEIGHT / 64)
        py = int(config.WIN_WIDTH / 64)
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 2:
                    Player(self, j, i)
                if column == 1:
                    Block(self, j, i)
                if i == 3 and j == 3:
                    Life(self, j, i)
                if i + 3 <= px or i - 3 >= px or j + 3 <= py or j - 3 >= py:
                    Fog(self, j, i)

    def new(self):
        """Start new game"""
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.healthsprite = pygame.sprite.LayeredUpdates()
        self.fog = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.pickups = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.create_tilemap()

    def events(self):
        """Handles events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        """Updates sprite image"""
        self.all_sprites.update()

    def draw(self):
        """Draw screen"""
        self.screen.fill(config.BLACK)
        self.all_sprites.draw(self.screen)
        self.healthsprite.draw(self.screen)
        self.clock.tick(config.FPS)
        pygame.display.update()

    def main(self):
        """Main function"""
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def intro_screen(self):
        """Launch screen"""
        intro = True

        title = self.font.render("ZOMBIE WARZONE", True, config.BLACK)
        title_rect = title.get_rect(x=170, y=20)

        play_button = Button(270, 100, 100, 50, config.WHITE, config.BLACK, "Play", 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(config.FPS)
            pygame.display.update()

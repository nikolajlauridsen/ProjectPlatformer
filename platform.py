import pygame

from settings import Settings
settings = Settings()


class Platform(pygame.sprite.Sprite):
    """Platform units can stand on"""

    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(settings.BLACK)

        self.rect = self.image.get_rect()

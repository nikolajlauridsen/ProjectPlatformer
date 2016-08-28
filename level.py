import pygame

from settings import Settings
settings = Settings()


class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game.
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    def __init__(self, player):
        """Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player."""
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """Draw everything on this level. """

        # Draw the background
        screen.fill(settings.SKY)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

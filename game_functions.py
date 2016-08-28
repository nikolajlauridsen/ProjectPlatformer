import pygame
import sys


def check_events():
    """Manage events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #elif event.type == pygame.KEYDOWN:
            # Code keydown events here

        #elif event.type == pygame.KEYDOWN:
            # Code keyup events here


def draw_screen(screen, settings, player):
    screen.fill(settings.WHITE)
    player.blitme()

    pygame.display.flip()

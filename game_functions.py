import pygame
import sys


def check_events(player):
    """Manage events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, player)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)


def check_keydown_events(event, player):
    """Respond to keydown events."""
    if event.key == pygame.K_RIGHT or event.key == 100:
        player.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == 97:
        player.moving_left = True
    if event.key == pygame.K_SPACE:
        player.jump()
    if event.key == 27:
        sys.exit()


def check_keyup_events(event, player):
    """Respond to keyup events."""
    if event.key == pygame.K_RIGHT or event.key == 100:
        player.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == 97:
        player.moving_left = False


def draw_screen(screen, settings, player):
    """Update the screen."""
    screen.fill(settings.WHITE)
    player.blitme()

    pygame.display.flip()

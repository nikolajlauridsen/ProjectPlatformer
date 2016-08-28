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
        player.go_right()
    elif event.key == pygame.K_LEFT or event.key == 97:
        player.go_left()
    if event.key == pygame.K_SPACE:
        player.jump()
    if event.key == 27:
        sys.exit()


def check_keyup_events(event, player):
    """Respond to keyup events."""
    if event.key == pygame.K_RIGHT or event.key == 100 and player.change_x > 0:
        player.stop()
    elif event.key == pygame.K_LEFT or event.key == 97 and player.change_x < 0:
        player.stop()


def draw_screen(screen, settings, player):
    """Update the screen."""
    screen.fill(settings.WHITE)
    player.blitme()

    pygame.display.flip()

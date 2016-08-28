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
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        player.go_right()
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        player.go_left()
    if event.key == pygame.K_SPACE:
        player.jump()
    if event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, player):
    """Respond to keyup events."""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d and player.change_x > 0:
        player.stop()
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a and player.change_x < 0:
        player.stop()

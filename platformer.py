import pygame

import game_functions as gf
from settings import Settings
from player import Player


def main():
    """ Main function for the game. """
    pygame.init()

    # Create settings object
    settings = Settings()

    # Create screen
    screen = pygame.display.set_mode(settings.screen_size)

    pygame.display.set_caption("Platformer")

    # Flag to close game
    running = True

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Create unit objects
    player = Player(screen, settings)

    # -------- Main Program Loop -----------
    while running:

        # Event handling
        gf.check_events(player)

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        player.update()
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        gf.draw_screen(screen, settings, player)

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()


if __name__ == "__main__":
    main()

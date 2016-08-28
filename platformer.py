import pygame

import game_functions as gf
from settings import Settings
from player import Player


def main():
    """ Main function for the game. """
    pygame.init()

    # Create settings object
    gs = Settings()

    # Create screen
    screen = pygame.display.set_mode(gs.screen_size)

    pygame.display.set_caption("Platformer")

    # Flag to close game
    running = True

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Create unit objects
    player = Player(screen, gs)

    # -------- Main Program Loop -----------
    while running:

        gf.check_events()

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        gf.draw_screen(screen, gs, player)

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()


if __name__ == "__main__":
    main()

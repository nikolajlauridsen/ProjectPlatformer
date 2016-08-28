import pygame

import game_functions as gf
import levels
from settings import Settings
from player import Player


def main():
    """ Main function for the game. """

    # -------- Set the stage -----------
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

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    active_sprite_list.add(player)

    # -------- Main Program Loop -----------
    while running:

        # Event handling
        gf.check_events(player)

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        # Update the player.
        active_sprite_list.update()
        # Update items in the level
        current_level.update()
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # Limit to 60 frames per second
        clock.tick(60)

        pygame.display.flip()

    # Close the window and quit.
    pygame.quit()


if __name__ == "__main__":
    main()

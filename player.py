import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, screen, settings):
        """Initialize player and set starting position."""

        # Call the parrent's constructor
        super().__init__()

        self.screen = screen

        # Load player graphics
        self.image = pygame.Surface([40, 80])
        self.image.fill(settings.RED)

        # Set reference to the image rect
        self.rect = self.image.get_rect()
        # Set reference to screen rect
        self.screen_rect = screen.get_rect()

        # Start player in the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the players center.
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # Set X/Y movement vector
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None

        # Player attributes
        self.speed = settings.player_base_speed
        self.jump_height = settings.player_base_jump

    def update(self):
        """Update player's position based on movement flags."""
        # Gravity
        self.calc_grav()

        self.center_x += self.change_x

        self.center_y += self.change_y

        # Update rect object of player
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.35

        # Check if player is on the ground
        if self.rect.y >= self.screen_rect.bottom - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = self.screen_rect.bottom - self.rect.height

    def jump(self):
        """Called when user hits the jump button"""
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2

        # If it is ok to jump set player speed upwards
        if self.rect.bottom >= self.screen_rect.bottom:
            self.change_y = self.jump_height

    def go_left(self):
        """Set the player to move left"""
        self.change_x = -self.speed

    def go_right(self):
        """Set the player to move right"""
        self.change_x = self.speed

    def stop(self):
        """Stop the player movement"""
        self.change_x = 0

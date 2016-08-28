import pygame


class Player():

    def __init__(self, screen, settings):
        """Initialize player and set starting position."""
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

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        # Set X/Y movement vector
        self.change_y = 0

        # Player speed
        self.speed = settings.player_base_speed

    def update(self):
        """Update player's position based on movement flags."""
        # Gravity
        self.calc_grav()

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.speed

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
            self.change_y = -10

    def blitme(self):
        """Draw the ship at the its current location."""
        self.screen.blit(self.image, self.rect)
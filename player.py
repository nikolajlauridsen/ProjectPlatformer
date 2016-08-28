import pygame


class Player():

    def __init__(self, screen, settings):
        """Initialize player and set starting position."""
        self.screen = screen

        # Load player graphics
        self.image = pygame.Surface([40, 60])
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

        # Player speed
        self.speed = settings.player_base_speed

    def update(self):
        """Update player's position base on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.speed

        # Update rect object of player
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        """Draw the ship at the its current location."""
        self.screen.blit(self.image, self.rect)
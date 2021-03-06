
class Settings:

    def __init__(self):
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.SKY = (135, 206, 250)
        # Window options
        self.screen_size = [1280, 720]
        # Player settings
        self.player_base_speed = 7      # Higher for higher speed
        self.player_base_jump = -13     # Lower for higher jump
        # World options
        self.world_shift_right = 900
        self.world_shift_left = 300

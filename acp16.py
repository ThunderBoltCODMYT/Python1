import pygame
import random
# Sprite Class representing the moving object
class Sprite(pygame.sprite.Sprite):

    # Constructor Method
    def __init__(self, color, height, width):
        # Call to the parent class (Sprite) constructor
        super().__init__()
        #Create the Sprites surface with dimension and colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #Get the sprites rect defining its position and size
        self.rect = self.image.get_rect()
# Create a group to hold the sprite
all_sprites_list = pygame.sprite.Group()
# Instantiate the sprite
sp1 = Sprite(pygame.color.Color('white'), 20, 30)
# Randomly position the sprite
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
# Add the sprite to the group
all_sprites_list.add(sp1)
# Create the game window
screen = pygame.display.set_mode((500, 400))
# Set the window title
pygame.display.set_caption("Colorful Bounce")
# Set the initial background color
bg_color = pygame.color.Color('blue')
# Apply the background color
screen.fill(bg_color)
# Game loop control flag
exit = False
# Create a clock object to control frame rate
clock = pygame.time.Clock()
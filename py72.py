import pygame
import random

#initialize pygame module
pygame.init()

#Custom event ids for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

#Define basic colors using pygame.Color
#Background Colors
BLUE = pygame.Color('Blue')
LIGHTBLUE = pygame.Color('Lightblue')
DARKBLUE = pygame.Color('Darkblue')

#Sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('Magenta')
ORANGE = pygame.Color('Orange')
WHITE = pygame.Color('white')


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
        # Set initial velocity with random direction
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    # Method to update the Sprites position
    def update(self):
        #Move the Sprite by its velocity
        self.rect.move_ip(self.velocity)
        #Flag to track if the sprite hits a boundary
        boundary_hit = False
        #Check for collision with left or right boundaries and reverse direction(top, bottom)
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        #Check for top and bottom collision and reverse direction
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        #If a boundary was hit post events to change color
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    # method to change the sprites color
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))

# Function to change the background color
def change_background_color():
    global bg_color
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])


# Create a group to hold the sprite
all_sprites_list = pygame.sprite.Group()
# Instantiate the sprite
sp1 = Sprite(WHITE, 20, 30)
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
bg_color = BLUE
# Apply the background color
screen.fill(bg_color)
# Game loop control flag
exit = False
# Create a clock object to control frame rate
clock = pygame.time.Clock()

# Main game Loop
while not exit:
    # Event handling loop
    for event in pygame.event.get():
        # If the window's close button is clicked, exit the game
        if event.type == pygame.QUIT:
            exit = True

        # If the sprite color change event is triggered, change the sprite's color
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()

        # If the background color change event is triggered, change the background color
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    # Update all sprites
    all_sprites_list.update()

    # Fill the screen with the current background color
    screen.fill(bg_color)

    # Draw all sprites to the screen
    all_sprites_list.draw(screen)

    # Refresh the display
    pygame.display.flip()

    # Limit the frame rate to 240 fps
    clock.tick(240)

# Uninitialize all pygame modules and close the window
pygame.quit()
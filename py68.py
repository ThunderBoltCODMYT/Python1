#Import Necessary Libraries
import pygame
#Initialize required modules
pygame.init()
#Setup Window geometry
screen = pygame.display.set_mode((400,500))
#Create a loop to urn till the game is quit by the user
done = False
while not done:
    #Clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #make the changes visible
    pygame.display.flip()

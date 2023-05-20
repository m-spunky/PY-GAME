# Class Initialization
import pygame
pygame.init()

# Screen Setup
scr_x = 400
scr_y = 400
screen = pygame.display.set_mode((scr_x,scr_y))

# Main Loop
while True:
    # Check for any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
 

    # Update All New Changes
    pygame.display.flip()

























# IN Work
        # if event.type == pygame.KEYDOWN:
        #     if (inline==True & (r < 240 | g<240 | b<240) ):
        #         r+=10
        #         g+=10
        #         b+=10
        #     else:
        #         inline = False
        #         if (inline==False & (r > 0 | g>0 | b>0) ):
        #             r-=10
        #             g-=10
        #             b-=10
        #         else:
        #             inline = True
import pygame
pygame.init()


# Colours Library
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
clrs = [red,white,black,green,blue]

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Clr Changer")

index = 0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            # Iterate Over Library
            if index < (len(clrs)-1):
                # Increment Index
                index +=1
            # If limit exceeds index=0
            else:
                index = 0
        
        # Change Screen Colour
        screen.fill(clrs[index])

    pygame.display.flip()

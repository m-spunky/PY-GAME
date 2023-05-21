# Class Initialization
import pygame
pygame.init()

# Screen Setup
scr_x = 800
scr_y = 600
screen = pygame.display.set_mode((scr_x,scr_y))

# Function : TO resize the given IMG
def resize_img(path,w_multiplier,h_multiplier):
    img = pygame.image.load(path)
    width = img.get_rect().width
    height = img.get_rect().height
    image = pygame.transform.scale(img,(int(width*w_multiplier),int(height*h_multiplier)))

    return image

#Background 
bg_img = resize_img(r"PY-GAME/fundamentals/PNG/Stall/bg_blue.png",3.2,2.5)


# Main Loop
while True:
    # Check for any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
 

    # Background added
    screen.blit(bg_img,(0,0))
    # Update All New Changes
    pygame.display.flip()


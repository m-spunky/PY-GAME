# Class Initialization
import pygame
pygame.init()

# Screen Setup
scr_x = 800
scr_y = 600
screen = pygame.display.set_mode((scr_x,scr_y))


# Function : TO resize the given IMG
def load_img(path,w_multiplier,h_multiplier):
    img = pygame.image.load(path)
    width = img.get_rect().width
    height = img.get_rect().height
    image = pygame.transform.scale(img,(int(width*w_multiplier),int(height*h_multiplier)))
    return image
#Background 
bg_img = load_img(r"PY-GAME/fundamentals/PNG/Stall/bg_blue.png",3.2,2.5)


# SPrite Class For Targets
class Target(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        super().__init__()
        self.image = load_img(img,0.5,0.5)
        # Bounding rectangle to image
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]



# # Adding ALL Targets to one Group
target_grp = pygame.sprite.Group()
# Random location of Targets
import random
for i in range(20):
    target= Target(f"PY-GAME/fundamentals/PNG/Objects/target_colored.png",random.randrange(0,scr_x),random.randrange(0,scr_y))
    target_grp.add(target)


# Main Loop
while True:
    # Check for any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(bg_img,(0,0))
    #Draw All the Targets on main screen  
    target_grp.draw(screen)

    # Update All New Changes
    pygame.display.flip()
























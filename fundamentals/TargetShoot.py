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


dist = 20
# SPrite Class For MOUSE - POINTER
class Pointer(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = load_img(img,1,1)
        self.rect = self.image.get_rect()
    # Action : IF pointer and targets coords collide target destroy
    def shoot(self):
        for i in target_xy:
            if (abs(i[0] - pygame.mouse.get_pos()[0]) < dist) & (abs(i[1] - pygame.mouse.get_pos()[1]) < dist) :
                t = Target(f"PY-GAME/fundamentals/PNG/Objects/target_colored.png",i[0],i[1])
                t.kill()
        # pygame.sprite.spritecollide(pointer,target_grp,True)
    # Pointer hover with mouse 
    def update(self):
        self.rect.center = pygame.mouse.get_pos()


# SPrite Class For Targets
class Target(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        super().__init__()
        self.image = load_img(img,0.5,0.5)
        # Bounding rectangle to image
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.x = x
        self.y = y
    
    def kill(self):
        print(f"{self.x},{self.y} are shoot")





# # Adding ALL Targets to one Group
target_grp = pygame.sprite.Group()
# Random location of Targets
target_xy = []
import random
for i in range(20):
    target_x = random.randrange(0,scr_x)
    target_y = random.randrange(0,scr_y)
    if (target_xy.count((target_x,target_y)) < 1) & (target_xy.count((target_x,target_y)) < 1):
        target= Target(f"PY-GAME/fundamentals/PNG/Objects/target_colored.png",target_x,target_y)
        target_grp.add(target)
        target_xy.append((target_x,target_y))
    else:
        continue

pointer_grp = pygame.sprite.Group()
pointer = Pointer(f"PY-GAME/fundamentals/PNG/HUD/crosshair_red_large.png")
pointer_grp.add(pointer)


# Main Loop
while True:
    # Check for any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pointer.shoot()

    screen.blit(bg_img,(0,0))
    #Draw All the Targets on main screen  
    target_grp.draw(screen)
    pointer_grp.draw(screen)
    pointer_grp.update()
    # Update All New Changes
    pygame.display.flip()
























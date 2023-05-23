import pygame,sys

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.frames = []
        for i in range(10):
            self.frames.append(pygame.image.load(f'Animation/attack_{i+1}.png'))


        self.is_animating = False
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def isAnimating(self):
        self.is_animating = True

    def isNotAnimating(self):
        self.is_animating = False

    def update(self,speed):
        print(self.current_frame)
        if self.is_animating == True:
            self.current_frame += speed
            index = int(self.current_frame % len(self.frames))
            self.image = self.frames[index]



pygame.init()
screen = pygame.display.set_mode((400,400))



moving_sprites = pygame.sprite.Group()
p1 = Player(100,100)
moving_sprites.add(p1)
p2 = Player(300,100)
moving_sprites.add(p2)





while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            [p.isAnimating() for p in moving_sprites] 
        if event.type == pygame.KEYUP:
            [p.isNotAnimating() for p in moving_sprites]
    
    screen.fill((0,0,0))

    moving_sprites.draw(screen)
    moving_sprites.update(0.1)
    pygame.display.flip()

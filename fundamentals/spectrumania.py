import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Spectrumania")

r=55
g=55
b=55

clr = (0,0,0)
font = pygame.font.Font(None,36)
loc= (300,20)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if (r<245):
                    r+=10
                else:
                    r=0
            if event.key == pygame.K_g:
                if (g<245):
                    g+=10
                else:
                    g=0
            if event.key == pygame.K_b:
                if (b<245):
                    b+=10
                else:
                    b=0

    screen.fill((r,g,b))       
    screen.blit(font.render(f"r:{r} g:{g} b:{b}",True,clr),loc)
    pygame.display.flip()

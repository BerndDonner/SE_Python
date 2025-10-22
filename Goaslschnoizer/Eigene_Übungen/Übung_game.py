import pygame
import random
pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
width,height = screen.get_size()
clock = pygame.time.Clock()
start = True

rand_circles = []

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                start = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_rand = random.randint(0,width)
            y_rand = random.randint(0,height)
            rand_circles.append((x_rand,y_rand))
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill((255,255,255))
            
    blue = (0,0,255)
    
    pygame.display.set_caption("Wurzelsepp")
    screen.fill((255,255,255)) 

    x, y = pygame.mouse.get_pos()

    pygame.draw.circle(screen, blue, (x,y),100,0)

    for pos in rand_circles:
        pygame.draw.circle(screen,blue,pos,50,0)
   

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

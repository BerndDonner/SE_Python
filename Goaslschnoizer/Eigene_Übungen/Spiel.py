import pygame

pygame.init()
 
screen = pygame.display.set_mode((400, 300))

clock = pygame.time.Clock()
 
x, y = 200, 150

speed = 5

running = True
 
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:  x -= speed

    if keys[pygame.K_RIGHT]: x += speed

    if keys[pygame.K_UP]:    y -= speed

    if keys[pygame.K_DOWN]:  y += speed
 
    screen.fill((30, 30, 30))

    pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)

    pygame.display.flip()

    clock.tick(60)
 
pygame.quit()

 
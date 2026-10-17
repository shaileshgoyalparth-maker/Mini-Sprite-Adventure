
import pygame

pygame.init()

screen_width = 600
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Rectangle and Circles")

GREEN = (0, 255, 0)
BLUE = (0, 125, 255)

x = 30
y = 30
speed = 5

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    x = max(0, min(x, screen_width - 60))
    y = max(0, min(y, screen_height - 60))

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, BLUE, (x, y, 60, 60))

    pygame.draw.circle(screen, GREEN, (300, 300), 50)
    pygame.draw.circle(screen, GREEN, (100, 100), 50, 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

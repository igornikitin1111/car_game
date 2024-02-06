import pygame
from pygame.locals import *

size = width, height = (800, 800)
road_width = int(width/1.6)
roadmark_width = int(width/80)

pygame.init()
running = True
# set window size
screen = pygame.display.set_mode(size)
# set title
pygame.display.set_caption("Speedcar game")

# set background colour
screen.fill((60, 220, 0))
# draw graphics - black road
pygame.draw.rect(
    screen,
    (50, 50, 50),
    (width/2-road_width/2, 0, road_width, height)
)
# yellow mid line
pygame.draw.rect(
    screen,
    (255, 240, 60),
    (width/2 - roadmark_width/2, 0, roadmark_width, height)
)
# white border line left
pygame.draw.rect(
    screen,
    (255, 255, 255),
    (width/2 - road_width/2 + roadmark_width*2, 0, roadmark_width, height)
)
# white border line right
pygame.draw.rect(
    screen,
    (255, 255, 255),
    (width/2 + road_width/2 - roadmark_width*3, 0, roadmark_width, height)
)

# apply changes
pygame.display.update()

# load player vehicle images
car1 = pygame.image.load("D:/Programmin in VS/GitHub/SomeStuff/pygame_car_game/images/blue_car.png")
car_location1 = car1.get_rect()
car_location1.center = width/2 + road_width/4, height*0.8

# load enemy vehicle images
car2 = pygame.image.load("D:/Programmin in VS/GitHub/SomeStuff/pygame_car_game/images/red_car.png")
car_location2 = car2.get_rect()
car_location2.center = width/2 - road_width/4, height*0.2

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_location1 = car_location1.move([-int(road_width/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_location1 = car_location1.move([int(road_width/2), 0])
    
    # set background colour
    screen.fill((60, 220, 0))
    # draw graphics - black road
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2-road_width/2, 0, road_width, height)
    )
    # yellow mid line
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2 - roadmark_width/2, 0, roadmark_width, height)
    )
    # white border line left
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - road_width/2 + roadmark_width*2, 0, roadmark_width, height)
    )
    # white border line right
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_width/2 - roadmark_width*3, 0, roadmark_width, height)
    )

    screen.blit(car1, car_location1)
    screen.blit(car2, car_location2)
    pygame.display.update()

pygame.quit()
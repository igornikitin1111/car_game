import pygame
from pygame.locals import *
import random

size = width, height = (800, 800)
road_width = int(width/1.6)
roadmark_width = int(width/80)
right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4
car_speed = 1

pygame.init()
running = True
# set window size
screen = pygame.display.set_mode(size)
# set title
pygame.display.set_caption("Speedcar game")

# apply changes
pygame.display.update()

# load player vehicle images
car1 = pygame.image.load("D:/Programmin in VS/GitHub/SomeStuff/pygame_car_game/images/blue_car.png")
car1_location = car1.get_rect()
car1_location.center = right_lane, height*0.8

# load enemy vehicle images
car2 = pygame.image.load("D:/Programmin in VS/GitHub/SomeStuff/pygame_car_game/images/red_car.png")
car2_location = car2.get_rect()
car2_location.center = left_lane, height*0.2

counter = 0
# game loop
while running:
    counter += 1
    if counter == 5000:
        car_speed += 0.15
        counter = 0
        print("level up", car_speed)
    
    # animate enemy vehicle
    car2_location[1] += car_speed
    if car2_location[1] > height:
        if random.randint(0, 1) == 0:
            car2_location.center = right_lane, -200
        else:
            car2_location.center = left_lane, -200

    # end game
    if car1_location[0] == car2_location[0] and car2_location[1] > car1_location[1] - 100:
        print("Game over! You Lost!")
        break

    # event listenersa
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car1_location = car1_location.move([-int(road_width/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car1_location = car1_location.move([int(road_width/2), 0])
    
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

    screen.blit(car1, car1_location)
    screen.blit(car2, car2_location)
    pygame.display.update()

pygame.quit()
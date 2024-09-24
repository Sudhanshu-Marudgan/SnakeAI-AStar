import pygame
import numpy as np
import math
import random
from astar import *
import time

pygame.init()

BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

GRID_SIZE = 30
GRID_WIDTH = 30
GRID_HEIGHT = 30
WINDOW_WIDTH = GRID_SIZE * GRID_WIDTH
WINDOW_HEIGHT = GRID_SIZE * GRID_HEIGHT

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("SnakeAI")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Logic here
    playableSpace = 30
    l = playableSpace
    field = np.zeros((l, l), dtype = int)

    nodenum = l*l
    nodenames = list(range(1,nodenum + 1))
    blankfield = field
    allblankfield = np.zeros((l, l), dtype = int)
    head = math.ceil(nodenum/2 + math.ceil(l/2))
    snake = [head, head+1, head+2]
    
    def coords(indnum):
        coords = [math.ceil(indnum/l)-1,((indnum-1)%l)]
        # returns [row, col]
        return coords
    
    def inds(coordnum):
        inds = coordnum[:,1]+(coordnum[:,0]*l)+1
        # col + (row*grid) + 1
        # returns index number according to nodenames
        return inds
    
    # drop the apple in un-snaked region
    openfield = nodenames
    openfield = [elem for elem in openfield if elem not in snake]
    apple = openfield[random.randint(1,len(openfield))]

    optimalPath = [-50, -50]

    ########## THE GAME ITERATOR ##########
    gameiter = 0

    while True:
        gameiter = gameiter + 1

        ##### Choose Move #####

        #draw currentMap
        field = blankfield
        snake_row, snake_col = np.unravel_index(snake, (30, 30))
        field[snake_row, snake_col-1] = 1

        needtoupdate = False
        # if np.sum([math.fabs(i) for i in [xi - yi for xi, yi in zip(coords(snake[-1]), optimalPath)]] < 1, axis=0).sum() == 2:
        #     # disp('recalc route - tail moved')
        #     needtoupdate = True
        if len(optimalPath) < 1 or len(optimalPath) == 1:
            needtopudate = True
        if coords(apple) != optimalPath[0]:
            needtoupdate = True
        if needtoupdate:
            # draw goal map
            goalm = np.zeros((l,l),dtype = int)
            goalm[math.ceil(apple/l)-1][(apple-1)%l] = 1
            
            # running path finder
            optimalPath = main(math.ceil(snake[0]/l)-1,((snake[0]-1)%l),snake,apple)
            print(optimalPath)
            # print(coords(apple))
            # print(coords(snake[0]))
        
        nextStep = optimalPath[1]
        optimalPath = optimalPath[:-1]

        ########## Plotting ##########
        screen.fill(BLACK)
        snakecoords = [coords(snake[tup]) for tup in range(0, len(snake))]
        applecoords = coords(apple)
        for segment in snakecoords:
            pygame.draw.rect(screen, GREEN, (segment[1] * GRID_SIZE, segment[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        
        pygame.draw.rect(screen, RED, (applecoords[1] * GRID_SIZE, applecoords[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        font = pygame.font.Font(None, 36)
        text = font.render("Snake Lenght: {}".format(len(snake)), True, WHITE)
        screen.blit(text, (10, 10))
        pygame.display.flip()
        time.sleep(0.05)

        if gameiter > 100000:
            print("Failed - hit 200k steps...")
            running = False
            break

        ########## game stuff ##########
        nextstepinds = nextStep[1] + (nextStep[0]*l) +1
        if nextstepinds == apple:
            snake = [nextstepinds] + snake
            if len(snake) == nodenum:
                print("Done! Game Completed")
                running = False
                break

            field = np.zeros((l, l), dtype = int)
            snake_row, snake_col = np.unravel_index(snake, (30, 30))
            field[snake_row, snake_col-1] = 1
            openfield = nodenames
            openfield = [elem for elem in openfield if elem not in snake]
            apple = openfield[random.randint(1,len(openfield))]

        else:
            snake[1:] = snake[:-1]
            snake[0] = nextstepinds
pygame.quit()


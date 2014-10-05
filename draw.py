#!/usr/bin/python

import sys
import pygame
import time
import random
import fileinput

#this script uses the array of coordinates generated at each step by the generate.py script, draws and updates them, thus creating an animation

w=(10, 10)

data = open(sys.argv[1], 'r')

pygame.init()
window = pygame.display.set_mode((640, 480))

for line in data:
    window.fill((0, 0, 0))
    coordinates=[]
    for i in line.split():
        coordinates.append(map(int, i.split(':')))

    #draw a square for each pair of coordinates
    for i in coordinates:
        pygame.draw.rect(window, ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))), pygame.Rect((10*i[0], -10*i[1]), w))

    #this updates the screen and draws the rectangles generated above
    pygame.display.flip()

    #listen for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    time.sleep(0.1)


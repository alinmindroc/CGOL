#!/usr/bin/python

import sys
import pygame
import time
import random

w=(10, 10)

data = open(sys.argv[1], 'r')

pygame.init()
window = pygame.display.set_mode((640, 480))

for line in data:
	window.fill((0, 0, 0))
	coordinates=[]
	for i in line.split():
			coordinates.append(map(int, i.split(':')))

	print coordinates
	for i in coordinates:
		pygame.draw.rect(window, ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))), pygame.Rect((10*i[0], -10*i[1]), w))

	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)

	time.sleep(0.1)


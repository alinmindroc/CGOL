#!/usr/bin/python

#draws each line of coordinates from file received as command-line arg

import sys
import pygame
import time
import random
import fileinput

w=(10, 10)

data = open(sys.argv[1], 'r')

pygame.init()
window = pygame.display.set_mode((640, 480))

for line in data:
	window.fill((0, 0, 0))
	coordinates=[]
	for i in line.split():
			coordinates.append(map(int, i.split(':')))

	#desenez un patratel pentru fiecare pereche de coordonate din fisierul de intrare
	for i in coordinates:
		pygame.draw.rect(window, ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))), pygame.Rect((10*i[0], -10*i[1]), w))

	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)

	time.sleep(0.1)


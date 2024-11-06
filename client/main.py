# -*- coding: utf-8 -*-
import sys
import pygame
import os

fps = 5

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('test')

clock = pygame.time.Clock()

image = pygame.image.load(os.path.join('resources', 'pictures', 'grass.jpg')).convert()
imageSmall = pygame.transform.scale(image, (60, 60))

while 1:
    now_t = clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(imageSmall, (-30, -30))
    pygame.display.flip()
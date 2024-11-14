# -*- coding: utf-8 -*-
import sys
import pygame
import os
import enum
import random

FRAME_FPS = 5
MOVE_SPEED = 5

TILES_SIZE = 20
WINDOW_WIDTH = 32
WINDOW_HEIGHT = 24
WINDOW_WIDTH_SIZE = WINDOW_WIDTH * TILES_SIZE
WINDOW_HEIGHT_SIZE = WINDOW_HEIGHT * TILES_SIZE

MAP_WIDTH = 100
MAP_HEIGHT = 100

COMMAND_UP = 'up'
COMMAND_DOWN = 'down'
COMMAND_LEFT = 'left'
COMMAND_RIGHT = 'right'

class TilesType(enum.IntEnum):
    UNKNOW = 0
    GRASS = 1
    ROCKS = 2

class Map():
    def __init__(self):
        self.tiles = []
        self.surface = pygame.Surface((MAP_WIDTH * TILES_SIZE, MAP_HEIGHT * TILES_SIZE), pygame.HWSURFACE)

        grassImg = pygame.image.load(os.path.join('resources', 'pictures', 'grass.jpg')).convert()
        rocksImg = pygame.image.load(os.path.join('resources', 'pictures', 'rocks.jpg')).convert()
        grassTile = pygame.transform.scale(grassImg, (TILES_SIZE, TILES_SIZE))
        rocksTile = pygame.transform.scale(rocksImg, (TILES_SIZE, TILES_SIZE))

        for row in range(MAP_HEIGHT):
            self.tiles.append([])
            for col in range(MAP_WIDTH):
                self.tiles[row].append(random.choice([TilesType.GRASS, TilesType.ROCKS]))

                tile = None
                if self.tiles[row][col] == TilesType.GRASS:
                    tile = grassTile
                elif self.tiles[row][col] == TilesType.ROCKS:
                    tile = rocksTile

                if tile:
                    self.surface.blit(tile, (col * TILES_SIZE, row * TILES_SIZE))

class MapRender():
    def __init__(self):
        self.left = 0
        self.top = 0
        self.source = Map()

    def move_left(self):
        self.left = max(self.left - MOVE_SPEED, 0)

    def move_right(self):
        self.left = min(self.left + MOVE_SPEED, (MAP_WIDTH - WINDOW_WIDTH) * TILES_SIZE)

    def move_up(self):
        self.top = max(self.top - MOVE_SPEED, 0)

    def move_down(self):
        self.top = min(self.top + MOVE_SPEED, (MAP_HEIGHT - WINDOW_HEIGHT) * TILES_SIZE)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.source.surface, pygame.Rect(self.left, self.top, WINDOW_WIDTH_SIZE, WINDOW_HEIGHT_SIZE))

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH_SIZE, WINDOW_HEIGHT_SIZE))
    clock = pygame.time.Clock()

    mapRender = MapRender()

    while 1:
        now_t = clock.tick(FRAME_FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                print('deal event key down.')
                if event.key == pygame.K_w:
                    print('up')
                    mapRender.move_up()
                if event.key == pygame.K_a:
                    print('left')
                    mapRender.move_left()
                if event.key == pygame.K_s:
                    print('down')
                    mapRender.move_down()
                if event.key == pygame.K_d:
                    print('right')
                    mapRender.move_right()

        mapRender.draw(screen)
        pygame.display.flip()

# -*- coding: utf-8 -*-
import enum
import os
import pygame

class _TilesType(enum.IntEnum):
    UNKNOW = 0
    GRASS = 1
    ROCKS = 2
    RIVER = 3

class _Tiles():
    def __init__(self, tType: _TilesType, size: int):
        self.tType: _TilesType = tType
        self.size = size

        image: pygame.Surface = pygame.image.load(os.path.join('resources', 'pictures', tType.name)).convert()
        self.image = pygame.transform.scale(image, (size, size))

    def tiles_type(self):
        return self.tType

    def draw(self, face: pygame.Surface, x: int, y: int):
        face.blit(self.image, (x, y))

class Map():
    def __init__(self, windowWidth: int, windowHeight: int, tilesSize: int):
        self.x: int = 0
        self.y: int = 0
        self.width: int = 0
        self.height: int = 0

        self.surface: pygame.Surface = pygame.Surface((windowWidth, windowHeight))

        self.tilesSize = tilesSize
        self.tiles: list = []

    def get_tiles_type(self, x, y):
        if x < self.width and y < self.height:
            tiles: _Tiles = self.tiles[self.width * y + x]
            return tiles.tiles_type()

        return _TilesType.UNKNOW

    def init_with_file(self, file):
        pass

    def draw(self):
        pass

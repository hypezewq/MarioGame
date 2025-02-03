import pygame

from classes.collider import Collider
from classes.entitycollider import EntityCollider
from entities.EntityBase import EntityBase


class WinFlag(EntityBase):
    def __init__(self, screen, spriteColl, x, y, level, gravity=1):
        super(WinFlag, self).__init__(x, y, gravity)
        self.spriteCollection = spriteColl
        self.rect = pygame.Rect(x * 32, y * 32, 32, 32 * 5)
        self.screen = screen
        self.timer = 0
        self.type = "Object"
        self.dashboard = level.dashboard
        self.collision = Collider(self, level)
        self.EntityCollider = EntityCollider(self)
        self.levelObj = level

    def update(self, camera):
        ...

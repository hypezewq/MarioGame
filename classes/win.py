import pygame
import sys

from classes.spritesheet import Spritesheet
from classes.gaussianblur import GaussianBlur


class Win:
    def __init__(self, screen, entity, dashboard):
        self.screen = screen
        self.entity = entity
        self.dashboard = dashboard
        self.state = 0
        self.spritesheet = Spritesheet("./img/title_screen.png")
        self.win_srfc = GaussianBlur().filter(self.screen, 0, 0, 640, 480)
        self.dot = self.spritesheet.image_at(
            0, 150, 2, colorkey=[255, 0, 220], ignoreTileSize=True
        )
        self.gray_dot = self.spritesheet.image_at(
            20, 150, 2, colorkey=[255, 0, 220], ignoreTileSize=True
        )

    def update(self):
        self.screen.blit(self.win_srfc, (0, 0))
        self.dashboard.drawText("YOU WON", 120, 160, 68)
        self.dashboard.drawText(f"YOU PASSED {self.entity.levelObj.levelname.upper()}", 150, 250, 25)
        self.dashboard.drawText(f"SCORE: {self.dashboard.points}  COINS: {self.dashboard.coins}  TIME: {self.dashboard.time}", 140, 140, 10)
        self.dashboard.drawText("BACK TO MENU", 150, 320, 32)
        self.drawDot()
        pygame.display.update()
        self.checkInput()

    def drawDot(self):
        self.screen.blit(self.dot, (100, 315))

    def checkInput(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.entity.restart = True

    def createBackgroundBlur(self):
        self.win_srfc = GaussianBlur().filter(self.screen, 0, 0, 640, 480)

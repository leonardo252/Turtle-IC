import pygame

class Background:

    def __init__(self):
        self.x = 15
        self.y = 15
        self.width = 680 - (2 * self.x)
        self.height = 680 - (2 * self.y)

    def drawBackground(self, screen):
        frameRect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (255, 153, 51), frameRect)
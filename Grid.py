import pygame


class Grid:

    def __init__(self):
        self.x = 15
        self.y = 15
        self.height = 50
        self.width = 50
        

    def drawGrid(self, screen):
        x = self.x
        y = self.y
        width = self.width
        height = self.height

        for _ in range(13):
            for _ in range(13):
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, width, height), 1)
                x += self.width
            
            x = self.x
            y += self.width


import pygame

class Turtle(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load("turtle.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def moveTurtle(self, movement):
        aux = 0

        if movement == "up":
            if ((self.rect.y - 50) < 15):
                pass
            else:
                while(aux < 50):
                    self.rect.y -= 10
                    aux += 10

        
        elif movement == "down":
            if ((self.rect.y + 50) > 665):
                pass
            else:
                while(aux < 50):
                    self.rect.y += 10
                    aux += 10

        
        elif movement == "left":
            if ((self.rect.x - 50) < 15):
                pass
            else:
                while(aux < 50):
                    self.rect.x -= 10
                    aux += 10


        elif movement == "right":
            if ((self.rect.x + 50) > 665):
                pass
            else:
                while(aux < 50):
                    self.rect.x += 10
                    aux += 10
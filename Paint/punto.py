import pygame
class Punto(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image= pygame.Surface((10,10))
        self.image.fill("red")
        self.rect= self.image.get_rect(topleft= pos)
        
import pygame
from math import sqrt
class Punto(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image= pygame.Surface((10,10))
        self.image.fill("red")
        self.rect= self.image.get_rect(topleft= pos)
        self.posicion=pos
    def entregar_posicion(self):
        return self.posicion
    def calcular_distancia(self,punto):
        return sqrt(((self.rect.x-punto.rect.x)**2)+((self.rect.y-punto.rect.y)**2))

        
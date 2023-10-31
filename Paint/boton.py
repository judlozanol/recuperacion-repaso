import pygame
from ajustes import *
from utilidades import imagen_redimensionada
class Boton(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image
        self.rect = self.image.get_rect(topleft=pos)
    
class BotonCirculo(Boton):
    def __init__(self, pos):
        self.image=imagen_redimensionada("Paint/sprites/circulo.png", 100,100)
        super().__init__(pos)

class BotonRectangulo(Boton):
    def __init__(self, pos):
        self.image=imagen_redimensionada("Paint/sprites/rectangulo.png", 100,100)
        super().__init__(pos)

class BotonBorrador(Boton):
    def __init__(self, pos):
        self.image=imagen_redimensionada("Paint/sprites/borrador.png", 100,100)
        super().__init__(pos)

class BotonTriangulo(Boton):
    def __init__(self, pos):
        self.image=imagen_redimensionada("Paint/sprites/triangulo.png", 100,100)
        super().__init__(pos)
    
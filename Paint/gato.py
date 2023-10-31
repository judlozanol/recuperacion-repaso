import pygame
from utilidades import imagen_redimensionada
class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=imagen_redimensionada("Paint/sprites/cursor.png", 25,25)
        self.rect = self.image.get_rect(topleft=pygame.mouse.get_pos())
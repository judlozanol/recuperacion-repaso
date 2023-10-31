import pygame
from utilidades import imagen_redimensionada
from stateM import *
class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=imagen_redimensionada("Paint/sprites/cursor.png", 25,25)
        self.rect = self.image.get_rect(topleft= pygame.mouse.get_pos())#topleft= pygame.mouse.get_pos()

    def update(self):
        mouse_pos= pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = mouse_pos[1]

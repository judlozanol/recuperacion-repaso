import pygame
from boton import *
import ajustes
class InterfazFiguras(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        x=50 
        y= (ajustes.ALTO_PANTALLA/2)-200
        botones=[BotonRectangulo((x,y)),BotonCirculo((x,y+100)),BotonTriangulo((x,y+200)),BotonBorrador((x,y+300))]
        for boton in botones:
            self.add(boton)
        

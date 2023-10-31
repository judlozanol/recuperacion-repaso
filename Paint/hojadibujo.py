import pygame
from stateM import *
from interfazfiguras import *
from cursor import *
from gato import *

class HojaDibujo:
    def __init__(self,capa):
        self.capa=capa
        self.estado=StateM("Borrar")
        self.interfaz= InterfazFiguras()
        self.cursor= pygame.sprite.Group()
        self.cursor.add(Cursor())
        self.gatos=pygame.sprite.Group()

    def get_input(self):
        eventos= pygame.event.get(pygame.MOUSEBUTTONUP)
        for event in eventos:
            if event.type == pygame.MOUSEBUTTONUP:
                gato = Gato()
                self.gatos.add(gato)

    def run(self):
        self.get_input()
        self.interfaz.draw(self.capa)

        self.cursor.update()
        self.gatos.draw(self.capa)
        self.cursor.draw(self.capa)
        
        
    
    
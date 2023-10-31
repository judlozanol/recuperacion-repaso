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

    def get_input(self):
        eventos=pygame.event.get()
        for event in eventos:
            if event.type == pygame.MOUSEBUTTONUP:
                gato = Gato()
                self.cursor.add(gato)

    def run(self):
        self.get_input()
        self.interfaz.draw(self.capa)

        self.cursor.update()
        self.cursor.draw(self.capa)
        
        
    
    
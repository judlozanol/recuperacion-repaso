import pygame
from stateM import *
from interfazfiguras import *
from cursor import *

class HojaDibujo:
    def __init__(self,capa):
        self.capa=capa
        self.estado=StateM("Borrar")
        self.interfaz= InterfazFiguras()
        self.cursor= pygame.sprite.GroupSingle()
        self.cursor.add(Cursor())
        self.figuras = pygame.sprite.Group()
        self.puntos= pygame.sprite.Group()

    def get_input(self):
        click= pygame.mouse.get_pressed()
        
        if click[0]:
            if self.cursor.sprite.rect.colliderect(self.interfaz.sprites()[0].rect):
                self.estado.set_status("Rectangulo")
            elif self.cursor.sprite.rect.colliderect(self.interfaz.sprites()[1].rect):
                self.estado.set_status("Circulo")
            elif self.cursor.sprite.rect.colliderect(self.interfaz.sprites()[2].rect):
                self.estado.set_status("Triangulo")
            elif self.cursor.sprite.rect.colliderect(self.interfaz.sprites()[3].rect):
                self.estado.set_status("Borrar")
            print(self.estado.get_status())


            

    def run(self):
        self.get_input()
        self.interfaz.draw(self.capa)

        self.cursor.update()
        self.cursor.draw(self.capa)
        
        
    
    
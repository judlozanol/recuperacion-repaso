import pygame
from stateM import *
from interfazfiguras import *
from cursor import *
from punto import Punto
from ajustes import *

class HojaDibujo:
    def __init__(self,capa):
        self.capa=capa
        self.estado=StateM("Borrar")

        self.interfaz= InterfazFiguras()
        self.cursor= pygame.sprite.GroupSingle()
        self.cursor.add(Cursor())
        self.puntos= pygame.sprite.Group()
        self.contador=0
    def get_input(self):
        click= pygame.mouse.get_pressed()
        pygame.time.delay(80)
        if click[0]:
            if self.cursor.sprite.rect.colliderect(self.interfaz.sprites()[0].rect):
                self.estado.set_status("Rectangulo")
            elif self.cursor.sprite.rect.colliderect(self.interfaz.sprites()[1].rect):
                self.estado.set_status("Circulo")
            elif self.cursor.sprite.rect.colliderect(self.interfaz.sprites()[2].rect):
                self.estado.set_status("Triangulo")
            
            else:
                if self.estado.get_status()=="Circulo":
                    if self.contador<2:
                        punto=Punto(pygame.mouse.get_pos())
                        self.puntos.add(punto)
                        self.contador+=1
                    else:
                        self.contador=0
                        puntos=self.puntos.sprites()
                        pygame.draw.circle(self.capa, "green", puntos[0].entregar_posicion(),puntos[0].calcular_distancia(puntos[1]) )
                        self.puntos.empty()


            

    def run(self):
        self.get_input()
        self.interfaz.draw(self.capa)
        self.puntos.draw(self.capa)

        self.cursor.update()
        self.cursor.draw(self.capa)
        
        
    
    
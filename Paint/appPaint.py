import pygame, sys
import ajustes
class AppPaint:
    def __init__(self):
        pygame.init()
        self.pantalla= pygame.display.set_mode((ajustes.ANCHO_PANTALLA, ajustes.ALTO_PANTALLA))
        self.clock = pygame.time.Clock()
        self.activo=True
        
    def correr(self):
        while self.activo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.pantalla.fill('black')

            pygame.display.update()
            self.clock.tick(ajustes.FPS)

if __name__=="__main__":
    j=AppPaint()
    j.correr()
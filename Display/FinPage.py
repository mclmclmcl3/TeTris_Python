import pygame
import sys
from Helpper.ColoresYFuentes import Colores
from Helpper.ColoresYFuentes import Fuentes


class EndGame:
    def __init__(self) -> None:
        pygame.init()
        self.__dimensiones = [700, 500]
        self.__pantalla = pygame.display.set_mode(self.__dimensiones)

    def Juego(self):

        fin = Fuentes.arialblack42().render("FIN DE PARTIDA", True, Colores.rojo())
        instrucicones = Fuentes.arial36().render("Pulsa [space] para finalizar", True, Colores.azul())

        while True:
            self.__pantalla.fill(Colores.blanco())

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        pygame.quit()
                        sys.exit()

            self.__pantalla.blit(fin, (180, 150))
            self.__pantalla.blit(instrucicones, (50, 400))
            pygame.display.update()


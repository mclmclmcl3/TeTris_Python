import os

import pygame
import sys
from Helpper.ColoresYFuentes import Colores
from Helpper.ColoresYFuentes import Fuentes


class QuitarVida:
    ANCHO = 800
    ALTO = 1000

    def __init__(self, jugador) -> None:
        pygame.init()
        self.__pantalla = pygame.display.set_mode((self.ANCHO, self.ALTO))
        self.jugador = jugador

    def resource_path(self, relative_path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def Juego(self):

        vida = Fuentes.arialblack42().render("¡¡¡ Has perdido una vida !!!", True, Colores.rojo())
        tienes = Fuentes.arial36().render(f"Tenias {self.jugador.vidas + 1} vidas", True, Colores.negro())
        te_quedan = Fuentes.arial36().render(f"Te quedan {self.jugador.vidas}", True, Colores.negro())
        instrucicones = Fuentes.arial42().render("Pulsa [space] para continuar", True, Colores.azul())

        archivo = self.resource_path("Resources/pasar pantalla.mp3")
        musica = pygame.mixer.Sound(archivo)
        musica = pygame.mixer.Sound(musica)
        # musica = pygame.mixer.Sound("Resources/perder.mp3")
        musica.set_volume(1)
        musica.play()

        empezar = False
        while not empezar:
            self.__pantalla.fill(Colores.blanco())

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        empezar = True
            vertical = 100
            horizontal = 90
            incremento = 100

            self.__pantalla.blit(vida, (horizontal, vertical))
            self.__pantalla.blit(tienes, (horizontal + 100, vertical + incremento * 3))
            self.__pantalla.blit(te_quedan, (horizontal + 100, vertical + incremento * 3 + 50))
            self.__pantalla.blit(instrucicones, (horizontal, vertical + incremento * 6))

            # marco exterior
            pygame.draw.rect(self.__pantalla,
                             Colores.negro(),
                             (30, 30, 740, 900), 4)

            pygame.display.update()

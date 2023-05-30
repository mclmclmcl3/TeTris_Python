import pygame
import sys
from Helpper.ColoresYFuentes import Colores
from Helpper.ColoresYFuentes import Fuentes


class Instrucciones:
    lineas = ["El juego es como el tetris convencional, pero casero.",
              "Tenemos 10 Niveles que irán incrementandose según vayas avanzando.",
              "El total de las partidas serán 40 para terminar el juego.",
              "La velocidad se irá ajustando según avances, así como en alguna",
              "pantalla apareceran piezas iniciales.",
              "Mandos de juego:",
              "Para ir a la derecha: Flecha DERECHA",
              "Para ir a la izquierda: Flecha IZQUIERDA",
              "Para bajar mas rapido: Flecha ABAJO",
              "Para rotar la pieza: ESPACIO",
              "Para pausar o quitar pausa durante el juego: A"
              ]
    ANCHO = 800
    ALTO = 1000

    def __init__(self) -> None:
        pygame.init()
        self.__pantalla = pygame.display.set_mode((self.ANCHO, self.ALTO))

    def Juego(self):

        titulo = Fuentes.arialblack36().render("Instrucciones para jugar", True, Colores.rojo())
        instrucicones = Fuentes.arial42().render("Pulsa [space] para finalizar", True, Colores.azul())

        seguir = True
        while seguir:
            self.__pantalla.fill(Colores.blanco())

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        seguir = False

            self.__pantalla.blit(titulo, (50, 40))

            horizonal = 100
            for y in range(len(self.lineas)):
                texto = Fuentes.arial24().render(self.lineas[y], True, Colores.negro())
                vertical = 120 + (y * 50)
                if y == 5:
                    vertical += 50
                    texto = Fuentes.arial24().render(self.lineas[y], True, Colores.verdeoscuro())
                if y > 5:
                    vertical += 50
                    horizonal = 150
                    texto = Fuentes.arial24().render(self.lineas[y], True, Colores.verdeoscuro())
                self.__pantalla.blit(texto, (horizonal, vertical))

            self.__pantalla.blit(instrucicones, (80, 800))

            # marco exterior
            pygame.draw.rect(self.__pantalla,
                             Colores.negro(),
                             (30, 30, 740, 900), 4)

            pygame.display.update()

import copy
import os

import pygame
import sys
from Helpper.CoorTableros import PosicicionTablero
from Helpper.ColoresYFuentes import Colores
from Helpper.ColoresYFuentes import Fuentes


class Tetris:
    ANCHO = 800
    ALTO = 1000

    def __init__(self, jugador, tablero):
        pygame.init()
        self.pantalla = pygame.display.set_mode((self.ANCHO, self.ALTO))
        pygame.display.set_caption("TETRIX")

        self.coor_tablero = PosicicionTablero()
        self.jugador = jugador
        self.nivel = tablero.nivel
        self.tablero = tablero

        self.partida_terminada = False
        self.partida_superada = False

    def __del__(self):
        del self.coor_tablero
        del self.tablero
        del self.partida_terminada
        del self.partida_superada

    def pintar_ficha(self):
        for pieza in self.tablero.ficha.lista_cuadrados:
            if pieza.cy >= 0:
                pygame.draw.rect(self.pantalla,
                                 self.tablero.ficha.color,
                                 (self.coor_tablero.tablero_x(pieza.cx),
                                  self.coor_tablero.tablero_y(pieza.cy),
                                  self.coor_tablero.dim_cuadrado - 4,
                                  self.coor_tablero.dim_cuadrado - 4))

    def pintar_ficha_siguiente(self):
        for pieza in self.tablero.duo_ficha[0].lista_cuadrados:
            pygame.draw.rect(self.pantalla,
                             self.tablero.duo_ficha[0].color,
                             (self.coor_tablero.tablero_x(pieza.cx) + 330,
                              self.coor_tablero.tablero_y(pieza.cy) + 150,
                              self.coor_tablero.dim_cuadrado - 4,
                              self.coor_tablero.dim_cuadrado - 4))

    def pintar_tablero(self):
        # delimitador
        pygame.draw.rect(self.pantalla,
                         Colores.negro(),
                         (30, 30, 740, 900), 4)
        # pintamos los cuadrados
        for cuadrados in self.tablero.lista_cuadrados:
            pygame.draw.rect(self.pantalla,
                             Colores.grisclaro(),
                             (self.coor_tablero.tablero_x(cuadrados.cx),
                              self.coor_tablero.tablero_y(cuadrados.cy),
                              self.coor_tablero.dim_cuadrado - 4,
                              self.coor_tablero.dim_cuadrado - 4))

        # pintamos los numeros laterales
        for y in range(21):
            if y != 20:
                if y < 10:
                    mi_texto = Fuentes.arial24().render(f" {y + 1}", 0, Colores.grisoscuro())
                else:
                    mi_texto = Fuentes.arial24().render(f"{y + 1}", 0, Colores.grisoscuro())

                self.pantalla.blit(mi_texto, (
                    self.coor_tablero.offset_x - 30,
                    self.coor_tablero.offset_y - 6 + self.coor_tablero.dim_cuadrado / 2 + (
                            y * self.coor_tablero.dim_cuadrado)))

            for x in range(10):
                pygame.draw.rect(self.pantalla,
                                 Colores.grisoscuro(),
                                 (self.coor_tablero.offset_x,
                                  self.coor_tablero.offset_y,
                                  self.coor_tablero.dim_cuadrado * x,
                                  self.coor_tablero.dim_cuadrado * y),
                                 2)

    def pintar_datos(self):
        vidas = Fuentes.arialblack36().render(f"Vidas: {self.jugador.vidas}", True, Colores.rojo())
        puntos = Fuentes.arialblack24().render(f"Puntos: {self.jugador.puntos}", True, Colores.azul())
        filas_restantes = Fuentes.arialblack24().render(f"Filas restantes: {self.tablero.filas_acabadas}", True,
                                                        Colores.azul())
        nivel = Fuentes.arialblack24().render(f"Nivel: {self.tablero.nivel.nivel}", True, Colores.negro())
        pantalla = Fuentes.arialblack24().render(f"Pantalla: {self.tablero.nivel.pantalla}", True, Colores.negro())

        vertical = 500
        horizontal = 500
        incremento = 50
        self.pantalla.blit(vidas, (horizontal, vertical))
        self.pantalla.blit(puntos, (horizontal, vertical + 3 * incremento))
        self.pantalla.blit(filas_restantes, (horizontal, vertical + 4 * incremento))
        self.pantalla.blit(nivel, (horizontal, vertical + 5 * incremento))
        self.pantalla.blit(pantalla, (horizontal, vertical + 6 * incremento))

    def resource_path(self, relative_path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def juego(self):
        reloj = pygame.time.Clock()
        factor_velocidad = 1
        pausa = False
        contador_bajar_pieza = 0

        # pygame.mixer.music.load("Resources/Tetris.mp3")

        archivo = self.resource_path("Resources/Tetris.mp3")
        pygame.mixer.music.load(archivo)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(100)

        while not self.partida_superada and not self.partida_terminada:
            reloj.tick((self.nivel.velocidad * factor_velocidad) * 2)
            contador_bajar_pieza += 1

            self.pantalla.fill(Colores.blanco())

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:

                    # if evento.key == pygame.K_RIGHT:
                    #     self.tablero.mover_Pieza_Dcha()
                    # if evento.key == pygame.K_LEFT:
                    #     self.tablero.mover_pieza_izq()

                    if evento.key == pygame.K_a:
                        if not pausa:
                            pausa = True
                        else:
                            pausa = False

                    if evento.key == pygame.K_SPACE:
                        self.tablero.rotar_pieza()

                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_DOWN:
                        factor_velocidad = 1

            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_DOWN]:
                factor_velocidad = 30 / self.nivel.velocidad
            if teclas[pygame.K_LEFT]:
                self.tablero.mover_pieza_izq()
            if teclas[pygame.K_RIGHT]:
                self.tablero.mover_Pieza_Dcha()

            if pausa:
                if contador_bajar_pieza % 2 == 0:
                    self.tablero.avance_automatico()

                if self.tablero.muerto:
                    pygame.mixer.music.stop()
                    self.partida_terminada = True

                if self.tablero.pasar_pantalla:
                    pygame.mixer.music.stop()
                    self.partida_superada = True

            self.pintar_tablero()
            self.pintar_ficha()
            self.pintar_ficha_siguiente()
            self.pintar_datos()

            if not pausa:
                msg_pausa = Fuentes.arialblack36().render(f"PULSA ( a ) PARA CONTINUAR...", True, Colores.verdeoscuro())
                self.pantalla.blit(msg_pausa, (80, 40))
            pygame.display.update()

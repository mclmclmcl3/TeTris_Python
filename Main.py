from Negocio.Jugador import Jugador
from Negocio.Niveles import Niveles
from Negocio.Tablero import Tablero
from Display.TetrisPage import Tetris
from Display.CambioPantallaPage import CambioPantalla
from Display.FinPage import EndGame
from Display.InstruccionesPage import Instrucciones
from Display.QuitarVidaPage import QuitarVida


class Inicio:
    def __init__(self):
        # perviven mientras estemos jugando
        self.jugador = Jugador()
        self.niveles = Niveles()

        # creamos instacias de ventanas informativas
        self.page_pasar_pantalla = CambioPantalla(self.niveles)
        self.page_quitar_vida = QuitarVida(self.jugador)

    def inicio_juego(self):
        instrucion = Instrucciones()
        instrucion.Juego()

        # primera partida
        self.niveles.nueva_pantalla()
        tetris = Tetris(self.jugador, Tablero(self.niveles, self.jugador))
        tetris.juego()

        jugando = True
        while jugando:
            if self.jugador.vidas == 0:
                jugando = False

            if tetris.partida_superada:
                self.niveles.nueva_pantalla()
                self.page_pasar_pantalla.Juego()
                tetris = Tetris(self.jugador, Tablero(self.niveles, self.jugador))
                tetris.juego()

            if tetris.partida_terminada:
                self.jugador.vidas -= 1
                self.page_quitar_vida.Juego()

                if self.jugador.vidas == 0:
                    jugando = False
                else:
                    tetris = Tetris(self.jugador, Tablero(self.niveles, self.jugador))
                    tetris.juego()

        final = EndGame()
        final.Juego()



if __name__ == "__main__":
    inicio = Inicio()
    inicio.inicio_juego()

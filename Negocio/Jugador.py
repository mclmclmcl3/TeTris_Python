class Jugador:
    __rango_puntos = []

    def __init__(self):
        self.puntos = 0
        self.__rango_puntos = [x for x in range(20, 0, -1)]
        self.vidas = 3
        self.fin_juego = False
        self.fin_pantalla = False

    def sumar_puntos(self, y, cant=1):
        print(y)
        for valor in y:
            self.puntos += self.__rango_puntos[valor] * cant

    def fin_vidas(self):
        if self.vidas == 0:
            self.fin_juego = True


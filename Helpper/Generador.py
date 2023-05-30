import random
from Models.Fichas import Ficha1
from Models.Fichas import Ficha2
from Models.Fichas import Ficha3
from Models.Fichas import Ficha4
from Models.Fichas import Ficha5
from Models.Fichas import Ficha6
from Models.Fichas import Ficha7


class Generador:
    @staticmethod
    def __generador() -> object:
        while True:
            seleccion = random.randint(0, 6)
            if seleccion == 0:
                yield Ficha1(4, -1)
            if seleccion == 1:
                yield Ficha2(4, -1)
            if seleccion == 2:
                yield Ficha3(4, -1)
            if seleccion == 3:
                yield Ficha4(4, -1)
            if seleccion == 4:
                yield Ficha5(4, -1)
            if seleccion == 5:
                yield Ficha6(4, -1)
            if seleccion == 6:
                yield Ficha7(4, -1)

    def enviar_pieza(self, lista_duo: list) -> list:
        while len(lista_duo) < 2:
            gen = self.__generador()
            lista_duo.append(next(gen))
        return lista_duo

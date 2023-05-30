from Models.IFichas import IFichas
from Helpper.ColoresYFuentes import Colores


class Ficha1(IFichas):
    def __init__(self, cx, cy):
        super().__init__(cx, cy)
        self.lista_cuadrados = []
        self.posicion = 1
        self.construir()
        self.color = Colores.naranja()

    # xxxx

    def grados_0(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy - 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx, self.cy + 1),
            IFichas(self.cx, self.cy + 2)]

    def grados_90(self):
        self.lista_cuadrados = [
            IFichas(self.cx - 1, self.cy),
            IFichas(self.cx, self.cy),
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx + 2, self.cy)]

    def grados_180(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy - 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx, self.cy + 1),
            IFichas(self.cx, self.cy + 2)]

    def grados_270(self):
        self.lista_cuadrados = [
            IFichas(self.cx - 1, self.cy),
            IFichas(self.cx, self.cy),
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx + 2, self.cy)]


class Ficha2(IFichas):
    def __init__(self, cx, cy):
        super().__init__(cx, cy)
        self.lista_cuadrados = []
        self.posicion = 1
        self.construir()
        self.color = Colores.rojo()

    #  x
    # xxx
    def grados_0(self):
        self.lista_cuadrados = [
            IFichas(self.cx - 1, self.cy),
            IFichas(self.cx, self.cy),
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx, self.cy - 1)]

    def grados_90(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy - 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx, self.cy + 1),
            IFichas(self.cx - 1, self.cy)]

    def grados_180(self):
        self.lista_cuadrados = [
            IFichas(self.cx - 1, self.cy),
            IFichas(self.cx, self.cy),
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx, self.cy + 1)]

    def grados_270(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy - 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx, self.cy + 1),
            IFichas(self.cx + 1, self.cy)]


class Ficha3(IFichas):
    def __init__(self, cx, cy):
        super().__init__(cx, cy)
        self.lista_cuadrados = []
        self.posicion = 1
        self.construir()
        self.color = Colores.cyan()

    #  xx
    # xx
    def grados_0(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy + 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx - 1, self.cy + 1)]

    def grados_90(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy - 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx + 1, self.cy + 1)]

    def grados_180(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy + 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx - 1, self.cy + 1)]

    def grados_270(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy - 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx + 1, self.cy + 1)]


class Ficha4(IFichas):
    def __init__(self, cx, cy):
        super().__init__(cx, cy)
        self.lista_cuadrados = []
        self.posicion = 1
        self.construir()
        self.color = Colores.morado()

    # xxx
    # x
    def grados_0(self):
        self.lista_cuadrados = [
            IFichas(self.cx - 1, self.cy),
            IFichas(self.cx, self.cy),
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx + 1, self.cy - 1)]

    def grados_90(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy + 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx, self.cy - 1),
            IFichas(self.cx - 1, self.cy - 1)]

    def grados_180(self):
        self.lista_cuadrados = [
            IFichas(self.cx - 1, self.cy + 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx - 1, self.cy),
            IFichas(self.cx + 1, self.cy)]

    def grados_270(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy + 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx, self.cy - 1),
            IFichas(self.cx + 1, self.cy + 1)]


class Ficha5(IFichas):
    def __init__(self, cx, cy):
        super().__init__(cx, cy)
        self.lista_cuadrados = []
        self.posicion = 1
        self.construir()
        self.color = Colores.azul()

    # xxx
    #   x
    def grados_0(self):
        self.lista_cuadrados = [
            IFichas(self.cx - 1, self.cy),
            IFichas(self.cx, self.cy),
            IFichas(self.cx - 1, self.cy - 1),
            IFichas(self.cx + 1, self.cy)]

    def grados_90(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy - 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx, self.cy + 1),
            IFichas(self.cx - 1, self.cy + 1)]

    def grados_180(self):
        self.lista_cuadrados = [
            IFichas(self.cx - 1, self.cy),
            IFichas(self.cx, self.cy),
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx + 1, self.cy + 1)]

    def grados_270(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy + 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx, self.cy - 1),
            IFichas(self.cx + 1, self.cy - 1)]


class Ficha6(IFichas):
    def __init__(self, cx, cy):
        super().__init__(cx, cy)
        self.lista_cuadrados = []
        self.posicion = 1
        self.construir()
        self.color = Colores.grisoscuro()

    # xx
    # xx
    def grados_0(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy + 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx + 1, self.cy + 1)]

    def grados_90(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy + 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx + 1, self.cy + 1)]

    def grados_180(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy + 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx + 1, self.cy + 1)]

    def grados_270(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy + 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx + 1, self.cy + 1)]


class Ficha7(IFichas):
    def __init__(self, cx, cy):
        super().__init__(cx, cy)
        self.lista_cuadrados = []
        self.posicion = 1
        self.construir()
        self.color = Colores.morado()

    #  x
    #  xx
    #   x
    def grados_0(self):
        self.lista_cuadrados = [
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx, self.cy),
            IFichas(self.cx, self.cy - 1),
            IFichas(self.cx - 1, self.cy - 1)]

    def grados_90(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy - 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx - 1, self.cy),
            IFichas(self.cx - 1, self.cy + 1)]

    def grados_180(self):
        self.lista_cuadrados = [
            IFichas(self.cx + 1, self.cy),
            IFichas(self.cx, self.cy),
            IFichas(self.cx, self.cy - 1),
            IFichas(self.cx - 1, self.cy - 1)]

    def grados_270(self):
        self.lista_cuadrados = [
            IFichas(self.cx, self.cy - 1),
            IFichas(self.cx, self.cy),
            IFichas(self.cx - 1, self.cy),
            IFichas(self.cx - 1, self.cy + 1)]

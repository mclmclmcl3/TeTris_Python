from Models.Base import Base


class IFichas(Base):
    def __init__(self, cx, cy):
        super().__init__(cx, cy)
        self.lista_cuadrados = []
        self.posicion = 1
        self.color = None

    def construir(self):
        if self.posicion == 1:
            self.grados_0()
        elif self.posicion == 2:
            self.grados_90()
        elif self.posicion == 3:
            self.grados_180()
        elif self.posicion == 4:
            self.grados_270()

    def grados_0(self):
        pass

    def grados_90(self):
        pass

    def grados_180(self):
        pass

    def grados_270(self):
        pass

    def avanzar(self):
        self.cy += 1
        self.construir()

    def dcha(self):
        self.cx += 1
        self.construir()

    def izq(self):
        self.cx -= 1
        self.construir()

    def rotar(self):
        self.posicion += 1
        if self.posicion == 5:
            self.posicion = 1
        self.construir()

    def rotar_invertido(self):
        self.posicion -= 1
        if self.posicion == 0:
            self.posicion = 4
        self.construir()

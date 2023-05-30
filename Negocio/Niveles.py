class Niveles:

    def __init__(self):
        self.nivel = 1
        self.pantalla = 0
        self.velocidad = 1
        self.bloques_iniciales = 0
        self.bloques_a_terminar = 10

    def __subir_nivel(self):
        self.nivel += 1

    def nueva_pantalla(self):
        self.pantalla += 1

        if self.pantalla % 4 == 0:
            self.__subir_nivel()

        self.velocidad = round(self.pantalla / 10) + 3

        if self.pantalla % 3 == 0:
            valor = round(self.pantalla / 3)
            if valor <= 2:
                valor = 3
            if valor > 8:
                valor = 8
            self.bloques_iniciales = valor
        else:
            self.bloques_iniciales = 0

        if self.pantalla % 10 == 0:
            self.bloques_a_terminar += round((self.pantalla + self.nivel) / 4)



import random

from Helpper.Generador import Generador
from Models.Base import Base


class Tablero:
    def __init__(self, nivel, jugador):
        self.nivel = nivel
        self.filas_acabadas = self.nivel.bloques_a_terminar
        self.lista_cuadrados = []
        self.muerto = False
        self.pasar_pantalla = False
        self.jugador = jugador

        self.ficha = None
        self.generador = Generador()
        self.duo_ficha = []

        self.__insertar_pieza()

    def __del__(self):
        self.lista_cuadrados = []
        self.fichas_aleatorias = []
        del self.ficha
        del self.filas_acabadas
        del self.muerto
        del self.pasar_pantalla

    def __insertar_pieza(self):
        if self.ficha is None:
            mi_duo = self.generador.enviar_pieza(self.duo_ficha)
            self.ficha = mi_duo.pop(0)

    def avance_automatico(self):
        if self.nivel.bloques_iniciales > 0:
            self.__bloques_iniciales()

        if self.filas_acabadas < 1:
            self.pasar_pantalla = True

        self.__borrar_fila_terminada()
        self.vida_terminada()

        if self.ficha is not None:
            if not self.__colisiones_pieza_en_avance() and not self.__salir_pantalla():
                self.ficha.avanzar()
            else:
                self.__explosiona_figura()
        else:
            self.__insertar_pieza()

    def __bloques_iniciales(self):
        fila = 20
        for f in range(self.nivel.bloques_iniciales):
            fila -= 1
            for columnas in range(9):
                pongo = random.randint(0, 2)
                if pongo == 1:
                    print(f"Pongo: {pongo} => {columnas}:{fila}")
                    cuadrado = Base(columnas, fila)
                    self.lista_cuadrados.append(cuadrado)
        self.nivel.bloques_iniciales = 0
        print(self.nivel.bloques_iniciales == 0)

    def vida_terminada(self):
        for pieza in self.lista_cuadrados:
            if pieza.cy == 0:
                self.muerto = True

    def __salir_pantalla(self) -> bool:
        maximo = max(self.ficha.lista_cuadrados[0].cy,
                     self.ficha.lista_cuadrados[1].cy,
                     self.ficha.lista_cuadrados[2].cy,
                     self.ficha.lista_cuadrados[3].cy)
        if maximo <= 18:
            return False
        else:
            return True

    def __colisiones_pieza_en_avance(self) -> bool:
        if len(self.lista_cuadrados) > 0:
            for cuadrado in self.lista_cuadrados:
                for pieza in self.ficha.lista_cuadrados:
                    if cuadrado.cx == pieza.cx and cuadrado.cy == pieza.cy + 1:
                        return True
        return False

    def __colisiones_cuadrado(self, cuad) -> bool:
        for cuadrado in self.lista_cuadrados:
            if cuadrado.cx == cuad.cx and cuadrado.cy == cuad.cy + 1:
                return True
        return False

    def __explosiona_figura(self):
        for ficha in self.ficha.lista_cuadrados:
            self.lista_cuadrados.append(ficha)

        self.ficha = None
        self.__insertar_pieza()

    def __borrar_fila_terminada(self):
        if len(self.__filas_llenas_ordenadas()) > 0:
            self.jugador.sumar_puntos(self.__filas_llenas_ordenadas(), len(self.__filas_llenas_ordenadas()))
            for fila in self.__filas_llenas_ordenadas():
                lista_aux = self.lista_cuadrados[:]
                for cuadrado in lista_aux:
                    if cuadrado.cy == fila:
                        self.lista_cuadrados.remove(cuadrado)

                self.filas_acabadas -= 1
                self.__reajustar_cuadrados(fila)

    def __filas_llenas_ordenadas(self) -> list:
        # creo lista para rellenar con los índices
        total_filas = [0 for x in range(21)]
        # busco todos los cuadrados por fila comparandolo con la cy y los añado a la lista provisinal total_filas
        for cuadrado in self.lista_cuadrados:
            total_filas[cuadrado.cy] = total_filas[cuadrado.cy] + 1
        # si la busqueda anterior es = 9, o sea, esta llena, se introduce el índice en lista[]
        lista = []
        for x in range(len(total_filas)):
            if total_filas[x] == 9:
                lista.append(x)
        # devuelvo una lista de índices de filas completadas
        return list(set(lista))

    def __reajustar_cuadrados(self, fila):
        for cuadrado in self.lista_cuadrados:
            if cuadrado.cy == fila and fila != 19:
                if not self.__colisiones_cuadrado(cuadrado):
                    cuadrado.cy += 1
        if fila > 0:
            self.__borrar_fila_terminada()  # prueba
            self.__reajustar_cuadrados(fila - 1)
        else:
            self.__borrar_fila_terminada()

    def mover_Pieza_Dcha(self):
        maximo = max(self.ficha.lista_cuadrados[0].cx,
                     self.ficha.lista_cuadrados[1].cx,
                     self.ficha.lista_cuadrados[2].cx,
                     self.ficha.lista_cuadrados[3].cx)

        if maximo < 8:
            self.ficha.dcha()

        if self.colision_pos_actual():
            self.ficha.izq()

    def mover_pieza_izq(self):
        minimo = min(self.ficha.lista_cuadrados[0].cx,
                     self.ficha.lista_cuadrados[1].cx,
                     self.ficha.lista_cuadrados[2].cx,
                     self.ficha.lista_cuadrados[3].cx)
        if minimo > 0:
            self.ficha.izq()

        if self.colision_pos_actual():
            self.ficha.dcha()

    def rotar_pieza(self):
        self.ficha.rotar()

        maximo_x = max(self.ficha.lista_cuadrados[0].cx,
                       self.ficha.lista_cuadrados[1].cx,
                       self.ficha.lista_cuadrados[2].cx,
                       self.ficha.lista_cuadrados[3].cx)

        minimo_x = min(self.ficha.lista_cuadrados[0].cx,
                       self.ficha.lista_cuadrados[1].cx,
                       self.ficha.lista_cuadrados[2].cx,
                       self.ficha.lista_cuadrados[3].cx)

        if maximo_x > 8 or minimo_x < 0:
            self.ficha.rotar_invertido()

        if self.colision_pos_actual():
            self.ficha.rotar_invertido()

    def colision_pos_actual(self) -> bool:
        if len(self.lista_cuadrados) > 0:
            for cuadrado in self.lista_cuadrados:
                for pieza in self.ficha.lista_cuadrados:
                    if cuadrado.cx == pieza.cx and cuadrado.cy == pieza.cy:
                        return True
        return False

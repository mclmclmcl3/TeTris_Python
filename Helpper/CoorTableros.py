class PosicicionTablero:
    def __init__(self):
        self.offset_x = 100
        self.offset_y = 100
        self.dim_cuadrado = 40

    def tablero_x(self, coor_x) -> int:
        return self.offset_x + (coor_x * self.dim_cuadrado) + 1

    def tablero_y(self, coor_y) -> int:
        return self.offset_y + (coor_y * self.dim_cuadrado) + 1

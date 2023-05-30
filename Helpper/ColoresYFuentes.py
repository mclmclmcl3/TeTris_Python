import pygame


class Colores:
    @staticmethod
    def blanco() -> pygame.color:
        return pygame.color.Color(255, 255, 255)

    @staticmethod
    def negro() -> pygame.color:
        return pygame.color.Color(0, 0, 0)

    @staticmethod
    def rojo() -> pygame.color:
        return pygame.color.Color(255, 0, 0)

    @staticmethod
    def verde() -> pygame.color:
        return pygame.color.Color(0, 255, 0)

    @staticmethod
    def verdeoscuro() -> pygame.color:
        return pygame.color.Color(0, 150, 0)

    @staticmethod
    def azul() -> pygame.color:
        return pygame.color.Color(0, 0, 255)

    @staticmethod
    def grisclaro() -> pygame.color:
        return pygame.color.Color(200, 200, 200)

    @staticmethod
    def grisoscuro() -> pygame.color:
        return pygame.color.Color(100, 100, 100)

    @staticmethod
    def cyan() -> pygame.color:
        return pygame.color.Color(70, 180, 170)

    @staticmethod
    def morado() -> pygame.color:
        return pygame.color.Color(180, 70, 170)

    @staticmethod
    def naranja() -> pygame.color:
        return pygame.color.Color(215, 130, 50)


class Fuentes:
    @staticmethod
    def normal30():
        return pygame.font.Font(None, 30)

    @staticmethod
    def normal42():
        return pygame.font.Font(None, 42)

    @staticmethod
    def arialblack42():
        return pygame.font.SysFont("Arial Black", 42)

    @staticmethod
    def arialblack36():
        return pygame.font.SysFont("Arial Black", 36)

    @staticmethod
    def arialblack24():
        return pygame.font.SysFont("Arial Black", 24)

    @staticmethod
    def arialblack16():
        return pygame.font.SysFont("Arial Black", 16)

    @staticmethod
    def arial42():
        return pygame.font.SysFont("Arial", 42)

    @staticmethod
    def arial36():
        return pygame.font.SysFont("Arial", 36)

    @staticmethod
    def arial24():
        return pygame.font.SysFont("Arial", 24)

    @staticmethod
    def arial16():
        return pygame.font.SysFont("Arial", 16)

    @staticmethod
    def calibri24():
        return pygame.font.SysFont("Calibri", 24)

    @staticmethod
    def calibri14():
        return pygame.font.SysFont("Calibri", 14)

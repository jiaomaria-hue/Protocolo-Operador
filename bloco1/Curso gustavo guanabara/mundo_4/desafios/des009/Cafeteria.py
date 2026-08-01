from rich import inspect
from abc import ABC, abstractmethod
class Bebidaquente(ABC):
    def preparar(self):
        print('---- Iniciando o Preparo ----')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('---- Bebida Pronta ----\n')

    def ferver_agua(self):
        print('1. Fervendo água a 100 graus Celsius.')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(Bebidaquente):
    def misturar(self):
        print('2. Passando água pressurizada pelo pó de cafe moido')

    def servir(self):
        print('3. Servindo em xicara pequena')


class Cha(Bebidaquente):
    def misturar(self):
        print('2. Mergulhando o sachẽ de ervas na agua. ')

    def servir(self):
        print('3. Servindo na canelca de porcelana com limão. ')


class Leite(Bebidaquente):
    def misturar(self):
        print('2. Passando agua pressurizada pela chaleira do leite')

    def servir(self):
        print('3. Servindo na caneca grande, ja com cafe.')

from abc import ABC, abstractmethod
import random
from rich import print
class Personagem(ABC):
    def __init__(self, nome='', vida=0):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca=50):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(F'[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com um [blue]{golpe}[/], de força {forca}')
            alvo.receber_dano(forca)
        else:
            print(F'O ataque {self.nome} -> {alvo.nome} não pode acontecer')


    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida = self.vida - fator
        if self.vida < 0:
            self.vida = 0
        print(f'[blue]{self.nome}[/] recebey o [red]dano de {fator}[/]!')

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome='', vida=0):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Golpe de machado', 'Pulo giratorio']

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'[blue]O guerreiro {self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {fator} pontos[/] de vida')



class Mago(Personagem):
    def __init__(self, nome='', vida=0):
        super().__init__(nome, vida)
        self.golpes = ['Bola de fogo', 'Rajada de gelo', 'Barragem de água']


    def curar(self):
        fator = random.randint(0, 100)
        print(f'[blue]O mago {self.nome}[/] [green]recuperou {fator} pontos[/] de vida com seu feitiço de cura')




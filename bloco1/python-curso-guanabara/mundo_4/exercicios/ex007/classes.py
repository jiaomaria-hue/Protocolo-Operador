from rich import print
from abc import ABC, abstractmethod #abstravt base methods
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'[yellow]O professor [red]{self.nome}[/], começou a dar aula[/]')

    def estudar(self):
            print(f'[green]O Professor [red]{self.nome}[/], Começou a estudar a materia que vai apresentar na sala de aula na especialidade de {self.especialidade} no nivel de {self.nivel}.[/]')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'[blue]o funcionario(a) [red]{self.nome}[/], acabou de bater ponto[/]')

    def estudar(self):
            print(f'[red]o Funcionario [black]{self.nome}[/] começou a estudar sobre a função dele de {self.cargo} no setor de {self.setor}[/]')

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'[green]O aluno [red]{self.nome}[/], acabou de fazer matricula[/]')

    def estudar(self):
            print(f'[red]o Aluno [green]{self.nome}[/], acabou de estudar sobre a materia de estudos na turma {self.turma} no curso de {self.curso}[/]')
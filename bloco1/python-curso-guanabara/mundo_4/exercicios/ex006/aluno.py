from rich import print
from pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'[green]O aluno [red]{self.nome}[/], acabou de fazer matricula[/]')
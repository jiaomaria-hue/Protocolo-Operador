from rich import print
class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def aprensentacao(self):
        return f':waving_hand: Olá, sou [blue]{self.nome}[/] e sou do cargo de [red]{self.cargo}[/] na empresa do Curso em video, e sou do setor de [green]{self.setor}[/]'
c1 = Funcionario('joao', 'Diretoria', 'Cybersecurity')
print(c1.aprensentacao())

c2 = Funcionario('Arthur', 'Diretoria', 'Dev/cyber')
print(c2.aprensentacao())
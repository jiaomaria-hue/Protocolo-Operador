from classesex005 import Aluno, Professor, Funcionario
from rich import inspect, print
a1 = Aluno('jose', 17,'informatica', 'T01')
a1.fazer_aniversario()
a1.fazer_matricula()

p1 = Professor('Samuel', 37, 'biologia', 'Mestrado')
p1.dar_aula()

f1 = Funcionario('Joao', 24, 'Cybersecurity senior', 'TI')
f1.bater_ponto()
f1.fazer_aniversario()
# inspect(f1, methods=True)
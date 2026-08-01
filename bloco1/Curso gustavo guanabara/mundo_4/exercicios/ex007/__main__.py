from classes import Professor, Funcionario, Aluno
from rich import inspect, print
def main():
    a1 = Aluno('jose', 17,'informatica', 'T01')
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor('Samuel', 37, 'biologia', 'Mestrado')
    p1.dar_aula()

    f1 = Funcionario('Joao', 24, 'Cybersecurity senior', 'TI')
    f1.bater_ponto()
    f1.fazer_aniversario()

    a1.estudar()
    print('')
    p1.estudar()
    print('')
    f1.estudar()

if __name__ == '__main__':
    main()
from Funcionarios_salar import *

def main():
    # Instanciando Paulo (Horista: R$15/hora * 160h = R$2400 bruto -> -7.5% INSS = R$2220.00)
    f1 = FuncionarioHorista(nome="Paulo", valor_hora=15.0, horas_trab=160)
    f1.calcular_salario()
    f1.analisar_salario()

    # Instanciando Amanda (Mensalista: R$9500 bruto -> -7.5% INSS = R$8787.50)
    f2 = FuncionarioMensalista(nome="Amanda", sal_bruto=9500.0)
    f2.calcular_salario()
    f2.analisar_salario()


if __name__ == "__main__":
    main()
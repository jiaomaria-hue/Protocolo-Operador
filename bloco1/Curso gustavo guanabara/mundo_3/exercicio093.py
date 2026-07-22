from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['Contrataçao'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('salario: R$'))
    dados['Aposentadoria'] = (dados['idade'] + (dados['Contrataçao'] + 35) - datetime.now().year)
print('-' * 35)
for k, v in dados.items():
    print(F'- {k} tem o valor {v}')
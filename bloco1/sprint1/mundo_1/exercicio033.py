# Entrada de dados
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

# --- Lógica para o MAIOR ---
maior = n1

if n2 > maior:
    maior = n2

if n3 > maior:
    maior = n3

# --- Lógica para o MENOR ---
menor = n1

if n2 < menor:
    menor = n2

if n3 < menor:
    menor = n3

# Saída única com o resultado final
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
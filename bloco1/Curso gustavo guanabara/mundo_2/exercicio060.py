import os

# Função para limpar o terminal
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicialização das variáveis
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
opcao = 0

while opcao != 5:
    limpar() # Limpa a tela antes de mostrar o menu
    print('''
    --- PROTOCOLO OPERADOR ---
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')

    try:
        opcao = int(input('Qual a sua opção? '))
    except ValueError:
        print('Erro: Digite apenas números inteiros!')
        input("\nPressione Enter para continuar...")
        continue # Volta para o início do while

    if opcao == 1:
        print(f'A soma é {n1 + n2}')
        input("\nPressione Enter para continuar...")
    elif opcao == 2:
        print(f'O produto é {n1 * n2}')
        input("\nPressione Enter para continuar...")
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior é o número {n1}')
        elif n2 > n1:
            print(f'O número maior é o {n2}')
        else:
            print('Os dois são iguais.')
        input("\nPressione Enter para continuar...")
    elif opcao == 4:
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
    elif opcao == 5:
        print('Finalizando o servidor Cybersecurity.')
    else:
        print('Opção inválida!')
        input("\nPressione Enter para continuar...")

print('Servidor fechado.')
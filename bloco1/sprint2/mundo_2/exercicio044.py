preco = float(input('Preço do produto: R$ '))
print('Formas de pagamento:\n1: À vista (dinheiro/cheque)\n2: À vista (cartão)\n3: Até 2x no cartão\n4: 3x ou mais no cartão')
opcao = int(input('Qual a opção? '))

if opcao == 1:
    total = preco * 0.90  # 10% de desconto
elif opcao == 2:
    total = preco * 0.95  # 5% de desconto
elif opcao == 3:
    total = preco  # Preço normal
elif opcao == 4:
    total = preco * 1.20  # 20% de juros
else:
    print('Opção inválida!')
    total = preco

print(f'O preço final é R$ {total:.2f}')
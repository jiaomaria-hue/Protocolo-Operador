try:
    # Tudo o que está aqui dentro deve ter um recuo de 4 espaços
    nasc = int(input('Qual o seu ano de nascimento? '))
    idade = 2026 - nasc
    serv_militar = 18
    # ... resto do seu código com recuo ...
except ValueError:
    # Este print também precisa de recuo de 4 espaços
    print('Erro: voce nao digitou um numero.')
if serv_militar > idade:
    print('voce esta muito velho')
elif idade > serv_militar:
    print('voce ainda vai se alistar')
if serv_militar == idade:
    print('Esta na hora de se alistar.')
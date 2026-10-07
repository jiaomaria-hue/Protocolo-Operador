def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Voce tem {idade} anos, Voto opcional'
    else:
        return f'Com {idade} anos, Voce é obrigatorio a VOTAR'
# programa principal
ano = int(input('Em que ano voce nasceu? '))
print(voto(ano))
    
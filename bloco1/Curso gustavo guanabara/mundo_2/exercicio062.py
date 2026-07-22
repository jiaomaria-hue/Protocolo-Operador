
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    cont += 1
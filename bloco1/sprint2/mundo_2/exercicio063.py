
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

termo = primeiro
cont = 1
mais = 10
total = 10

while mais != 0:
        while cont <= total:
            print(f'{termo} -> ', end='')
            termo = termo + razao
            cont += 1
        mais = int(input('Quantos termos a mais? '))
        total += mais
    

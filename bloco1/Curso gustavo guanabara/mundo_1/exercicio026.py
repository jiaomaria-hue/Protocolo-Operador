A = input('digite uma frase: ').strip().lower()
print(f'A letra "A" aparece {A.count("a")} vezes.')
print(f'a letra A apareceu na posiçao {A.find('a') + 1}.')
print(f'a ultima letra a apareceu na posiçao {A.rfind('a')} + 1.')
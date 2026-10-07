sexo = str(input('Digite seu sexo(M/F): ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Porfavor digite um sexo valido: ')).strip().upper()[0]
else:
    print(f'sexo {sexo} cadastrado.')
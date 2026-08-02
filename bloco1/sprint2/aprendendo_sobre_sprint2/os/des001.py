import os
from rich import print
tot_byte = 0
tot_byte_pasta = 0
print('-' * 30)
resultado = '/home/joao/Documentos/Protocolo-Operador/bloco1/sprint1/projetos_proprios'
print(os.listdir(resultado))
print('-' * 30)
for item in os.listdir('/home/joao/Documentos/Protocolo-Operador/bloco1/sprint1/projetos_proprios'):
    caminho = os.path.join(resultado, item)
    if os.path.isfile(caminho):
        tot_byte += os.path.getsize(caminho)
        print(f'[red]{item}[/] é um arquivo')
    else:                         # senão é pasta
        tot_byte_pasta += os.path.getsize(caminho)
        print(f'[blue]{item}[/] é uma pasta')

print(f'Total pastas: {tot_byte_pasta} bytes')
print(f'\nTotal arquivos: {tot_byte} bytes')



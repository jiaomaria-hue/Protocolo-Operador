import os
caminho = '/home/joao/Documentos/Protocolo-Operador/bloco1/sprint2/aprendendo_sobre_sprint2/os/denunciar'
if os.path.exists(caminho):
    print('Ja existe')
else:
    os.makedirs(caminho)
    print(f'Pasta {caminho} criada com sucesso.')
from rich import print
from datetime import datetime
import os

os.makedirs('reports', exist_ok=True)

def salvar_log(alvo, portas_abertas, tipo='TCP'):
    data = datetime.now().strftime('%d/%m/%Y %H:%M')
    arquivo = f'reports/log_{alvo}_{tipo}.txt'

    with open(arquivo, 'a') as f:
        f.write(f'{'='*40}\n')
        f.write(f'Data: {data}\n')
        f.write(f'Alvo: {alvo}\n')
        f.write(f'Tipo: {tipo}\n')
        f.write(f'Portas abertas: {portas_abertas}\n')
    print(f'[green]Log salvo em {arquivo}[/]')
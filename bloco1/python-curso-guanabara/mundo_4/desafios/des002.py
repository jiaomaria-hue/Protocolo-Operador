from rich import print
from rich.panel import Panel


class Produto:

  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

  def etiqueta(self):
    conteudo = f'{self.nome.center(30, ' ')}'
    conteudo += f'{'-' * 30}'
    precof = f'R${self.preco:,.2f}'
    conteudo += f'{precof.center(30, '-')}'
    etiqueta = Panel(conteudo, title='Produto', width=34)
    print(etiqueta)


# Exemplo de uso:
p1 = Produto("iPhone 17 Pro Max", 25000.85)
p1.etiqueta()

p2 = Produto('MOuse', 120.00)
p2.etiqueta()
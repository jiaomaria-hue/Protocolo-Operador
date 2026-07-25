from rich import print
from rich.panel import Panel
class Churrasco:
    def __init__(self, titulo='', quant=0):
        self.titulo = titulo
        self.quant = quant
    def analisar(self):
        Panel('[white]Esse aqui e um painel de exemplo'
        'ola[/]:+1:', title='Mensagem', style='red')
c = Churrasco('Churrasco em familia', 15)
c.analisar()
print(c.analisar())
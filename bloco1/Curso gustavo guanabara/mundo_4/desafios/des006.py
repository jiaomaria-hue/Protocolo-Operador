from rich import print

class Caneta:

    def __init__(self, cor='azul'):
        escolha = ''
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case 'laranja':
                escolha = '[orange]'
            case 'amarelo':
                escolha = '[yellow]'
            case 'verde':
                escolha = '[green]'
            case _:
                escolha = '[white]'
        self.cor = escolha
        self.tampada = True

    def quebrar_linha(self, qtd = 1):
        print('\n' * qtd, end='')

    def tampar(self):
        self.tampada = True
        return "Caneta Tampada"
    
    def destampar(self):
        self.tampada = False
        return "Caneta destampada"

    def escrever(self, texto):
        if self.tampada:
            print(f':prohibited: A {self.cor}caneta[/] esta tampada')
        else:
            print(f'{self.cor}{texto}[/]', end='')
c2 = Caneta( cor="vermelho")
c3 = Caneta(cor= 'azul')
c4 = Caneta(cor= 'verde')
c2.destampar()
c3.destampar()
c3.destampar()

c2.escrever("Atenção: Erro crítico no sistema!")
c3.escrever('ola mundinho')
c3.quebrar_linha(2)
c4.escrever('hellow')
c4.quebrar_linha(5)

c2.tampar()
c2.escrever('Sera que rola?')
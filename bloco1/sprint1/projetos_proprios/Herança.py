from rich import inspect, print
class Scanner:
    def __init__(self,alvo, porta):
        self.alvo = alvo
        self.porta = porta

    def conectar(self):
        return f'[green][+] Voce esta conectado ao alvo {self.alvo} : {self.porta}[/]'

class PortScanner(Scanner):
    def __init__(self, alvo, porta, protocolo):
        super().__init__(alvo, porta)
        self.protocolo = protocolo

    def executar(self):
        return f'[green][+] Voce esta escaneando o protocolo {self.protocolo} do alvo {self.alvo} na porta {self.porta}[/]'

class WebScanner(Scanner):
    def __init__(self, alvo, porta, caminho):
        super().__init__(alvo, porta)
        self.caminho = caminho

    def executar(self):
        return f'[green][+] Voce esta escaneando o caminho {self.caminho}, no alvo {self.alvo}, na porta {self.porta}[/]'

a1 = Scanner('Google',1045)
print(a1.conectar())

p1 = PortScanner('Google', 1045, 'UDP')
print(p1.executar())

w1 = WebScanner('Google', '1045', '/admin')
print(w1.executar())
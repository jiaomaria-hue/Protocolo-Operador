from rich import print

class Caneta:
    CORES = {
        "azul": "blue",
        "vermelho": "red",
        "verde": "green"
    }

    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor.lower()
        self.tampada = True

    def tampar(self):
        self.tampada = True
        return "Caneta Tampada"
    
    def destampar(self):
        self.tampada = False
        return "Caneta destampada"

    def escrever(self, texto):
        if self.tampada:
            return f"Erro: A caneta {self.modelo} está tampada! Não é possível escrever."
        else:
            cor_rich = self.CORES.get(self.cor, "white")
            
            print(f"[{cor_rich}]{texto}[/{cor_rich}]")

c2 = Caneta(modelo="Faber-Castell", cor="vermelho")
c2.destampar()
c2.escrever("Atenção: Erro crítico no sistema!")
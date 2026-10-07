class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use:
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, n='vazio', i=0):
        # Atributos de instância
        self.nome = n
        self.idade = i

    # Métodos de instância
    def aniversario(self):
        self.idade = self.idade + 1
    
    def mensagem(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade'

# Declaração de objetos
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto('Mauro', 53)
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())
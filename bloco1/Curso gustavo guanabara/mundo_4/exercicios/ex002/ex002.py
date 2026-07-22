    # declaraçao de classe
class Gafanhoto:
    def __init__(self, n='vazio', i=0):
        """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade
    
    Para criar uma nova pessoa, ue:
    variavel = gafanhoto(nome, idade)
        """
        #metodo contrutor
        # atributos de instacians
        self.nome = n
        self.idade = i
    #metodos de instancias
    def aniversario(self):
        self.idade = self.idade + 1
    
    def mensagem(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade'
    #declaraço de objetos
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto('Mauro', 53)
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())
    # declaraçao de classe
class Gafanhoto:
    def __init__(self): #metodo contrutor
        # atributos de instacians
        self.nome = ''
        self.idade = 0
    #metodos de instancias
    def aniversario(self):
        self.idade = self.idade + 1
    
    def mensagem(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade'
    #declaraço de objetos
g1 = Gafanhoto()
g1.nome = 'maria'
g1.idade = 22
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'mauro'
g2.idade = 53
g2.aniversario()
print(g2.mensagem())
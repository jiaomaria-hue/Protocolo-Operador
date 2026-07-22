    # declaraçao de classe
class Gafanhoto:
        """
        Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade
    
        Para criar uma nova pessoa, ue:
        variavel = gafanhoto(nome, idade)
        """
        def __init__(self, n='vazio', i=0):
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
print(g1.__doc__)
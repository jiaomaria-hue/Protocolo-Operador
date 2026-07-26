class ContaBancaria:
    '''
Cria uma conta bancaria e deixa possivel fazer saques e depositos
    '''
    def __init__(self, id, nome, saldo_inicial=0):
        self._saldo = saldo_inicial
        self.id = id
        self. nome =nome
        print(f'Conta {self.id} criada com sucesso. Saldo atual de {self._saldo:,.2f}')

    def __str__(self):
        return f'A conta {self.id} de {self.nome} tem R${self._saldo:.2f} de saldo'

    def depositar(self, valor):
        if valor < 0:
            print('Nao posso fazer isso')
        else:
            self._saldo += valor
            print(f'Ok vou depositar o valor de R${valor:,.2f} na conta {self.id}')


    def sacar(self, valor):
        if valor <= 0:
            print('Valor invalido')
        elif valor > self._saldo:
            print(f'Saldo insuficiente na conta {self.id}')
        else:
            self._saldo -= valor
            print(f'Vou deixar voce sacar o valor de R${valor:,.2f} autorizado na conta {self.id}')

    def ver_saldo(self):
        print(f'o seu saldo atual é {self._saldo}')

conta = ContaBancaria(112, 'gustavo', 1500)
conta.depositar(500)
conta.sacar(300)
print(conta)
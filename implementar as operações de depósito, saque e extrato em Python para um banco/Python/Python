class Conta:
    def __init__(self, numero, saldo_inicial=0):
        self.numero = numero
        self.saldo = saldo_inicial
        self.historico = []

    def depositar(self, valor):
        self.saldo += valor
        self.historico.append(('DEPÓSITO', valor))

    def sacar(self, valor):
        if self.saldo < valor:
            raise ValueError('Saldo insuficiente')
        self.saldo -= valor
        self.historico.append(('SAQUE', valor))

    def extrato(self):
        print('Extrato da conta', self.numero)
        print('Saldo:', self.saldo)
        print('Histórico:')
        for tipo, valor in self.historico:
            print(tipo, '-', valor)

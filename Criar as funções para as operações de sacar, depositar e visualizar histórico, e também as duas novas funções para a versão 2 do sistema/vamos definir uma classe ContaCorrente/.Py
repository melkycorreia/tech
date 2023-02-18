class ContaCorrente:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.historico = []

    def depositar(self, valor):
        self.saldo += valor
        self.historico.append(f"Depósito de {valor:.2f}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.append(f"Saque de {valor:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def ver_historico(self):
        print("Histórico de transações:")
        for transacao in self.historico:
            print("-", transacao)


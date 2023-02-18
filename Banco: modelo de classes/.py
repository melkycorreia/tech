class Cliente:
    def __init__(self, nome, endereco, cpf):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf

class ContaBancaria:
    def __init__(self, num_conta, saldo, data_abertura, tipo_conta):
        self.num_conta = num_conta
        self.saldo = saldo
        self.data_abertura = data_abertura
        self.tipo_conta = tipo_conta

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor

class RelacaoClienteConta:
    def __init__(self, cliente, conta):
        self.cliente = cliente
        self.conta = conta

cliente1 = Cliente("João", "Rua A, 123", "111.222.333-44")
conta1 = ContaBancaria("12345", 1000, "01/01/2022", "Corrente")
relacao1 = RelacaoClienteConta(cliente1, conta1)

cliente2 = Cliente("Maria", "Rua B, 456", "555.666.777-88")
conta2 = ContaBancaria("67890", 5000, "02/02/2022", "Poupança")
relacao2 = RelacaoClienteConta(cliente2, conta2)

conta1.depositar(500)
conta2.sacar(1000)

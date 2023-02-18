class Cliente:
    def __init__(self, nome: str, endereco: str, cpf: str):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

class ContaBancaria:
    def __init__(self, numero: str, saldo: float, tipo: str):
        self.numero = numero
        self.saldo = saldo
        self.tipo = tipo

    def depositar(self, valor: float):
        self.saldo += valor

    def sacar(self, valor: float):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor

    def __str__(self):
        return f"{self.numero} ({self.tipo}): R${self.saldo:.2f}"

class ClienteConta:
    def __init__(self, cliente: Cliente, conta: ContaBancaria):
        self.cliente = cliente
        self.conta = conta

    def __str__(self):
        return f"{self.cliente.nome} ({self.cliente.cpf}) -> {self.conta}"

# Exemplo de uso:
cliente1 = Cliente("João da Silva", "Rua A, 123", "111.222.333-44")
conta1 = ContaBancaria("12345-6", 1000.0, "corrente")
relacao1 = ClienteConta(cliente1, conta1)

cliente2 = Cliente("Maria Oliveira", "Rua B, 456", "555.666.777-88")
conta2 = ContaBancaria("65432-1", 5000.0, "poupança")
relacao2 = ClienteConta(cliente2, conta2)

conta1.depositar(500)
conta2.sacar(1000)

print(relacao1)
print(relacao2)

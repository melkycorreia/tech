# Neste exemplo, a classe Cliente representa as informações do cliente, como nome, endereço e CPF. A classe ContaBancaria representa os dados da conta bancária, incluindo o número da conta, saldo e tipo de conta. A classe ClienteConta representa a relação entre o cliente e a conta bancária, por meio de objetos de cliente e conta.

Além disso, as classes Cliente, ContaBancaria e ClienteConta estão mapeadas para um modelo de classes UML, representando seus atributos e métodos.

# As instâncias de objetos cliente e conta bancária são criadas e, em seguida, associadas por meio de objetos de relação cliente-conta. Por fim, algumas transações bancárias são realizadas para testar as funcionalidades das classes ContaBancaria.

# Python


# código Python que implementa as classes de Cliente e Conta Bancária, seguindo o modelo de classes UML

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

# Autor

# Melky Correia


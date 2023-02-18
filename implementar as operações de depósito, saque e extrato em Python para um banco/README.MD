implementar as operações de depósito, saque e extrato em Python para um banco, você pode seguir os seguintes passos:



Para implementar as operações de depósito, saque e extrato em Python para um banco, podemos criar uma classe chamada Conta que representará uma conta bancária. Esta classe pode conter métodos para cada uma das operações desejadas, além de uma lista para armazenar o histórico de transações.

# Criar dois arquivos em Pyton

# Pyton

class ContaBancaria:
    def __init__(self, numero_conta):
        self.numero_conta = numero_conta
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def extrato(self):
        return f"Conta: {self.numero_conta} / Saldo: R${self.saldo:.2f}"

Com essa implementação, pode-se criar objetos da classe ContaBancaria e utilizar seus métodos para realizar as operações de depósito, saque e extrato. 
Por exemplo:

# Pyton

# Criando uma nova conta
conta = ContaBancaria(123456)

# Depositando R$ 500,00 na conta
conta.depositar(500)

# Sacando R$ 200,00 da conta
conta.sacar(200)

# Imprimindo o extrato da conta
print(conta.extrato())  # Saída: Conta: 123456 / Saldo: R$300.00


# autor


# Melky Correia

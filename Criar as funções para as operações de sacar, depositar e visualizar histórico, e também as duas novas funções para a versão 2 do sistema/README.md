Vamos criar as funções para as operações de sacar, depositar e visualizar histórico, e também as duas novas funções para a versão 2 do sistema.

Para começar, vamos definir uma classe ContaCorrente que irá armazenar as informações da conta, como o saldo e o histórico de transações. As funções serão métodos dessa classe.


# Python

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
            
Essa classe possui um construtor que permite definir um saldo inicial para a conta, e três métodos: depositar, sacar e ver_historico.
O método depositar adiciona o valor informado ao saldo da conta e registra a transação no histórico.
O método sacar subtrai o valor informado do saldo da conta e registra a transação no histórico, desde que haja saldo suficiente. Caso contrário, uma mensagem é exibida informando que o saque não foi realizado.
O método ver_historico exibe o histórico de transações na tela.
Agora podemos criar duas novas funções para a versão 2 do sistema: criar_usuario e criar_conta_corrente.

# Python

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta_corrente(self, cpf, saldo_inicial=0):
        if cpf not in self.contas:
            self.contas[cpf] = ContaCorrente(saldo_inicial)
            print(f"Conta corrente criada para o CPF {cpf}.")
        else:
            print(f"Já existe uma conta corrente para o CPF {cpf}.")

    def criar_usuario(self, nome, cpf):
        if cpf not in self.contas:
            self.contas[cpf] = {"nome": nome, "conta": None}
            print(f"Usuário {nome} criado com sucesso.")
        else:
            print("Já existe um usuário com esse CPF.")



A classe Banco agora possui um dicionário contas que associa um CPF a uma conta corrente ou a um usuário. O método criar_conta_corrente cria uma nova conta corrente para o CPF informado, caso não exista uma conta corrente associada a esse CPF. O método criar_usuario cria um novo usuário com o nome e CPF informados, caso não exista um usuário com esse CPF.
Com essas funções, podemos criar um sistema simples de banco com usuários e contas correntes. Veja um exemplo de como utilizá-las:


# Python


banco = Banco()
banco.criar_usuario("João Silva", "111.111.111-11")
banco.criar_conta_corrente("111.111.111-11",


# Autor

# Melky Correia


























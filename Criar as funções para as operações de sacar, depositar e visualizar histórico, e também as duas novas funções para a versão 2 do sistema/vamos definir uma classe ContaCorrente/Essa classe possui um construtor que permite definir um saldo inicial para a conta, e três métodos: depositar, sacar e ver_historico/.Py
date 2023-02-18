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

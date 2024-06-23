# cliente.py

class Cliente:
    
    def __init__(self, endereco):
        self.contas = []
        self.endereco = endereco
        self.indice_conta = 0

    def realizar_operacao(self, conta, tipo_operacao, valor):
        transacoes_hoje = conta.historico.transacoes_do_dia()
        if len(transacoes_hoje) >= 3:
            print(f"Limite de transações diárias atingido. Transação de {tipo_operacao} não pode ser realizada.")
            return False
        return True


    def adicionar_conta(self, conta):
        self.contas.append(conta)

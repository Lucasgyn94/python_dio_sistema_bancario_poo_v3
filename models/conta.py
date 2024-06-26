from models.historico import Historico
from datetime import datetime

class Conta:
    def __init__(self, cliente, numero_conta, agencia):
        self.__saldo = 0
        self.__numero_conta = numero_conta
        self.__agencia = agencia
        self.__historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero_conta):
        return cls(cliente, numero_conta)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero_conta(self):
        return self.__numero_conta

    @property
    def agencia(self):
        return self.__agencia

    @property
    def historico(self):
        return self.__historico

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False
    
    def sacar(self, valor):
        saldo = self.__saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Limite insuficiente.")
        elif valor > 0:
            self.__saldo -= valor
            return True
        else:
            print("Operação falhou! Valor inválido.")

        return False

    
    

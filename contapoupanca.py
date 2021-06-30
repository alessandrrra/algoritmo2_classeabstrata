from contabancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo = 0.00, limite = 2000.00, juros = 0.01):
        self.__saldo = saldo
        self.__limite = limite
        self.__juros = juros

    def cadastrar(self):
        return print("Conta Poupança cadastrada.")
    
    def depositar(self, deposito):
        if deposito > 0:
            self.__saldo += deposito
            return print("Depósito concluído. Seu saldo atual é" , self.__saldo)
        else:
            return print("Valor inválido, tente novamente.")
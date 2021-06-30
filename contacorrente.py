from contabancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, saldo = 0.00, limite = 1500.00, cartaocredito = False, cartaodebito = True):
        self.__saldo = saldo
        self.__limite = limite
        self.__cartaocredito = cartaocredito
        self.__cartaodebito = cartaodebito

    def cadastrar(self):
        return print("Conta Corrente cadastrada.")
    
    def depositar(self, deposito):
        if deposito > 0:
            self.__saldo += deposito
            return print("Depósito concluído. Seu saldo atual é" , self.__saldo)
        else:
            return print("Valor inválido, tente novamente.")
from contabancaria import ContaBancaria
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca

separador = '-----'
print(separador)

ccorrente = ContaCorrente(100.00, 1500.00, False, True)
ccorrente.cadastrar()
ccorrente.depositar(800.00)

print(separador)

cpoupanca = ContaPoupanca(500.00, 2000.00, 0.5)
cpoupanca.cadastrar()
cpoupanca.depositar(600.00)

print(separador)
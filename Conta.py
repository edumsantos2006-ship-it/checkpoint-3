class Conta:

    def __init__(self, saldo):
        self._saldo = 0.0

    def get_saldo(self):
        return self._saldo
    
    def get_depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"seu deposito de R$ {valor} foi realizado.")

    def get_sacar(self, valor):
        if valor <= self._saldo:
            self._saldo-= valor
            print(f"saque de R${valor} realizado")

        else:
            print("Saldo insuficiente, saque recusado.")
from Conta import Conta

class ContaCorrente(Conta):
    def sacar(self,valor):
        taxa = 1
        total = valor + taxa

        if total <= self._saldo:
            self._saldo -= total
            print(f"saque de R$ {valor} + R$ {taxa} de taxa realizado.")
        else:
            print("saldo insuficiente")

from Conta import Conta

class ContaPoupanca(Conta):
    def render_juros(self):
        self._saldo *= 1.01
        print(f"seu rendimento é de: R$ {self._saldo:.2f}")
        
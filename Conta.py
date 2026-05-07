import json

class Conta:



    def __init__(self, saldo):
        self._saldo = saldo

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

    def conta_do_banco(self):
        return {
            "saldo" : self._saldo
        }

    def salvar_dados(self):
        with open("dados.json", "w") as arquivo:
            json.dump(self.conta_do_banco(), arquivo, indent=4)

    def carregar_dados(self):
        try:
            with open("dados.json", "r") as arquivo:
                dados = json.load(arquivo)
                self._saldo = dados["saldo"]
        except FileNotFoundError:
            print("arquivo não encontrado")
            
            
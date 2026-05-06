from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
from Cliente import Cliente



def exibir_menu():

    print("\n --- MENU DO CAIXA ELETRÔNICO ---")
    print("--- [1] Para ver Saldo --- ")
    print("--- [2] Para Depositar ---")
    print("--- [3] Para Sacar")
    print("--- [4] render juros")
    print("--- [5] ver saldo(após rendimento)")
    print("--- [0] Sair ---")

def main():
    cliente = Cliente("Eduardo", "340.555.999-00")

    conta_corrente = ContaCorrente(100)
    conta_poupanca = ContaPoupanca(100)
    


    while True:
        exibir_menu()
        opcao = input("digite uma opção:")

        match opcao:
            case "1":
                print(f"seu saldo: R$ {conta_corrente.get_saldo():.2f}")

            case "2":
                valor = float(input("Digite o valor que deseja depositar em R$: "))
                conta_corrente.get_depositar(valor)
            
            case "3":
                valor = float(input("Digite o valor que deseja sacar em R$: "))
                conta_corrente.get_sacar(valor)
            
            case "4":
                conta_poupanca.render_juros()
            
            case "5":
                print(f"Seu saldo na Poupança: R$ {conta_poupanca.get_saldo():.2f}")




if __name__ == "__main__":
    main()
from sisbanco import Conta, Banco
import os

def terminal():
    sisbanco = Banco()
    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("SisBanco::Bem-Vindo!")
        print("..::Opcoes::..")
        print("[0]–CriarConta")
        print("[1]–Creditar")
        print("[2]–Debitar")
        print("[3]–Transferir")
        print("[4]–Saldo")
        print("[5]–Sair")

        opcao = int(input("Digite: "))

        os.system('cls' if os.name == 'nt' else 'clear')

        if opcao == 0:
            # solicite o numero da conta a ser criada
            conta_numero = int(input("Digite o numero da conta: "))
            # instancie uma conta com esse numero
            conta = Conta(conta_numero)
            # cadastre a conta no sisbanco
            sisbanco.cadastrar(conta)
            input("Pressione Enter para continuar...")

        elif opcao == 1:
            # solicite o numero da conta alvo
            conta_alvo = int(input("Digite o numero da conta: "))
            # solicite o valor a ser creditado
            valor = float(input("Digite o valor a ser creditado: "))
            # realize a operacao de credito no sisbanco
            sisbanco.creditar(conta_alvo, valor)
            input("Pressione Enter para continuar...")


        elif opcao == 2:
            # solicite o numero da conta alvo
            conta_alvo = int(input("Digite o numero da conta: "))
            # solicite o valor a ser debitado
            valor = float(input("Digite o valor a ser debitado: "))
            # realize a operacao de debito no sisbanco
            sisbanco.debitar(conta_alvo, valor)
            input("Pressione Enter para continuar...")

        elif opcao == 3:
            # solicite o numero da conta origem
            conta_origem = int(input("Digite o numero da conta origem: "))
            # solicite o numero da conta destino
            conta_destino = int(input("Digite o numero da conta destino: "))
            # solicite o valor a ser transferido
            valor = float(input("Digite o valor a ser transferido: "))
            # realize a operacao de transferencia no sisbanco
            sisbanco.transferir(conta_origem, conta_destino, valor)
            input("Pressione Enter para continuar...")

        elif opcao == 4:
            # solicite o numero da conta alvo
            conta_alvo = int(input("Digite o numero da conta: "))
            # realize a operacao de obtencao de saldo no sisbanco
            saldo_conta = sisbanco.saldo(conta_alvo)
            # exiba o saldo na tela
            print(f"Saldo da conta {conta_alvo}: {saldo_conta}")
            input("Pressione Enter para continuar...")

        elif opcao == 5:
            print("SisBanco::Bye!")
            input("Pressione Enter para continuar...")
            break 

if __name__ == "__main__":
    terminal()
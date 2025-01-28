from sisbanco import Conta, Banco, ContaPoupanca, ContaEspecial, ContaImposto
from excecoes import *

def terminal():
   sisbanco = Banco()
   while(True):
      print("SisBanco::Bem-Vindo!")
      print(".::Opcoes::.")
      print("[0] Cadastrar Conta")
      print("[1] Creditar")
      print("[2] Debitar")
      print("[3] Transferir")
      print("[4] Consultar Saldo")
      print("[5] Render Juros")
      print("[6] Render Bonus")
      print("[7] Alterar Taxa_Juros")      
      print("[8] Alterar Taxa_Imposto")
      print("[9] Sair")
      opcao = input("Digite:")
      
      if opcao == 0:
         # qual o tipo de conta a ser criada: S - Simples, P - Poupanca, E - Especial
         tipo_conta = input("Digite o tipo de conta (S - Simples, P - Poupanca, E - Especial): ")
         # solicite o numero da conta a ser criada
         conta_numero = input("Digite o numero da conta: ")
         # instancie uma conta do tipo selecionado com esse numero
         if tipo_conta == 'S':
               conta = Conta(conta_numero)
         elif tipo_conta == 'P':
               conta = ContaPoupanca(conta_numero)
         elif tipo_conta == 'E':
               conta = ContaEspecial(conta_numero)
         elif tipo_conta == 'E':
            conta = ContaImposto(conta_numero)
         # cadastre a conta no sisbanco
         try:
            sisbanco.cadastrar(conta)
         except VIException as VIE:
            VIE.print_mensagem_erro()
         except CEException as CEE:
            CEE.print_mensagem_erro()
         else:
            print("Conta cadastrada")
         finally:   
            input("Pressione Enter para continuar...")

      elif opcao == 1:
         # solicite o numero da conta alvo
         conta_alvo = input("Digite o numero da conta: ")
         # solicite o valor a ser creditado
         valor = float(input("Digite o valor a ser creditado: "))
         # realize a operacao de credito no sisbanco
         try:
            sisbanco.creditar(conta_alvo, valor)
         except VIException as VIE:
            VIE.print_mensagem_erro()
         except CIException as CEE:
            CEE.print_mensagem_erro()
         else:
            print("Operacao realizada!")
         finally:   
            input("Pressione Enter para continuar...")

      elif opcao == 2:
         # solicite o numero da conta alvo
         conta_alvo = input("Digite o numero da conta: ")
         # solicite o valor a ser debitado
         valor = float(input("Digite o valor a ser debitado: "))
         # realize a operacao de debito no sisbanco
         try:
            sisbanco.debitar(conta_alvo, valor)
         except VIException as VIE:
            VIE.print_mensagem_erro()
         except SIException as SIE:
            SIE.print_mensagem_erro()
         except CIException as CIE:
            CIE.print_mensagem_erro()
         else:
            print("Operacao realizada!")
         finally:   
            input("Pressione Enter para continuar...")

      elif opcao == 3:
         # solicite o numero da conta origem
         conta_origem = input("Digite o numero da conta origem: ")
         # solicite o numero da conta destino
         conta_destino = input("Digite o numero da conta destino: ")
         # solicite o valor a ser transferido
         valor = float(input("Digite o valor a ser transferido: "))
         # realize a operacao de transferencia no sisbanco
         try:
            sisbanco.transferir(conta_origem, conta_destino, valor)
         except CIException as CIE:
            CIE.print_mensagem_erro()
         else:
            print("Operacao realizada!")
         finally:   
            input("Pressione Enter para continuar...")

      elif opcao == 4:
         # solicite o numero da conta alvo
         conta_alvo = input("Digite o numero da conta: ")
         # realize a operacao de obtencao de saldo no sisbanco
         try:
            saldo_conta = sisbanco.saldo(conta_alvo)
         except CIException as CIE:
            CIE.print_mensagem_erro()
         else:
            # exiba o saldo na tela
            print(f"Saldo da conta {conta_alvo}: {saldo_conta}")
         finally:   
            input("Pressione Enter para continuar...")

      
      elif opcao == 5:
         # solicite o número da conta alvo
         conta_alvo = input("Digite o numero da conta: ")
         # realize a operação correção da poupança no sisbanco
         try:
            sisbanco.render_juros(conta_alvo)
         except TJIException as TJIE:
            TJIE.print_mensagem_erro()
         except CIException as CIE:
            CIE.print_mensagem_erro()
         else:
            print("Operacao realizada!")
         finally:   
            input("Pressione Enter para continuar...")
      
      elif opcao == 6:
         # solicite o número da conta alvo
         conta_alvo = input("Digite o numero da conta: ")
         # realize a operação conversão/rendimento de bônus no sisbanco
         try:
            sisbanco.render_bonus(conta_alvo)
         except CIException as CIE:
            CIE.print_mensagem_erro()
         else:
            print("Operacao realizada!")
         finally:   
            input("Pressione Enter para continuar...")
      
      elif opcao == 7:
         # solicite a nova taxa de correção da poupança
         nova_taxa = float(input("Digite a nova taxa de correção da poupança: "))
         # realize a operação de alteração da taxa no sisbanco
         sisbanco.set_taxa_poupanca(nova_taxa)
         input("Pressione Enter para continuar...")

      elif opcao == 8:
         # solicite a nova taxa de correção da poupança
         nova_taxa = float(input("Digite a nova taxa de imposto: "))
         # realize a operação de alteração da taxa no sisbanco
         sisbanco.set_taxa_imposto(nova_taxa)
         input("Pressione Enter para continuar...")
         
      elif opcao == 9:
         print("SisBanco::Bye!")
         break

if __name__ == "__main__":
   terminal()
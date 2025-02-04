from sisbanco_bugs import Conta, Banco, ContaPoupanca, ContaEspecial, ContaImposto, ContaAbstrata
import unittest

class TestSisbanco(unittest.TestCase):
    def setUp(self):
        self.conta_simples = Conta("123")
        self.conta_simples2 = Conta("1234")
        self.conta_poupanca = ContaPoupanca("321")
        self.conta_especial = ContaEspecial("456")
        self.conta_imposto = ContaImposto("654")

        self.sisbanco = Banco(0.001, 0.1)

    #1
    def test_conta_abstrata_init(self):
        self.assertEqual(self.conta_simples._saldo, 0.0, "[ContaAbstrata] Saldo inicializado errado")
    
    #2
    def test_conta_abstrata_creditar(self):
        self.conta_simples.creditar(10)
        self.assertEqual(self.conta_simples._saldo, 10, "[ContaAbstrata] Módulo Creditar está errado")

    #3
    def test_conta_abstrata_saldo(self):
        self.assertEqual(self.conta_simples.get_saldo(), 0.0, "[ContaAbstrata] Módulo 'get_saldo' errado")

    #4
    def test_conta_debitar(self):
        self.conta_simples.creditar(10)
        self.conta_simples.debitar(5)
        self.assertEqual(self.conta_simples._saldo, 5,"[Conta] Módulo 'debitar' está errado")    

    #5
    def test_conta_poupanca_render_juros(self):
        self.conta_poupanca.creditar(10)
        try:
            self.conta_poupanca.render_juros(0.1)
        except Exception as e:
            self.fail("[ContaPoupança] Módulo 'render_juros' está errado")

    #6
    def test_conta_especial_render_bonus(self):
        self.conta_especial.creditar(100)
        self.conta_especial.render_bonus()
        self.assertEqual(self.conta_especial._ContaEspecial__bonus, 0.0, "[ContaEspecial] Módulo 'render_bonus' está errado")

    #7
    def test_conta_imposto_debitar(self):
        self.conta_imposto.creditar(10000)
        self.conta_imposto.debitar(1000)
        self.assertEqual(self.conta_imposto._saldo, 8999, "[ContaImposto] Módulo 'debitar' está errado")

    #8
    def test_banco_cadastrar(self):
        self.sisbanco.cadastrar(self.conta_imposto)
        self.assertEqual(self.conta_imposto.get_taxa(), 0.1)

    #9
    def test_banco_creditar(self):
        self.sisbanco.cadastrar(self.conta_simples)
        self.sisbanco.creditar('123', 100)
        self.assertEqual(self.conta_simples._saldo, 100.0)

    #10
    def test_banco_debitar(self):
        self.sisbanco.cadastrar(self.conta_simples)
        self.sisbanco.creditar('123', 100)
        self.sisbanco.debitar('123', 10)
        self.assertEqual(self.conta_simples._saldo, 90.0)

    #11
    def test_banco_transferir(self):
        self.sisbanco.cadastrar(self.conta_simples)
        self.sisbanco.cadastrar(self.conta_simples2)
        self.sisbanco.creditar('123', 100)
        self.sisbanco.transferir('123', '1234', 50)
        self.assertEqual(self.conta_simples2._saldo, 50.0)

    #12
    def test_banco_set_taxa_imposto(self):
        self.sisbanco.cadastrar(self.conta_imposto)
        self.sisbanco.set_taxa_imposto(0.1)
        self.assertEqual(self.conta_imposto._ContaImposto__taxa, 0.1)

if __name__ == '__main__':
    unittest.main(verbosity=2)

        
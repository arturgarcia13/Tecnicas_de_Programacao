from sisbanco import Conta, Banco, ContaPoupanca, ContaEspecial, ContaImposto
import unittest

class TestClassesSisbanco(unittest.TestCase):
    def setUp(self):
        # Inicializa o banco e cadastra contas
        self.sisbanco = Banco()

        self.conta_simples = Conta("123")
        self.sisbanco.cadastrar(self.conta_simples) 

        self.conta_poupanca = ContaPoupanca("456")
        self.sisbanco.cadastrar(self.conta_poupanca)

        self.conta_especial = ContaEspecial("789")
        self.sisbanco.cadastrar(self.conta_especial)

        self.conta_imposto = ContaImposto("321")
        self.sisbanco.cadastrar(self.conta_imposto)

    # Métodos auxiliares para operações repetidas
    def _creditar_e_verificar(self, numero, valor, saldo_esperado):
        self.sisbanco.creditar(numero, valor)
        self.assertEqual(self.sisbanco.saldo(numero), saldo_esperado, f"Erro ao creditar na conta {numero}")

    def _debitar_e_verificar(self, numero, valor, saldo_esperado):
        self.sisbanco.debitar(numero, valor)
        self.assertEqual(self.sisbanco.saldo(numero), saldo_esperado, f"Erro ao debitar da conta {numero}")

    # Testes gerais
    def test_saldo_inicial(self):
        self.assertEqual(self.sisbanco.saldo("123"), 0, "Saldo inicial incorreto para Conta Simples")

    # Testes para Conta Simples
    def test_conta_simples_creditar(self):
        self._creditar_e_verificar("123", 100, 100)

    def test_conta_simples_debitar(self):
        self._creditar_e_verificar("123", 100, 100)
        self._debitar_e_verificar("123", 50, 50)

    # Testes para Conta Poupança
    def test_conta_poupanca_instance(self):
        self.assertIsInstance(self.sisbanco.procurar("456"), ContaPoupanca, "Conta Poupança não instanciada corretamente")

    def test_conta_poupanca_taxa(self):
        self.assertEqual(self.sisbanco.get_taxa_poupanca(), 0.001, "Taxa de poupança incorreta")

    def test_conta_poupanca_render_juros(self):
        self._creditar_e_verificar("456", 50, 50)
        self.sisbanco.render_juros("456")
        self.assertAlmostEqual(self.sisbanco.saldo("456"), 50.05, places=2, msg="Cálculo de juros incorreto para Conta Poupança")

    # Testes para Conta Especial
    def test_conta_especial_instance(self):
        self.assertIsInstance(self.sisbanco.procurar("789"), ContaEspecial, "Conta Especial não instanciada corretamente")

    def test_conta_especial_creditar(self):
        self._creditar_e_verificar("789", 100, 100)

    def test_conta_especial_render_bonus(self):
        self._creditar_e_verificar("789", 50, 50)
        self.sisbanco.render_bonus("789")
        self.assertAlmostEqual(self.sisbanco.saldo("789"), 50.5, places=2, msg="Cálculo de bônus incorreto para Conta Especial")

    # Testes para Conta Imposto
    def test_conta_imposto_instance(self):
        self.assertIsInstance(self.sisbanco.procurar("321"), ContaImposto, "Conta Imposto não instanciada corretamente")

    def test_conta_imposto_taxa(self):
        self.assertEqual(self.sisbanco.get_taxa_imposto(), 0.001, "Taxa de imposto incorreta")

    def test_conta_imposto_creditar(self):
        self._creditar_e_verificar("321", 100, 100)

    def test_conta_imposto_debitar(self):
        self._creditar_e_verificar("321", 100, 100)
        self._debitar_e_verificar("321", 50, 49.95)

    # Testes para o banco
    def test_transferencia_entre_contas(self):
        self._creditar_e_verificar("123", 100, 100)
        self._creditar_e_verificar("456", 100, 100)
        self.sisbanco.transferir("456", "123", 10)
        self.assertEqual(self.sisbanco.saldo("456"), 90, "Transferência não debitada corretamente")
        self.assertEqual(self.sisbanco.saldo("123"), 110, "Transferência não creditada corretamente")


# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(TestClassesSisbanco('test_saldo_inicial'))
#     suite.addTest(TestClassesSisbanco('test_conta_simples_creditar'))
#     return suite

# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite())

if __name__ == '__main__':
    unittest.main(verbosity=2)

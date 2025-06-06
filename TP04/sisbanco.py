from abc import ABC, abstractmethod

class ContaAbstrata(ABC):
    def __init__(self, numero: str):
        self.__numero = numero 
        self.__saldo = 0.0

    def creditar(self, valor: float) -> None:
        self.__saldo += valor

    @abstractmethod
    def debitar(self, valor: float) -> None:
        pass

    def get_numero(self) -> str:
        return self.__numero

    def get_saldo(self) -> float:
        return self.__saldo

class ContaImposto(ContaAbstrata):
    def __init__(self, numero: str):
        super().__init__(numero)
        self.__taxa = 0.001

    def debitar(self, valor: float) -> None:
        self.__saldo -= valor + (valor * self.__taxa)

    def get_taxa(self) -> float:
        return self.__taxa

    def set_taxa(self, taxa: float) -> None:
        self.__taxa = taxa

class Conta(ContaAbstrata):
    def __init__(self, numero:str): 
        super().__init__(numero)
 
    def debitar(self, valor:float) -> None: 
        self.__saldo -= valor 

class ContaPoupanca(Conta):
    def __init__(self, numero:str):
        super().__init__(numero)

    def render_juros(self, taxa:float) -> None:
        self.creditar(self.get_saldo() * taxa)

class ContaEspecial(Conta):
    def __init__(self, numero: str):
        super().__init__(numero)
        self.__bonus = 0

    def render_bonus(self) -> None:
        super().creditar(self.__bonus)
        self.__bonus = 0

    def creditar(self, valor:float) -> None:
        self.__bonus += valor * 0.01
        super().creditar(valor)

class Banco: 
    def __init__(self, taxa_poupanca:float=0.001, taxa_imposto:float=0.001): 
        self.__contas = []
        self.set_taxa_poupanca(taxa_poupanca)
        self.set_taxa_imposto(taxa_imposto)

    def render_juros(self, numero:str) -> None:
        conta = self.procurar(numero)
        if isinstance(conta, ContaPoupanca):
          self.debitar(numero, conta.get_saldo() * self.get_taxa_poupanca()) 
    
    def render_bonus(self, numero:str) -> None:
        conta = self.procurar(numero)
        if isinstance(conta, ContaEspecial):
            self.creditar(numero, conta.get_saldo() * 0.01)

    def get_taxa_poupanca(self) -> float:
        return self.__taxa_poupanca

    def set_taxa_poupanca(self, taxa_poupanca:float) -> None: 
        self.__taxa_poupanca = taxa_poupanca

    def get_taxa_imposto(self) -> float:
        return self.__taxa_imposto

    def set_taxa_imposto(self, taxa_imposto:float) -> None: 
        self.__taxa_imposto = taxa_imposto

    def cadastrar(self, conta: Conta) -> None: 
        self.__contas.append(conta)  

    def procurar(self, numero:str) -> Conta: 
        for conta in self.__contas: 
            if conta.get_numero() == numero: 
                return conta 
        return None 
    
    def creditar(self, numero:str, valor:float) -> None: 
        conta = self.procurar(numero)
        if conta is not None:
            conta.creditar(valor)

    def debitar(self, numero:str, valor:float) -> None: 
        conta = self.procurar(numero)
        if conta is not None:
            conta.debitar(valor)

    def saldo(self, numero:str) -> float: 
        conta = self.procurar(numero)
        if conta is not None:
            return conta.get_saldo() 

    def transferir(self, origem:str, destino:str, valor:float) -> None:
        count_origem = self.procurar(origem)
        count_destino = self.procurar(destino)
        if count_origem is not None and count_destino is not None:
            count_origem.debitar(valor)
            count_destino.creditar(valor)


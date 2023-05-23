
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __saque_disponivel(self, valor_do_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_do_saque <= valor_disponivel

    def sacar(self, valor):
        if(self.__saque_disponivel(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapassou o limite".format(valor))
            
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
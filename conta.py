
class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objetos")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
 #      self.__limite = limite

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__saldo
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor): 
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valorDIsponivelSacar = self.saldo + self.__limite
        return valor_a_sacar <= valorDIsponivelSacar

    def saca(self, valor): 
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limte".format(valor))
    
    def transfere(self, valor, destino):
        if(self.__saldo < valor):
            print("Seu saldo é insuficiente para transferencia {}".format(self.__saldo))
        else:
            self.saca(valor)
            destino.deposita(valor)
        return "Saldo origem: {} saldo destino: {}".format(self.__saldo, destino.__saldo)
    

    print("teste")
        
        
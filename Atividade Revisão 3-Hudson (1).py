class ContaCorrente:
    
    def __init__(self,numero_conta, titular_conta,saldo):
        
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.lista=[]


        

    def sacar(self, sacar_saldo):
        
        self.saldo -= sacar_saldo
        print(f"Saque concluido!")
        self.lista.append(f"Saque de R${sacar_saldo}")
        return self.saldo


    


    def depositar(self, depositar_saldo):
        
        self.saldo += depositar_saldo
        print(f"Deposito feito!")
        self.lista.append(f"Deposito no valor de R${depositar_saldo}")
        return self.saldo


    

    def tranferir(self,tranferir_saldo,destino):

        self.saldo -= tranferir_saldo
        print(f"Transferência concluída!")
        self.lista.append(f"Transferência de R$ {tranferir_saldo} para {destino} .")
        return self.saldo


    

    def ver_saldo(self):

        print(f"Saldo:{self.saldo}")


        

    def ver_extrato_mensal(self):
        
        for i in range(0,len(self.lista)):
            print(self.lista[i])


contaBR = ContaCorrente(8877,'Hudson Ramon',800)
contaBR.depositar(1500)
contaBR.sacar(500)
contaBR.tranferir(1000,"ContaDinamarca")
contaBR.ver_saldo()
contaBR.ver_extrato_mensal()

from datetime import date

class Historico():
    def __init__(self,numero_conta):
        self.numero_conta = numero_conta
        self.extrato_transacoes = []

    def nova_transacao(self,valor):
        data_atual = date.today().strftime('%d/%m/%Y')
        self.extrato_transacoes.append(f"[{data_atual}]: {valor}")
    
    def ver_extrato_transacoes_mensal(self):
        print('\nTRANSAÇÕES')
        self.extrato_transacoes.reverse()
        for item in self.extrato_transacoes:
            print(item)
            
class ContaCorrente(Historico):
    
    def __init__(self,numero_conta, titular_conta, saldo):
        super().__init__(numero_conta)
        
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.titular_conta = titular_conta
        self.extrato = []

    def sacar(self, sacar_saldo):
        self.saldo -= sacar_saldo
        self.extrato.append(f"Saque de R${sacar_saldo:.2f}")
        
        return self.saldo

    def depositar(self, depositar_saldo):
        self.saldo += depositar_saldo
        self.extrato.append(f"Deposito de R${depositar_saldo:.2f}")
        
        return self.saldo

    def tranferencia(self,valor,acao):
        if(acao in 'recebida'):
            self.saldo += valor
        elif(acao in 'enviada'):
            self.saldo -= valor
        mensagem = f"Transferência {acao}. R$ {valor:.2f}"
        super().nova_transacao(mensagem)
        
        return self.saldo

    def ver_saldo(self):
        print(f"Seu Saldo: R${self.saldo:.2f}")

    def ver_extrato_mensal(self):
        print('\nEXTRATO')
        self.extrato.reverse()
        for item in self.extrato:
            print(item)
        super().ver_extrato_transacoes_mensal()

class ContaSalario():
    def __init__(self, numero_conta, titular_conta, saldo):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.titular_conta = titular_conta
        self.extrato = []
    
    def sacar(self, sacar_saldo):
        self.saldo -= sacar_saldo
        self.extrato.append(f"Saque de R${sacar_saldo:.2f}")
        
        return self.saldo
    def transferencia(self, conta_destino, valor):
        self.saldo -= valor
        conta_destino.tranferencia(valor, 'recebida')

        return self.saldo

    def ver_saldo(self):
        print(f"Seu Saldo: R${self.saldo:.2f}")


conta1 = ContaCorrente(5454,'Hudson ramon',800)

print('\nCONTA 2')
conta2 = ContaSalario(4545, 'Hudson ramon', 800)
conta2.sacar(50)
conta2.transferencia(conta1, 150)
conta2.ver_saldo()

print('\nCONTA 1')
conta1.depositar(900)
conta1.sacar(450)
conta1.tranferencia(250,'enviada')
conta1.ver_saldo()
conta1.ver_extrato_mensal()

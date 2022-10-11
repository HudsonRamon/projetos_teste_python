from datetime import date

class Historico:

    def __init__(self):
        self.historico = []

    def nova_transacao(self, transacao):
        self.historico.append(transacao)

    def mostra_historico(self):
        return self.historico

# ClassMãe
class ContaBancaria:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.menor_saldo = saldo

    def desconta_saldo(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            self.menor_saldo = self.saldo if self.menor_saldo > self.saldo else self.menor_saldo
        else:
            print('Saldo insuficiente!')

    def recebe_saldo(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.desconta_saldo(valor)
        self.ver_saldo()

    def depositar(self, valor):
        self.recebe_saldo(valor)
        self.ver_saldo()

    def ver_saldo(self):
        print(f"Saldo: R$ {self.saldo:.2f}")

    def transferir(self, conta_destino, valor):
        conta_destino.depositar(valor)
        self.desconta_saldo(valor)
        print(f"Transferência de R${valor:.2f} para {conta_destino.titular}")
        self.ver_saldo()

class ContaPoupanca(ContaBancaria):

    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)
        self.historico = Historico()

    def debitar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            self.add_movimentacao('debito', valor)
        else:
            print('Saldo insuficiente!')

    def creditar(self, valor):
        self.saldo += valor
        self.add_movimentacao('credito', valor)

    def ver_extrato_mensal(self):
        print('\nEXTRATO')
        for transacao in self.historico.mostra_historico():
            print(transacao)

    def add_movimentacao(self, acao, valor):
        hoje = date.today()
        str_data = hoje.strftime('%d/%m/%Y')
        texto_movimentacao = f"[{str_data}]: {acao.capitalize()} no valor de R$ {valor}"
        self.historico.nova_transacao(texto_movimentacao)
        self.render()
    
    def render(self):
        dia = date.today().strftime('%d/%m/%Y')[0:2] # gambiarra :'
        if dia == "30" or "31":
          rendimento = self.menor_saldo * 24 / 100
          self.saldo += rendimento

c1 = ContaPoupanca('234-6', 'Hudson', 400)
c2 = ContaPoupanca('937-9', 'Ramon', 500)

c1.depositar(150)
c1.debitar(150)
c1.creditar(75)
c1.transferir(c2, 90)
c1.ver_extrato_mensal()

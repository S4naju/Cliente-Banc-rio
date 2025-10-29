import datetime as dt

class Cliente:
    def __init__(self, nome, email, idade):
        self.nome  = nome
        self.email = email
        self.idade = idade
        self.agencia = "1234"
        self.nconta = "001 - sapé"
        self.movimentacoes = [] #lista c as datas, tipos, valores....

        self.taxaContrato = 250
        self.taxaMensal = 20
        self.taxaJuros = 0.2
        self.limiteCheque = 1000
        self._saldo = 0 #começa com _ pq indica q n deve ser alterado fora da classe - saldo privado
        self.transacoesIniciais()

    def transacoesIniciais(self): #deposito inicial e saque inicial automatico
        data = dt.datetime.now().date() #pega data atual
        self.depositar(500, data)
        self.sacar(100, data)

    def saldo(self):
        return self._saldo #retorna o saldo sem percorrer a lista

    def depositar(self, valor, data=None):
        self.valor = valor
        if data is None: #se n digitar a data ela vai printar a data atual
            data = dt.datetime.now().date()
        self.movimentacoes.append((data, "DEPÓSITO", valor))
        self._saldo += valor #atualiza o saldo depois do deposito
    
    def sacar(self, valor, data=None):
        if data is None:
            data = dt.datetime.now().date()
        #pode sacar até o saldo + o limite do cheque
        if valor <= self._saldo + self.limiteCheque:#se n tiver saldo pode ficar neg até -limiteCheque (-10000)
            self.movimentacoes.append((data, "SAQUE", valor))
            self._saldo -= valor
            return True #se for o valor de sacar é mair ou = ao saldo ele atualiza o saldo
        else:
            return False #se o valor for menor n altera nada no saldo

    def extrato(self, dataInicial, dataFinal):
        self.dataInicial = dataInicial
        self.dataFinal = dataFinal
        saldoParcial = 0 #começa zerado e vai sendo atualizado a cada movimentação feita
        resultado = [] #lista q vai guardas as linhas do extrato: data, valor, tipo, saldoParcial

        movimentacoesOrdenadas = sorted(self.movimentacoes, key=lambda x: x[0]) #key =lambda x: x[0] - como ele deve comparar os itens da lista p colocar em ordem.
        #sorted - ordenar as datas do extrato msm se tiverem colocado fora de ordem

        for data, tipo, valor in movimentacoesOrdenadas:
            if dataInicial <= data <= dataFinal: #movimentações entre essas datas
                if tipo == "DEPÓSITO":
                    saldoParcial += valor
                else:
                    saldoParcial -= valor #saque
                resultado.append((data, tipo, valor, saldoParcial)) #adiciona as coisas na lista
        return resultado

    def simularFinanciamento(self, valor, nParcelas): #usando a tabela PRICE
        self.nParcelas = nParcelas
        i = self.taxaJuros
        parcelaBase = valor*(i*(1+i)**nParcelas)/((1+i)**nParcelas-1)
        parcelaTotal = parcelaBase + self.taxaMensal
        totalPago = parcelaTotal*nParcelas + self.taxaContrato
        jurosTotal = totalPago - valor -(self.taxaMensal*nParcelas) - self.taxaContrato #calcula o juros subitraindo o total pago
        cet = ((totalPago/valor)-1)*100 
        return{
            "valorParcelas": valor,
            "nParcelas": nParcelas,
            "taxaJuros": i,
            "taxaContrato": self.taxaContrato,
            "taxaMensal": self.taxaMensal,
            "valorParcela": parcelaTotal,
            "totalPago":totalPago,
            "jurosTotal":jurosTotal,
            "CET": cet
        }
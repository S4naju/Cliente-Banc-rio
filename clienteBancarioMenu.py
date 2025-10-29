from clienteBancario import Cliente
import datetime as dt

class Menu():
    def __init__(self, cliente):
        self.cliente = cliente
    
    def data(self, mensagem):
        self.mensagem = mensagem
        while True:
            entrada = input(mensagem).strip() #strip - remove espaços em branco no inicio e no fim de um texto
            if entrada == "": #se n digitar nada pega a data atual
                return dt.datetime.now().date()
            try:
                return dt.datetime.strptime(entrada, "%d/%m/%Y").date() #strptime - converte uma string q representa uma data em um objeto datetime
            except ValueError:
                print("data inválida! por valor use o formato DATA/MÊS/ANO")

    def menuu(self):
        while True:
            print("\n" + "-"*80)
            print(f"BEM-VINDO(A) {self.cliente.nome} AO BANCO IFRJ".center(80).upper())
            print("-"*80)
            print(f"{'[1] DEPOSITAR':<30} | {'[2] SACAR':>14}") #<30- alinha o texto a esquerda em 12 espaços
            print(f"{'[3] VER SALDO':<30} | {'[4] VER EXTRATO':>20}") #>20 - alinha o texto a direita em 9 espaços
            print(f"{'[5] SIMULAR FINANCIAMENTO':<30} | { '[6] SAIR':>13}")
            print("-"*80)
            try:
                escolha = int(input("escolha uma das opções acima: "))
                if escolha < 1 or escolha > 6:
                    print("por favor, digite números entre 1 e 6!\n")
                    continue
            except ValueError:
                print("valor inválido! por favor digite apenas números!\n")
                continue
        
            if escolha == 1:
                self.menuDepositar()
            elif escolha == 2:
                self.menuSacar()
            elif escolha == 3:
                self.menuSaldo()
            elif escolha == 4:
                self.menuExtrato()
            elif escolha == 5:
                self.menuFinanciamento()
            elif escolha == 6:
                print("\n" + "-"*50)
                print(f"obrigado(a) {self.cliente.nome} por usar o BANCO IFRJ!".center(50))
                print("volte sempre!".center(50))
                print("-"*50)
                break
            else:
                print("opção inválida! por favor, tente novamente!\n")

    def menuDepositar(self):
        while True:
            try:
                valor = float(input("\ndigite o valor que deseja depositar: R$"))

                if valor <= 0:
                    print("por favor, digite um valor maior que zero!\n")
                    continue

                data = self.data("digite a data do depósito (DATA/MÊS/ANO): ")
                self.cliente.depositar(valor, data)
                print("\n" + "-"*50)
                print(f"depósito de R${valor:.2f} realizado em {data.strftime('%d/%m/%Y')}!".center(50)) #2f - duas casas decimais
                print(f"saldo disponível na conta: R${self.cliente.saldo():.2f}".center(50))
                print("-"*50)
                break
            except ValueError:
                print("valor inválido! por favor digite apenas números!\n")
    
    def menuSacar(self):
        while True:
            try:
                valor = float(input("\ndigite o o valor que deseja sacar: R$"))

                if valor <= 0:
                    print("por favor, digite um valor maior que zero!\n")
                    continue

                data = self.data("digite a data do saque (DATA/MÊS/ANO): ")
                if self.cliente.sacar(valor, data):
                    print("\n" + "-"*60)
                    print(f"saque de R${valor:.2f} realizado realizado em {data.strftime('%d/%m/%Y')}!".center(60))
                    print(f"saldo disponível na conta: R${self.cliente.saldo():.2f}".center(60))
                    print("-"*60)
                    break
                else:
                    print("saldo insuficiente!\n")
            except ValueError:
                print("valor inválido! por favor digite apenas números!\n")

    def menuSaldo(self):
        print("\n" + "-"*50)
        print("SALDO ATUAL".center(50))
        print("-"*50)
        print(f"cliente: {self.cliente.nome}".center(50))
        print(f"agência: {self.cliente.agencia}".center(50))
        print(f"conta: {self.cliente.nconta}".center(50))
        print(f"saldo disponível na conta: R${self.cliente.saldo():.2f}".center(50))
        print("-"*50)
    
    def menuExtrato(self):
        print("\n" + "-"*80)
        print("EXTRATO".center(80))
        print("-"*80)
        dataInicial = self.data("data inicial (DATA/MÊS/ANO): ")
        dataFinal = self.data("data final (DATA/MÊS/ANO): \n")
        extrato = self.cliente.extrato(dataInicial, dataFinal)

        if not extrato:
            print("nenhuma movimentação nesse período!\n".center(80))
            return
        
        print("\n" + "-"*80)
        print(f"{'DATA':<12} | {'TIPO':<12} | {'VALOR':<12} | {'SALDO PARCIAL':>14}")
        print("-"*80)

        for data, tipo, valor, saldoParcial in extrato:
            print(f"\n{data.strftime('%d/%m/%Y'):<12} | {tipo:<12} | R${valor:<10.2f} | R${saldoParcial:<13.2f}")
        
        print("\n" + "-"*80)
        print(f"{'SALDO FINAL:':<15} R${extrato[-1][3]:.2f}".center(80))
        print("-"*80)
    
    def menuFinanciamento(self):
        while True:
            try:
                valor = float(input("\ndigite o valor do financiamento: R$"))
                parcelas = int(input("digite o número de parcelas: "))

                if valor <= 0 or parcelas <=0:
                    print("por favor, digite um valor maior que zero!\n")
                    continue

                resultado = self.cliente.simularFinanciamento(valor, parcelas)
                print("\n" + "-"*50)
                print("SIMULAÇÃO".center(50))
                print("-"*50)
                print(f"valor das parcelas: R${resultado['valorParcelas']:.2f}".center(50))
                print(f"número das parcelas: {resultado['nParcelas']}x".center(50))
                print(f"taxa de juros mensais: {resultado['taxaJuros']:.2f}%".center(50))
                print(f"taxa de contrato: {resultado['taxaContrato']:.2f}%".center(50))
                print(f"taxa mensal de seguro: R${resultado['taxaMensal']:.2f}".center(50))
                print(f"valor da parcela (com o seguro): R${resultado['valorParcela']:.2f}".center(50))
                print(f"total pago: R${resultado['totalPago']:.2f}".center(50))
                print(f"juros total: R${resultado['jurosTotal']:.2f}".center(50))
                print(f"CET(custo efetivo total): RS{resultado['CET']:.2f}".center(50))
                print("-"*50)
                break
            except ValueError:
                print("valor inválido! por favor digite apenas números!\n")

print("------------ BEM VINDO AO BANCO IFRJ ------------")
nome = input("qual é o seu nome? ")
email = input("qual é o seu email? ")
while True:
    try:
        idade = int(input("qual é a sua idade? "))
        if idade <= 0:
            print("por favor, digite um valor maior que zero!\n")
            continue
        break
    except ValueError:
        print("valor inválido! por favor digite apenas números!\n")

cliente1 = Cliente(nome, email, idade)
menu= Menu(cliente1)
menu.menuu()
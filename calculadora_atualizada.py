

from ast import Num
from tkinter import W


class calculadora:

    def __init__(self):
        self.num = 0
        self.num1 = 0
        self.num2 = 0
        self.ret =  str
        self.true = True


    def Iniciar(self):
        self.Menu()
        self.num = input('Digite aqui:')
        try:

            if int(self.num) == 1:
                    
                self.Adicao()
                self.Retorno()
            
            elif int(self.num) == 2:
                self.Subtracao()
                self.Retorno()

            elif int(self.num) == 3:
                self.Multiplicacao()
                self.Retorno()

            elif int(self.num) == 4:
                self.Divisao()
                self.Retorno()
        except:
            print('Por favor digote só numeros validos')
            self.Iniciar()

    def Menu(self):
        print('========= Home Calculadora =========')
        print('Escolha uma das Opções de calculo: \n'
        '[1]Adição\n'
        '[2]Subtração\n'
        '[3]Multiplicação\n'
        '[4]Divisão\n')

    def Adicao(self):
        print('Você escolheu Adição')
        self.num1 = int(input('Digite o primeiro número: '))
        self.num2 = int(input('Digite o segundo número: '))
        self.resp = self.num1 + self.num2
        print(f'\nO Numero {self.num1} + {self.num2} = {self.resp}')

    def Subtracao(self):
        print('Você escolheu Subtração')
        self.num1 = int(input('Digite o primeiro número: '))
        self.num2 = int(input('Digite o segundo número: '))
        self.resp = self.num1 - self.num2
        print(f'\nO Resultado de {self.num1} - {self.num2} = {self.resp}')

    def Multiplicacao(self):
        print('Você escolheu Multiplicação')
        self.num1 = int(input('Digite o primeiro número: '))
        self.num2 = int(input('Digite o segundo número: '))
        self.resp = self.num1 * self.num2
        print(f'\nO Resultado de {self.num1} x {self.num2} = {self.resp}')
    
    def Divisao(self):
        print('Você escolheu Divisão')
        self.num1 = int(input('Digite o primeiro número: '))
        self.num2 = int(input('Digite o segundo número: '))
        self.resp = self.num1 / self.num2
        print(f'\nO Resultado de {self.num1} x {self.num2} = {self.resp}')
    
    def Retorno(self):
        print('\nDeseja retornar ao Home Calculadora?\n Escolhas uma das opções abaixo:\n\n [S] Sim\n [N] Não \n\n Digite aqui:')
        self.ret = input()

        if self.ret == 'S' or self.ret == 's':
            return self.Iniciar()
        elif self.ret == 'N' or self.ret == 'n':
            print('Muito Obrigado por ultilizar meu software :)')



cal = calculadora()
cal.Iniciar()

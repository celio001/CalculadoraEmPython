print( '==========            ==========\n'       
       '========== Calculador ==========\n'
       '==========            ==========\n')
    
print('Escolha uma das Opções de calculo: \n'
      '[1]Adição\n'
      '[2]Subtração\n'
      '[3]Multiplicação\n'
      '[4]Divisão\n')

num = int(input('Escreva aqui: '))
while num <= 0 or num >= 5:
    print('Por favor escreva uma numero válido')
    num = int(input('Escreva aqui: '))

if num == 1:
    print('Você escolheu Adição')
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    resp = num1 + num2
    print(f'O Resultado de {num1} + {num2} = {resp}')

    print(f'O resultado é: {resp}')

elif num == 2:
    print('Você escolheu Subtração')
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    resp = num1 - num2
    print(f'O Resultado de {num1} - {num2} = {resp}')

elif num == 3:
    print('Você escolheu Multiplicação')
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    resp = num1 * num2
    print(f'O Resultado de {num1} x {num2} = {resp}')

elif num == 4:
    print('Você escolheu Divisão')
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    resp = num1 / num2
    print(f'O Resultado de {num1} x {num2} = {resp}')


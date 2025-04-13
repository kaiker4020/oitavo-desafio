import math
print('Escolha seu operador: ')
print('[1] Soma')
print('[2] Subtração')
print('[3] Multiplicação')
print('[4] Divisão')
print('[5] Potência')
print('[6] Raiz quadrada')
opçao = int(input('Escolha uma opção: '))
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
if opçao == 1:
    print(f'A soma de {num1} + {num2} é igual a {num1 + num2}.')
elif opçao == 2:
    print(f'A subtração de {num1} - {num2} é igual a {num1 - num2}.')
elif opçao == 3:
    print(f'A multiplicação de {num1} * {num2} é igual a {num1 * num2}.')
elif opçao == 4:
    print(f'A divisão de {num1} / {num2} é igual a {num1 / num2}.')
elif opçao == 5:
    print(f'A potência de {num1} ** {num2} é igual a {num1 ** num2}.')
elif opçao == 6:
    print(f'A raiz quadrada de {num1} é igual a {math.sqrt(num1)}.')
else:
    print('Opção inválida!')
print('Fim do programa!') 
#Empréstimo bancário
#import math
#c = float(input('Qual o valor da casa: '))
#s = float(input('Qual o seu salário: '))
#a = int(input('Quantos anos de financiamneto: '))
#p = c / (a * 12)
#m = s * 0.3
#if p > m:
#    print('Empréstimo negado!')
#else:
#    print('Empréstimo aprovado!')
#print(f'O valor da prestação é de R${p:.2f}')
#print(f'O valor máximo da prestação é de R${m:.2f}')

#Conversão de numeros inteiros para binário, octal e hexadecimal
#import math
#n = int(input('Digite um número: '))
#print('\nEscolha uma das bases para conversão:')
#print('[1] Converter para binário')
#print('[2] Converter para octal')
#print('[3] Converter para hexadecimal')
#opçao = int(input('Digite sua opção: '))
#if opçao == 1:
#    print(f'{n} convertido para binario é igual a {bin(n)[2:]}.')
#elif opçao == 2:
#    print(f'{n} convertido para octal é igual a {oct(n)[2:]}.')
#elif opçao == 3:
#    print(f'{n} convertido para hexadecimal é igual a {hex(n)[2:]}.')
#else:
#    print('Opção inválida! Tente novamente.')



#Mostrar qual valor é maior entre dois números
#n = int(input('Digite um número: '))
##print('--'*20)
#if n > n2:
#    print(f'O primeiro valor é maior.')
#elif n < n2:
#    print(f'O segundo valor é maior.')
#elif n == n2:
#    print(f'Os números são iguais.')



#Veriuficar se deverá se alistar ao serviço militar
#ano = int(input('Digite o ano de nascimento: '))
#idade = 2025 - ano
#print(f'A sua idade é {idade} anos.')
#if idade < 18:
#    print(f'Você ainda não pode se alistar.')
#elif idade == 18:
#    print(f'Você deve se alistar esse ano.')
#elif idade > 18:
#    print(f'Você já deveria ter se alistado há {idade - 18} anos.')


#Media de um aluno
#nota = float(input('Digite a nota do aluno: '))
#nota2 = float(input('Digite a segunda nota do aluno: '))
#media = (nota + nota2) / 2
#if media < 5:
#    print(f'O aluno foi reprovado com a média {media:.1f}.')
#elif media >= 5 and media <=6.9:
#    print(f'O aluno está de recuperação com a média {media:.1f}.')
#elif media >= 7:
#    print(f'O aluno foi aprovado com a média {media:.1f}.')



# Saber idade do atleta
#ano = int(input('Digite o ano: '))
#idade = 2025 - ano
#print(f'A sua idade é {idade} anos.')
#if idade <= 9:
#    print(f'Você é um atleta mirim.')
#elif idade > 9 and idade <= 14:
#    print(f'Você é um atleta infantil.')
#elif idade > 14 and idade <= 19:
#    print(f'Você é um atleta junior.')
#elif idade > 19 and idade <= 20:
#    print(f'Você é um atleta sênior.')
#else:
#    print(f'Você é um atleta master.')


#Triângulo 
#c1 = float(input('Digite o comprimento do primeiro comprimento: '))
#c2 = float(input('Digite o comprimento do segundo comprimento: '))
#c3 = float(input('Digite o comprimento do terceiro comprimento: ')) 
#if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1:
#    print('Os segmentos formam um triângulo.')
#else:
#    print('Os segmentos não formam um triângulo.')
#if c1 == c2 ==c3:
#    print('O triângulo é equilátero.')
#elif c1 == c2 or c1 == c3 or c2 == c3:
#    print('O triângulo é isósceles.')
#else:
#    print('O triângulo é escaleno.') 



#IMC
#p = float(input('Digite seu peso: '))
#a = float(input('Digite sua altura: '))
#imc = p / (a ** 2)
#print(f'O seu IMC é {imc:.1f}.')
#if imc < 18.5:
#    print('Você está abaixo do peso.')
#elif imc >= 18.5 and imc < 25:
#    print('Você está no peso ideal.')
#elif imc > 25 and imc <= 30:
#    print('Você está com sobrepeso.')
#elif imc > 30 and imc <= 40:
#    print('Você está com obesidade.')
#else:
#    print('Você está com obesidade mórbida.')


#Preço de um produto e forma de pagamento
#p = float(input('Digite o preço do produto: '))
#print(f'Digite a forma de pagamento:')
#print(f'[1] À vista dinheiro/cheque')
#print(f'[2] À vista cartão')
#print(f'[3] 2x no cartão')
#print(f'[4] 3x ou mais no cartão')
#opcao = int(input('Digite sua opção: '))
#if opcao == 1:
#    print(f'O preço a vista é de R${p - (p * 0.1):.2f}.')
#elif opcao == 2:
#    print(f'O preço a vista é de R${p - (p * 0.05):.2f}.')
#elif opcao == 3:
#    print(f'O preço em 2x no cartão é de R${p / 2 :.2f}.')
#    print(f'O preço total é de R${p:.2f}.')
#elif opcao == 4:
#    print(f'O preço em 3x ou mais no cartão é de R${p + (p * 0.2):.2f}.')


from random import choice

opcoes = ['pedra', 'papel', 'tesoura']
computador = choice(opcoes)

print('--'*30)
print('Vamos jogar Jokenpô!')
print('Escolha uma das opções:')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')
print('--'*30)

jogador = int(input('Digite sua opção: '))
print('--'*30)

if jogador < 0 or jogador > 2:
    print('Opção inválida! Tente novamente.')
else:
    jogador_escolha = opcoes[jogador]
    print(f'Você escolheu {jogador_escolha}.')
    print(f'O computador escolheu {computador}.')

    if jogador_escolha == computador:
        print('Empate!')
    elif (jogador_escolha == 'pedra' and computador == 'tesoura') or \
         (jogador_escolha == 'papel' and computador == 'pedra') or \
         (jogador_escolha == 'tesoura' and computador == 'papel'):
        print('Você ganhou!')
    else:
        print('Você perdeu!')

#Contagem Regressiva para o Ano Novo
#import time
#for i in range(10, 0, -1):
#    print(f'Contagem egressiva para o Ano Novo: {i}...')
#    time.sleep(1)
#print('Feliz Ano Novo!')


#Contagem de 1 a 50, mostrando apenas os números pares
#for i in range(1, 51):
#    if i % 2 == 0:
#        print(i, end=' ')




#Soma dos números ímpares múltiplos de 3 entre 1 e 500
#soma = 0 
#for i in range(1, 501):
#    if i % 2 == 1 and i % 3 == 0:
#        soma += i
#print(f'A soma dos números ímpares múltiplos de 3 entre 1 e 500 é: {soma}')    





#Tabuada com o for
#n = int(input('Digite um número: '))
#for i in range(1, 11):
#    print(f'{n} x {i:2} = {n * i}')



#Soma dos números pares entre 1 e 6
#soma = 0
#for i in range(1, 7):
#    n = int(input(f'Digite o {i}º número: '))
#    if n % 2 == 0:
#        soma += n
#print(f'A soma dos números pares é: {soma}')






#PA (Progressão Aritmética)
#p = int(input('Digite o primeiro termo da PA: '))
#r = int(input('Digite a razão da PA: '))
#termos = []
#for i in range(10):
#    termo = p + i * r
#    termos.append(termo)
#print('Os 10 primeiros termos da PA são:')
#print(', ' .join(str(t) for t in termos))    






#Numeros Primos
#n = int(input('Digite um número inteiro: '))
#d = 0
#for i in range(1, n + 1):
#    if n % i == 0:
#        d += 1
#if d == 2:
#    print(f'{n} é um número primo.')
#else:
#    print(f'{n} não é um número primo.')   




#Frase Palíndromo
#frase = str(input('Digite uma frase: ')).strip().lower()
#palavras = frase.split()
#junto = ''.join(palavras)
#inverso = ''
#for letra in range(len(junto) - 1, -1, -1):
#    inverso += junto[letra]
#print(f'O inverso de {junto} é {inverso}.')
#if inverso == junto:
#    print('A frase é um palíndromo.')
#else:
#    print('A frase não é um palíndromo.')


#Contagem de pessoas maiores e menores de idade
#ma = 0
#me = 0
#for i in range(1, 8):
#    n = int(input(f'Digite o {i} ano de nascimento: '))
#    idade = 2025 - n
#    if idade >= 18:
#        ma += 1
#    else:
#        me += 1
#print(f'São de menor {me} pessoas. ')
#print(f'São maiores {ma} pessoas. ')






#Maior e menor peso
#for i in range(1, 6):
#    n = float(input(f'Digite o peso da {i}ª pessoa: '))
#    if i == 1:
#        maior = n
#        menor = n
#    else:
#        if n > maior:
#            maior = n
#        if n < menor:
#            menor = n
#print(f'O maior peso lido foi {maior}kg.')
#print(f'O menor peso lido foi {menor}kg.')






#Análise de dados do grupo
#si = 0
#hm = ''
#hi = 0
#mn = 0
#for i in range(1, 5):
#    n = str(input('Digite o nome: ')).strip() .title()
#    s = str(input('Digite o sexo [M/F]: ')).strip().upper()
#    i = int(input('Digite a idade: '))
#    si += i
#    if s == 'M':
#        if i > hi:
#            hi = i
#            hm = n
#    elif s == 'F':
#        if i < 20:
#            mn += 1
#md = si / 4
#print(f'A média de idade do grupo é {md} anos.')
#if hm:
#    print(f'O homem mais velho é {hm} com {hi} anos.')
#else:
#    print('Não há homens no grupo.')
#print(f'O número de mulheres com menos de 20 anos é {mn}.')

    







    
    


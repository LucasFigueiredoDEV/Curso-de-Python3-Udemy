'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
'''
EXERCICIO RESOLVIDO:
'''

try:
    print('Descubra se o número é ímpar ou par!')
    numero = input('Digite um número:')
    numero_inteiro = int(numero)

    resto = numero_inteiro % 2
    if resto == 0:
        print('O numero {} é par!'.format(numero))
    else:
        print('O número é impar!')
except:
    print('Você não digitou um número inteiro!')






'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''
'''
EXERCICIO RESOLVIDO:
'''

hora = (input('Digite a hora em números inteiros: '))
hora_inteiro = int(hora)

try:
    
    if hora_inteiro >= 0 and hora_inteiro <= 11:
        print('Bom dia!')
    elif hora_inteiro >= 12 and hora_inteiro <= 17:
        print('Boa tarde!')
    elif hora_inteiro >= 18 and hora_inteiro <= 23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora!')

except:
    print('Por favor, digite apenas números inteiros!')





'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver 5 ou 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
'''

'''
EXERCICIO RESOLVIDO:
'''

nome = input('Digite o seu primeiro nome: ')

if nome:
    contar_caracteres_nome = len(nome)
    if contar_caracteres_nome <= 4:
        print('Seu nome é curto!')
    elif contar_caracteres_nome == 5 or contar_caracteres_nome == 6:
        print('Seu nome é normal!')
    else:
        print('Seu nome é muito grande!')
else:
    print('Você não digitou nada no campo!')
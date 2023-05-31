'''
Calculadora com while
'''

while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite o operador (+ - / *)')

    numeros_validos = None
    numero1_float = 0
    numero2_float = 0
    
    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    

    print('Realizando a sua conta, confira o resultado abaixo:')
    
    if operador == '+':
        soma = numero1_float + numero2_float
        print('{} + {} = {}'.format(numero1_float, numero2_float, soma))

    elif operador == '-':
        subtracao = numero1_float - numero2_float
        print('{} - {} = {}'.format(numero1_float, numero2_float, subtracao))

    elif operador == '*':
        multiplicacao = numero1_float * numero2_float
        print('{} * {} = {}'.format(numero1_float, numero2_float, multiplicacao))

    elif operador == '/':
        divisao = numero1_float / numero2_float
        print('{} / {} = {}'.format(numero1_float, numero2_float, divisao))
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [s]im ').lower().startswith('s')
    print(sair)

    if sair is True:
        break

#Programa que pede dois valores, e mostra qual é maior, ou se eles são iguais.
print('Descubra qual valor é maior!')
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um segundo valor: ')

if primeiro_valor > segundo_valor:
    print('O primeiro valor {} é maior que o segundo valor {}'.format(primeiro_valor, segundo_valor))
elif segundo_valor > primeiro_valor:
    print('O segundo valor {} é maior que o primeiro valor {}'.format(segundo_valor, primeiro_valor))
elif primeiro_valor == segundo_valor:
    print('Os valores {} e {} são iguais!'.format(primeiro_valor, segundo_valor))
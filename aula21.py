'''
Formatação básica de strings
s - string
f - float
.<número de dígitos> f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100, .1f
Conversion flags - !r !s !a
'''

variavel = 'ABC'
print('{:>10}.'.format(variavel))
print('{:<10}.'.format(variavel))
print('{:^10}.'.format(variavel))
print(f'{20000.86432:.2f}')
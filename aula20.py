'''
Interpolação básica de strings
s - strings
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
'''

nome = 'Lucas'
preco = 1000.95897643
variavel = ('%s o preço total foi R$%.2f'%(nome, preco))
print(variavel)
print('O hexadeciamal de %d é %08X' %(1500, 15))
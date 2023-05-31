# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

'''nome = 'Otávio'
print(nome[0]) # Irá retornar a letra do indice 0, ou seja a letra 'O'.
print(nome[1]) # Irá retornar a letra do indice 1, ou seja a letra 't'.
print(nome[2]) # Irá retornar a letra do indice 2, ou seja a letra 'á'.
print(nome[3]) # Irá retornar a letra do indice 3, ou seja a letra 'v'.
print(nome[4]) # Irá retornar a letra do indice 4, ou seja a letra 'i'.
print(nome[5]) # Irá retornar a letra do indice 5, ou seja a letra 'o'.

print('á' in nome) # Analisa se a letra 'á' estaá entre as letras do nome.
print('vio' not in nome) # Analisa se 'vio' não está entre as letras do nome.
print('vio' in nome) # Analisa se 'vio' está entre as letras do nome.
print('z' in nome) # Analisa de 'z' está entre as letras do nome.'''

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar no seu nome: ')

if encontrar in nome:
    print('"{}" está em {}'.format(encontrar, nome))
else:
    print('"{}" não está entre {}'.format(encontrar, nome))

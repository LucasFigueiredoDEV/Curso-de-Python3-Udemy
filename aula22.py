'''
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caractere da str

'''

variavel = 'Olá mundo'
print(variavel[0:5])
print(variavel[:5])
print(variavel[-8:-2])
print(variavel[0:9])
print(variavel[5:9])
print(len(variavel[0:5])) #função len conta caracteres
print(variavel[0:9:2]) #O ultimo número (2) é o passo, ou seja de quanto em quanto ser contado caracteres
print(variavel[::-1]) #invertendo a string
print(variavel[-1:-10:-1]) #invertendo strings com valores negativos
print(variavel[-1:-2:-1])

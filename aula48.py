'''
for in com listas
'''

lista = ['Maria', 'Helena', 'Lucas']
lista.append('João')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
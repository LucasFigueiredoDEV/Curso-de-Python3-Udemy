'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create, read, update, delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

lista = [10, 20, 30, 40]
lista.append('Lucas')
nome = lista.pop()
lista.append(1233)
del lista[-1]
#lista.clear()
lista.insert(0, 'Lucas')
print(lista)
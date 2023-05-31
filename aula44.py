'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
create, read, update, delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''
lista = [10, 20, 30, 40]
#lista[2] = 300
#del lista[2]
#print(lista)
#print(lista[2])
lista.append(50) #adiciona item como último da lista
lista.pop() #remove último item da lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'removido:', ultimo_valor)

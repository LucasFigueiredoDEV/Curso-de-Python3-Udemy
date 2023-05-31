'''
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
'''

lista_a = ['Lucas', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
'''
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue o seu iterador
'''

'''texto = iter('Lucas') #__iter__()
print (next(texto))
print (next(texto))
print (next(texto))
print (next(texto))
print (next(texto))'''

#for letra in texto
texto = 'Lucas' #iterável
iterador = iter(texto) #iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
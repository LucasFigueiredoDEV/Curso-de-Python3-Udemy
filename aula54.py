'''
split e join com list e str
split - divide uma string
joing - une uma string
'''
frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split() #separa as palavras utilizando os espaços em branco entre cada palavra
lista_palavras2 = frase.split(',') #separa as pelavras que estão entre as virgulas, ou seja a virgula não será incluida
#resultará na formação de duas frases

#for i, frase in enumerate(lista_palavras2):
#    print(lista_palavras2[i].strip()) #strip remove os espaços do começo e do final da frase (rstrip - corta o espaço da direita da frase; lstrip - corta o espaço da esquerda da frase)

#print(lista_palavras)
#print(lista_palavras2)

frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = '-'.join(lista_frases) #une as frases com o que for escrito entre as aspas no "join"
print(frases_unidas)
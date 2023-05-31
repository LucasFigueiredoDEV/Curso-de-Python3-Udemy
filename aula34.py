'''
Iterando strings com while
'''

nome = 'Lucas Samuel' #iteráveis

tamanho_nome = len(nome)
novo_nome = ''

indice = 0
while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += '*{}'.format(letra)
    indice += 1
    
novo_nome += '*'
print(novo_nome)

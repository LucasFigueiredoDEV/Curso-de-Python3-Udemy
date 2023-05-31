texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += '*{}'.format(letra)
    print(letra)
print(novo_texto + '*')

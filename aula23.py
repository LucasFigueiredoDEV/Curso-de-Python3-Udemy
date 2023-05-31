'''
Exercicio
Peça ao usuário para digitar o seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contem (ou não) espaços
        Seu nome tem {numero} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "desculpe, você deixou campos vazios."
'''

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
idade = int or float


if nome and idade:
    print('Seu nome é: {}'.format(nome))
    print('Seu nome invertido é: {}'.format(nome[::-1]))
    if ' ' in nome:
        print('Seu nome contem espaços.')
    else:
        print('Seu nome não contém espaços.')
    print('Seu nome tem {} letras.'.format(len(nome)))
    print('A última letar do seu nome é "{}".'.format(nome[:-2:-1]))
else:
    print('Desculpe, você deixou campos vazios.')

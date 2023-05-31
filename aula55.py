'''
Lista de listas e seus indices
'''
salas = [
    #0
    ['Maria', 'Helena', ], #0
    #0
    ['Elaine', ], #1
    #   0       1        2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40, 50)],  #2

]
# print(salas[0][1]) #primeiro valor entre colchetes [] é o indice da lista, e o segundo valor entre colchetes [] é o indice dentro da lista
# print(salas[1][0])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    print('A sala é: {}'.format(sala))
    for aluno in sala:
        print('Aluno: {}'.format(aluno))
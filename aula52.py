'''
Faça uma lista de compra com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
não permita que o programa quebre com
erros de índices inexistentes na lista.
'''
import os

lista = []

while True:
    print('Selecione uma opção abaixo ou digite "q"/"quebrar" para sair do programa.')
    acao = input('Digite [i]nserir [a]pagar [l]istar: ').lower()
        
    if acao == 'i' or acao == 'inserir':
        os.system('cls')
        inserir = input('Digite o que deseja inserir na lista: ')
        lista.append(inserir)

    elif acao == 'a' or acao == 'apagar':
        os.system('cls')
        for i, valor in enumerate(lista):
                print(i, valor)
        apagar = input('Digite o número do item que deseja apagar: ') 
        try:               
            indice = int(apagar)
            del lista[indice]
                
        except ValueError:
            print('Por favor, digite um número inteiro.')
        except IndexError:
            print('Este índice não existe na lista.')
        except Exception:
            print('Erro desconhecido.')
                
    elif acao == 'l' or acao == 'listar':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar.')

        for i, valor in enumerate(lista):
                print(i, valor)
    elif acao == 'q' or acao == 'quebrar':
        break
    
    else:
            print('A opção selecionada não existe.')
print('Você saiu do programa. Utilize o run caso queira incia-lo novamente!')
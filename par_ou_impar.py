print("Descubra se o número é par ou impar")
numero = int(input("Digite o número:"))
resto = numero % 2
if resto == 0:
    print("O numéro é par!")
else:
    print("O número é impar!")
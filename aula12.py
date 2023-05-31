#programa que pede informações e imprime o indice de massa corporal do paciente
print("Vamos calcular o seu IMC(Indice de massa corporal)")
print("ex: Nome:Lucas/ Idade: 20/ altura: 1.75 / peso: 50.5")
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura * altura)
print("Nome do paciente: {}".format(nome))
print("Idade do paciente: {}".format(idade))
print("Altura do paciente: {}".format(altura))
print("Peso do paciente: {}".format(peso))
print("O seu Indice de massa corporal é de: {}".format(imc))
'''
Imprecisão de ponto flutuando (float)
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
'''
import decimal #recomendado importar, para calcular números de pontos flutuantes muito grandes, e que necessita de precisão

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print('{:.2f}'.format(numero_3)) #retorna uma string formatada
print(round(numero_3, 2)) #retorna um float da maneira correta com as quantidades de casas decimais pedidas depois da virgula
#Os zeros não aparecem, pois só é possivel aparecer, quando se formata uma string, ou seja, ficará um campo vazio após o valor float

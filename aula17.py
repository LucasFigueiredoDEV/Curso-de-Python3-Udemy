# Operadores lógicos
# and (e) or (ou) not(não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão será avaliada naquele valor
# São considerados falsy:
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

print(True and False and True) # Avaliação de curto circuito
# Quando o programa encontra um valor 'False', automaticamente ele para de avaliar os outros
# e retorna o valor 'False'

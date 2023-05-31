'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
'''

velocidade = 61  # velocidade atual do carro
local_carro = 90 # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_passou_radar1 = velocidade > RADAR_1

carro_multado1 = local_carro >= (LOCAL_1 - RADAR_RANGE)

carro_multado2 = local_carro <= (LOCAL_1 + RADAR_RANGE)

multa = carro_multado1 and carro_multado2

if velocidade_carro_passou_radar1:
    print('Velocidade do carro passou do radar 1.')
    #barra invertida \ no meio do código serve para quebrar linha 
if velocidade_carro_passou_radar1 == multa:
    print('O carro foi mutado!')
else:
    print('O carro não foi mutado!')
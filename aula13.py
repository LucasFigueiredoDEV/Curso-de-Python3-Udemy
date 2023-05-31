a = "A"
b = "B"
c = 1.1

#string = "a = {0}, a = {0}, a = {0}, b = {1}, c = {2:.2f}" (Código com a ordem definida)
        # :.2f entre {} significa que algo será formatado, nesse caso, o número ficará com duas casas decimais
        # Podemos definir a ordem das chaves que serão executadas dando
string = "a = {nome1}, a = {nome1}, a = {nome1}, b = {nome2}, c = {nome3:.2f}"

#formato = string.format(a, b, c) 

formato = string.format(nome1 = a, nome2 = b, nome3 = c)
        #tudo que vier depois de um parâmetro nomeado, deverá ser nomeado
        #Podemos nomear os parâmetros, dentro do format, sendo assim, quando fizermos a 
        #chamada da variável, deveremos chama-la pelo nome que foi dado dentro do parâmetro.


print(formato)
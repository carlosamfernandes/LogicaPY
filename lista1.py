"""1) Crie um algoritmo que receba, como entrada, o valor de três notas de um aluno e, em seguida, informe a média entre elas."""

primeira_nota = float(input("Informe a primeira nota: "))
segunda_nota = float(input("Informe a segunda nota: "))
terceira_nota = float(input("Informe a terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota)/3
media = round (media , 1)
print(f"A média final é {media}.")

"""2) Recrie o algoritmo de cálculo de média das notas, mas, desta vez, calcule a média ponderada, sabendo que a primeira nota possui peso 1, a segunda nota possui peso 2 e a terceira nota possui peso 3."""

primeira_nota = float(input("Informe a primeira nota: "))
segunda_nota = float(input("Informe a segunda nota: "))
terceira_nota = float(input("Informe a segunda nota: "))

primeira_nota = primeira_nota * 1
segunda_nota = segunda_nota * 2
terceira_nota = terceira_nota * 3

media = (primeira_nota + segunda_nota + terceira_nota) / 3
#media = round(media, 1)

print(f"A média final ponderada é: {round(media, 1)}.")

"""3) Crie um algoritmo que recebe o valor da altura e do peso de uma pessoa e retorna seu IMC. 
IMC = peso / altura²
"""

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura em metros: "))

imc = peso / (altura ** 2)
#imc = round(imc , 1)

#print(f"Seu IMC é {round(imc, 1)}")
print(f"Seu IMC é {0:.2f}".format(imc))

"""4) Crie um algoritmo que recebe um valor de temperatura em Celsius e o converte para Fahrenheit. 
F = (C * 9/5)+32
"""

temp_celsius = float(input("Informe a temperatura em Celsius que deseja converter para Fahrenheit: "))

temp_fahrenheit = (temp_celsius * 9 / 5) + 32
temp_fahrenheit = round(temp_fahrenheit , 1)

print(f"A temperatura em Celsius {temp_celsius} °C corresponde a {temp_fahrenheit} °F.")

"""5) Um motorista deseja abastecer um valor X em reais, de combustível. Escreva um algoritmo para ler o preço do litro do combustível e o valor que o motorista deseja abastecer. Em seguida, informe quantos litros foram abastecidos."""

valor_combustivel = float(input("Informe o valor do combustível: "))
valor_abastecer = float(input("Informe o valor que deseja abastecer: "))

valor_combustivel = round(valor_combustivel , 3)
valor_abastecer = round(valor_abastecer , 2)

total_litros = valor_abastecer / valor_combustivel
total_litros = round(total_litros , 3)

print(f"O total de litros que serão abastecidos com esse valor é {total_litros} L.")

"""6) Crie um algoritmo para calcular a média de duas notas digitadas pelo usuário, sendo que a segunda nota tem peso dois."""

primeira_nota = float(input("Informe a primeira nota: "))
segunda_nota = float(input("Informe a segunda nota: "))

segunda_nota = segunda_nota * 2

media = (primeira_nota + segunda_nota) / 2
media = round(media , 2)

print(f"A media final é {media}.")

"""7) Crie um algoritmo que calcule a gorjeta a ser paga de uma conta de restaurante. A gorjeta é calculada como sendo 10% do valor da conta, que deve ser informado pelo usuário."""

valor_conta = float(input("Informar o valor da conta: "))
valor_total = valor_conta * 1.1
print(f"O valor total da conta com os 10% é: {valor_total}")

"""8) Crie um algoritmo que calcule o novo valor de um salário a partir de um valor percentual de reajuste. O valor atual do salário e o valor percentual do reajuste devem ser informados pelo usuário como, por exemplo, 7,3%."""

salario = float(input("Favor informar o valor do salario: "))
reajuste = float(input("Favor informar o percentual do reajuste: "))
percentual = reajuste / 100
salario_reajustado = salario + (salario * percentual) 
print(f"O valor do salário reajustado é: {salario_reajustado}")

"""9) Crie um algoritmo que calcule a área de um quadrado, sendo que o comprimento do lado é informado pelo usuário. A área do quadrado é calculada elevando-se o lado ao quadrado."""

lado_quadrado = float(input("Favor informar o comprimento do lado do quadrado: "))
area_quadrado = lado_quadrado ** 2
print(f"A área do quadrado é: {area_quadrado}")

"""10) Crie um algoritmo que calcule a área de um retângulo, sendo que os comprimentos da altura e da base são informados pelo usuário. A área do retângulo é calculada multiplicando-se a altura pela base."""

base_retangulo = float(input("Favor informar o valor da base do retângulo: "))
altura_retangulo = float(input("Favor informar o valor da altura do retângulo: "))
area_retangulo = base_retangulo * altura_retangulo
print(f"A área do retângulo é: {area_retangulo}")

"""11) Crie um algoritmo que calcule a área de um círculo, sendo que o comprimento do raio é informado pelo usuário. A área do círculo é calculada multiplicando-se pi e o raio ao quadrado."""

raio_circulo = float(input("Favor informar o raio do círculo: "))
comprimento_circulo = 3.14 * (raio_circulo ** 2)
comprimento_circulo = round(comprimento_circulo, 1)
print(f"O comprimento do círculo é: {comprimento_circulo}")

"""12) Crie um algoritmo que calcule a área de uma esfera, sendo que o comprimento do raio é informado pelo usuário. A área da esfera é calculada multiplicando-se 4 vezes pi e o raio ao quadrado."""

raio_esfera = float(input("Favor informar o raio da esfera: "))
area_esfera = 4 * 3.14 * (raio_esfera ** 2)
area_esfera = round(area_esfera, 1)
print(f"A área da esfera é: {area_esfera}")

"""13) Crie um algoritmo que calcule o volume de uma caixa d’água cilíndrica, sendo que os comprimentos do raio e a altura são informados pelo usuário. O volume é calculado multiplicando-se pi, o raio ao quadrado e a altura."""

raio_cilindro = float(input("Favor informar o raio do cilindro: "))
altura_cilindro = float(input("Favor informar a altura do cilindro: "))
volume_cilindro = 3.14 * altura_cilindro * (raio_cilindro ** 2)
volume_cilindro = round(volume_cilindro, 1)
print(f"O volume do cilindro é: {volume_cilindro}")

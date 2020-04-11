def abrir(carros):
  matriz = []
  arquivo = open('carros.txt', 'r')
  conteudo = arquivo.readlines()
  linha = int(conteudo[0])
  coluna = int(conteudo[1])
  posicao = 2
  i = 0
  while i < linha:
    j = 0
    linha_matriz = []
    while j < coluna:
      linha_matriz.append(conteudo[posicao])
      posicao += 1
      j += 1
    matriz.append(linha_matriz)
    i += 1
  return(matriz)

matriz_carros = []
matriz_carros = abrir('carros.txt')

def calcular_combustivel():
  calculos_comb = []
  i = 0
  while i < 6: 
    gasto_comb = (10000 / float(matriz_carros[i][3])) * 3.98
    calculos_comb.append(gasto_comb)
    i += 1
  return(calculos_comb)

calculos_comb = []
calculos_comb = calcular_combustivel()

def calcular_gasto_total():
  totais = []
  i = 0
  while i < 6:
    gasto_total = float(matriz_carros[i][1]) + float(matriz_carros[i][2]) + float(matriz_carros[i][4]) + calculos_comb[i]
    totais.append(gasto_total)
    i += 1
  return(totais)

totais = []
totais = calcular_gasto_total()

def imprimir_resultado():
  i = 0
  while i < 6:
    print(f'\nVeículo {matriz_carros[i][0]}- Custou R${matriz_carros[i][1]}- O valor de impostos foi de R${matriz_carros[i][2]}- O consumo médio de combustível em Km/L é {matriz_carros[i][3]}- O gasto com combustível em um ano é R${round(calculos_comb[i], 2)}\n- O gasto com seguro é R${matriz_carros[i][4]}- O gasto total em um ano é de R${round(totais[i], 2)}\n')
    print('===================== // =====================')
    i += 1
  mais_barato = min(totais)
  j = totais.index(mais_barato)
  print(f'\nO veículo com o custo mais barato é: \nVeículo {matriz_carros[j][0]}- O gasto total em um ano é de R${round(totais[j], 2)}\n- Custou R${matriz_carros[j][1]}- O valor de impostos foi de R${matriz_carros[j][2]}- O consumo médio de combustível em Km/L é {matriz_carros[j][3]}- O gasto com combustível em um ano é R${round(calculos_comb[j], 2)}\n- O gasto com seguro é R${matriz_carros[j][4]}\n')
  
imprimir_resultado()

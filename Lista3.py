#Exerc�cio 1

valor_conta = float(input('Informe o valor total da conta: '))
num_pessoas = int(input('Informe o n�mero de pessoas na mesa: '))
valor_total_10_cento = valor_conta + (valor_conta * 0.1)
valor_individual = valor_total_10_cento / num_pessoas
print('\n*******************************')
valor_individual = round(valor_individual, 2)
valor_total_10_cento = round(valor_total_10_cento, 2)
print(f'\nO valor total da conta � R${valor_conta}. \nO valor total a ser pago, com os 10% � R${valor_total_10_cento}. \nA quantidade de pessoas na mesa � {num_pessoas} pessoa(s). \nO valor individual a pagar com os 10% � R${valor_individual}')


#Exerc�cio 2

nome = input('Informe o nome: ')
idade = int(input('Informe a idade: '))
if idade > 17 and idade < 66:
    print(f'\n{nome} � eleitor(a) obrigat�rio(a).')
elif idade < 16: 
    print(f'\n{nome} n�o � eleitor(a).')
else: 
    print(f'\n{nome} � eleitor(a) facultativo(a).')


#Exerc�cio 3

nomes = []
notas = []

def incluir_nomes():
  nome = input('Informar nome: ')
  nomes.append(nome)

def incluir_notas():
  nota = int(input('Informar nota: '))
  notas.append(nota)

def informar_resultado():
  resultado_nota = max(notas)
  i = notas.index(resultado_nota)
  resultado_nome = nomes[i]
  print(f'A pessoa que venceu � {resultado_nome} com a nota {resultado_nota}.')

for i in range(10):
  incluir_nomes()
  incluir_notas()

informar_resultado()

#Exerc�cio 4 - Calculo de empre�stimo

sal_bruto = float(input("Informar o salario bruto: "))
parcela = float(input("Informar o valor da parcela: "))

def calcular_emprestimo():
  perc_sal_parcela = (parcela / sal_bruto) * 100
  if perc_sal_parcela <= 30:
    print("\nO empr�stimo pode ser realizado.")
  else:
    print("\nO empr�stimo n�o pode ser realizado.")
  print(f"\nO sal�rio bruto � R${sal_bruto}.\nA parcela mensal � R${parcela}.\nO percentual que a parcela compromete do sal�rio � {round(perc_sal_parcela, 2)}%")

calcular_emprestimo()
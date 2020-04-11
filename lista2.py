
"""1) Crie um algoritmo que leia um número e mostre se o mesmo é positivo, negativo ou zero."""

x = float(input("Insira o número: "))
if (x > 0):
  print("O número é positivo")
elif (x < 0):
  print("O número é negativo")
else:
  print("O número é zero")

"""2)Crie um algoritmo que leia um número e mostre se o mesmo é par ou ímpar."""

num1 = int(input("Insira o numero: "))
div1 = num1 % 2
if (div1 == 0):
  print("Número par")
else:
  print("Número impar")

"""3) Crie um algoritmo que leia dois números e mostre o maior número."""

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
if (num1 > num2):
  print(f"O primeiro número {num1} é maior do que o segundo número {num2}")
else:
  print(f"O segundo número {num2} é maior do que o primeiro número {num1}")

"""4) Crie um algoritmo que leia três números e mostre o maior número."""

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))
if (num1 >= num2 and num1 >= num3) :
  print(f"O {num1} é o maior de todos")
# elif (num2 >= num1 and num2 >= num3) :
elif (num2 >= num3) :
  print(f"O {num2} é o maior de todos")
else:
  print(f"O {num3} é o maior de todos")

"""5) Crie um algoritmo que leia três números e mostre-os em ordem crescente."""

a = float(input("Insira o primeiro número: "))
b = float(input("Insira o segundo número: "))
c = float(input("Insira o terceiro número: "))

maior = 0
meio = 0
menor = 0

if a >= b and a >= c :
  maior = a
  if b >= c :
   meio = b
   menor = c
  else:
    meio = c
    menor = b
elif b >= c :
  maior = b
  if a >= c :
    meio = a
    menor = c
  else:
    meio = c
    menor = a
else:
  maior = c
  if a >= b :
    meio = a
    menor = b
  else: 
    meio = b
    menor = a

print(f"O menor numero é {menor}")
print(f"O número do meio é {meio}")
print(f"O maior número é {maior}")

"""6) Crie um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não."""

letra = input("Insira a letra: ")
letra = letra.upper()
#print(letra)

if letra in ("A", "E", "I", "O", "U"):
#if letra == "a" or "e" or "i" or "o" or "u" :

  print("A letra digitada é uma vogal")
else: 
  print("A letra digitada é uma consoante")

"""Crie um algoritmo que calcule e mostre o novo valor de um salário a partir das seguintes regras: salários de até R$ 1.000,00 inclusive recebem 30 % 
de aumento, salários de até R$ 2.000,00 inclusive recebem 25%, 
salários de até R$ 3.000,00 inclusive recebem 20%, 
salários de até R$ 4.000,00 inclusive recebem 15% 
e salários acima de R$ 4.000,00 recebem apenas 10%.
"""


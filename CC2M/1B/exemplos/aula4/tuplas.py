'''
Tuplas - É uma coleção ordenada, não-modificável e que permite duplicatas.
'''

frutas = ("pera", "banana", "morango", "banana", "laranja", "manga")

print(frutas)
print(type(frutas))

print(frutas[2])
print(frutas[2:4])

carros = ("cerato")
print(type(carros))

if "manga" in frutas:
  print('A manga está na lista de frutas.')
else:
  print('A manga não está na lista de frutas.')

frutas = list(frutas)

print(frutas)
print(type(frutas))

frutas[2] = "tomate"
print(frutas)

frutas = tuple(frutas)
print(frutas)
print(type(frutas))

minhas_compras = ("carne", "cerveja", "carvao")
compras_da_patroa = ("creme", "shampoo", "condicionador")

compras_da_casa = minhas_compras + compras_da_patroa

print(compras_da_casa)

carros = ("cerato", "corola", "civic", "fusca")

# (c1, c2, c3, c4) = carros

# print(c1)
# print(c2)
# print(c3)
# print(c4)

# for c in carros:
#   print(c)

# for i in range(len(carros)):
#   print(carros[i])

carros = carros * 2

for c in carros:
  print(c)

print(carros.count("cerato"))
print(carros.index("cerato"))
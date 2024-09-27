'''
lists - varios valores numa única variável
'''

nomes = ["wagner", "gabriel", "arthur", "joão"]

print(nomes[1])

nomes[1] = "antonio"

print(nomes[1])

print(nomes)

print(f"Minha lista possui {len(nomes)} pessoas")

lista = ["wagner", 39, True]

print(lista)

print(type(lista))

print(nomes[-1])

print(nomes[-4:-1])

#in
if "arthur" in nomes:
  print("eu conheço o arthur")
else
  print("eu não conheço o arthur")


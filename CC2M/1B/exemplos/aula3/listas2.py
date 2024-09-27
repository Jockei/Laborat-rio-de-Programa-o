nomes = ["wagner", "gabriel", "arthur", "joão", "wagner", "pedro"]

print('### iterando con for in ###')
for nome in nomes:
  print(nome)

print('### iterando pelo indice ###')
for i in range(len(nomes)):
  print(nomes[i])

print('### iterando con while ###')
i = 0
while i < len(nomes):
  print(nomes[i])
  i += 1

#short hand for
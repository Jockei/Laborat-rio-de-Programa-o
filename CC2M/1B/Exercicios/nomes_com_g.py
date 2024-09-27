nomes = ['wagner', 'carlos', 'antonio', 'jose', 'wellington']

nomes_con_G = []

for i in range(len(nomes)):
  if nomes[i].find('g') != -1 or nomes[i].find('G') != -1:
    nomes_con_G.append(nomes[i])

print(nomes_con_G)
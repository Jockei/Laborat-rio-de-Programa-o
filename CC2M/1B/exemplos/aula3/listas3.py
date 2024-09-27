nomes = ['wagner', 'carlos', 'antonio', 'jose', 'wellington']

nome_com_g = []

'''
gera uma nova lista contendo apenas os nomes que estão na lista
nomes e possuem a letra "g" no nome
'''

for nome in nomes:
  if "g" in nome:
    nome_com_g.append(nome)

print(nome_com_g)


nomes = ['wagner', 'carlos', 'antonio', 'jose', 'wellington']

nome_com_g = [nome for nome in nomes if "g" in nome]

print(nome_com_g)
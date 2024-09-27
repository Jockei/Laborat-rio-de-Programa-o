import csv

clientes = [
  {'nome' : 'João', 'Idade' : 28, 'cidade' : 'Serra'},
  {'nome' : 'Maria', 'Idade' : 32, 'cidade' : 'Vitoria'},
  {'nome' : 'Antônio', 'Idade' : 25, 'cidade' : 'Cariacica'},
  {'nome' : 'Jose', 'Idade' : 19, 'cidade' : 'Vila Valha'}
]

arquivo = 'clientes.csv'

with open(arquivo, mode='w', newline='') as file:
  writter = csv.DictWriter(file, fieldnames=['nome', 'Idade', 'cidade'])
  writter.writeheader()
  writter.writerows(clientes)

print(f'Arquivo {arquivo} criado com sucesso!')
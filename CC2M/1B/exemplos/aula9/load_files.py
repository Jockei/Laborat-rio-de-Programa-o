import csv
import pandas as pd

arquivo = "clientes.csv"

with open(arquivo, mode='r', newline='') as file:
  reader = csv.DictReader(file)
  clientes = list(reader) #[linha for linha in reader]

print('Dados carregados com sucesso!')
for cliente in clientes:
  print(cliente)

df = pd.DataFrame(clientes)

print(df)

print(df[[ 'nome', 'Idade' ]])
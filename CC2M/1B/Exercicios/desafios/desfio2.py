def soma_n(lista, valor):
  ordem = []
  inverter = []
  lista = sorted(lista)
  
  for i in range(len(lista)):
    for j in range(len(lista)):
      if lista[i] + lista[j] == valor and lista[i] != lista[j]:

        if ordem != [] and lista[i] == ordem[-1][-1] and lista[j] == ordem[-1][0]:
          for x in range(len(inverter)):
            ordem.append(inverter[x])
          return ordem

        ordem.append((lista[i], lista[j]))
        inverter.insert(0, (lista[j], lista[i]))

numeros = [5, 2, 3, 7, 8, 4, 1, 9]
print(soma_n(numeros, 10))
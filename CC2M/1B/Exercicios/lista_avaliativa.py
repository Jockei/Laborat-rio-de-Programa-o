# 1. Inicialização de Matriz

def criar_matriz(linhas, colunas, valor):
  result = []
  for i in range(linhas):   
    result.append([])
    for j in range(colunas):
        result[i].append(valor)
  return result

#print (criar_matriz(3, 4, 0))

# 2. Verificação de Matriz Identidade

def e_matriz_identidade(matriz):
  value = True
  index = 0
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      index += matriz[i][j]
  if index != len(matriz):
    value = False
  print(value)

#e_matriz_identidade([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

# 3. Extração da Diagonal da Matriz

def extrair_diagonal(matriz):
  x = matriz[0][0]
  y = matriz[1][1]
  z = matriz[2][2]
  print(x, y, z)

#extrair_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 4. Cálculo do Traço da Matriz
def calcular_traco(matriz):
  traco = 0
  for i in range(len(matriz)):
    traco += matriz[i][i]
  print(traco)

#calcular_traco([[1, 2], [3, 4]])

# 5. Verificação de Matriz Nula
def e_matriz_nula(matriz):
  value = True
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if matriz[i][j] != 0:
        value = False
  print(value)

#e_matriz_nula([[0, 0], [0, 0]])

# 6. Multiplicação de Matriz por Escalar
def multiplicar_escalar(matriz, escalar):
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      matriz[i][j] *= escalar
  print(matriz)

#multiplicar_escalar([[1, 2], [3, 4]], 3)

# 7. Soma das Linhas e Colunas da Matriz
def soma_linhas(matriz):
  for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz[i])):
      soma += matriz[i][j]
    print(f'Linha {i}: {soma}')

#soma_linhas([[1, 2, 3], [4, 5, 6]])

def soma_colunas(matriz):
    num_colunas = len(matriz[0])
    for i in range(num_colunas):
        soma = 0
        for j in range(len(matriz)):
            soma += matriz[j][i]
        print(f'Coluna {i}: {soma}')

#soma_colunas([[1, 2, 3], [4, 5, 6]])

# 8. Verificação de Matriz Esparsa
def e_matriz_esparsa(matriz):
  total_elementos = len(matriz) * len(matriz[0])
  elementos_zero = 0

  for i in range(len(matriz)):
      for j in range(len(matriz[i])):
          if matriz[i][j] == 0:
              elementos_zero += 1

  if elementos_zero > total_elementos / 2:
      print("True")
  else:
      print("False")

#e_matriz_esparsa([[1, 1, 1], [1, 1, 0], [0, 0, 0]])

# 9. Rotação de Matriz (90 Graus)
def rotacionar_matriz_90(matriz):
    matriz_rotacionada = []
    for i in range(len(matriz[0])):
        nova_linha = []
        for j in range(len(matriz) - 1, -1, -1):
            nova_linha.append(matriz[j][i])
        matriz_rotacionada.append(nova_linha)

    for linha in matriz_rotacionada:
        print(linha)

#rotacionar_matriz_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 10.Verificação de Simetria de Matriz
def e_matriz_simetrica(matriz):
    if len(matriz) != len(matriz[0]):
        print(False)
        return

    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                print(False)
                return
    print(True)

#e_matriz_simetrica([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
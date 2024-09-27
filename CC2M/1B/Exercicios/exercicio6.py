'''
1) Crie uma função que receba uma matriz 3X3 e um número referente à diagonal.
A função deve retornar a multiplicação de todos os valores da diagonal.
'''
def multiplicar_diagonal(matriz, diagonal):
  if diagonal == 1:
    return matriz[0][0] * matriz[1][1] * matriz[2][2]
  elif diagonal == 2:
    return matriz[0][1] * matriz[1][2] * matriz[2][0]
  elif diagonal == 3:
    return matriz[0][2] * matriz[1][0] * matriz[2][1]
  elif diagonal == -1:
    return matriz[0][2] * matriz[1][1] * matriz[2][0]
  elif diagonal == -2:
    return matriz[0][1] * matriz[1][0] * matriz[2][2]
  elif diagonal == -3:
    return matriz[0][0] * matriz[1][2] * matriz[2][1]

#print (multiplicar_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))

'''
2) Crie uma função que calcule determinante de uma mariz,
utilizando a função da 1) para os calculos diagonais.
'''

def determinante(matriz):
  # multiplicação das diagonais 

    x = matriz[0][0] * matriz[1][1] * matriz[2][2]
    y = matriz[0][1] * matriz[1][2] * matriz[2][0]
    z = matriz[0][2] * matriz[1][0] * matriz[2][1]
    a = matriz[0][2] * matriz[1][1] * matriz[2][0]
    b = matriz[0][1] * matriz[1][0] * matriz[2][2]
    c = matriz[0][0] * matriz[1][2] * matriz[2][1]
    # soma das diagonais
    soma = x + y + z - a - b - c
    print (soma)

determinante([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
'''
(1) Crie uma função chamda matrix_addition(A, B) que recebe matrizes da mesma dimensão,
calcule e retorne uma matrix com a soma das duas.
(2) Crie uma função chmada matrix_traspose(A) que retorne a matrix trasposts de A.
(3) Crie uma função chamda matrix_multipy(A, B) que retorne a matrix multiplic de A e B.
'''

def matrix_addition(A, B):
  if(len(A) != len(B) or len(A[0]) != len(B[0])):
    return None
  result = []
  for i in range(len(A)):   
    result.append([])
    for j in range(len(A[0])):
        result[i].append(A[i][j] + B[i][j])
  return result

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_addition(A, B))

def matrix_traspose(A):
  result = []
  for i in range(len(A[0])):   
    result.append([])
    for j in range(len(A)):
        result[i].append(A[j][i])
  return result

A = [[1, 2], [3, 4], [5, 6]]
print(matrix_traspose(A))

def martix_multipy(A, B):
  C = []
  for i in range(len(A)):
    C.append([])
    for j in range(len(B[0])):
      C[i].append(0)
      for k in range(len(B)):
        C[i][j] += A[i][k] * B[k][j]
  return C

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(martix_multipy(A, B))
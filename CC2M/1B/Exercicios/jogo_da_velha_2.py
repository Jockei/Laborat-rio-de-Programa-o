import os
import time
import random

# criar tabela
os.system('clear')
velha = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
def imprimir_velha(velha):
  print('  0   1   2')
  print('0 ' + velha[0][0] + ' | ' + velha[0][1] + ' | ' + velha[0][2])
  print('  ---------')
  print('1 ' + velha[1][0] + ' | ' + velha[1][1] + ' | ' + velha[1][2])
  print('  ---------')
  print('2 ' + velha[2][0] + ' | ' + velha[2][1] + ' | ' + velha[2][2])

# calcular vitoria
def vitoria():
  for i in range(len(velha)):
      if velha[i][0] == velha[i][1] == velha[i][2] != ' ':
        print(f'Jogador {velha[i][0]} venceu!')
        return False

      if velha[0][i] == velha[1][i] == velha[2][i] != ' ':
        print(f'Jogador {velha[0][i]} venceu!')
        return False

      if velha[0][0] == velha[1][1] == velha[2][2] != ' ':
        print(f'Jogador {velha[0][0]} venceu!')
        return False

      if velha[0][2] == velha[1][1] == velha[2][0] != ' ':
        print(f'Jogador {velha[0][2]} venceu!')
        return False
  return True
  
# jogador X
def jogador_X():
  print('Vez do jogador X')
  i = input('Digite a linha(0, 1 ou 2): ')
  j = input('Digite a coluna(0, 1 ou 2): ')
  try:
    if velha[int(i)][int(j)] == ' ':
      velha[int(i)][int(j)] = 'X'
    else: 
      print('Posição já está ocupada')
      imprimir_velha(velha)
      jogador_X()
  except Exception as e:
    print(e)
    time.sleep(2)
    os.system('clear')
    imprimir_velha(velha)
    jogador_X()
  os.system('clear')

# Computador
def computador():    
  print('Vez do computador')
  i = random.randint(0, 2)
  j = random.randint(0, 2)

  try:
    if velha[int(i)][int(j)] == ' ':
      velha[int(i)][int(j)] = 'O'
    else:
      imprimir_velha(velha)
      computador()
  except Exception as e:
    print(e)
    os.system('clear')
    imprimir_velha(velha)
    computador()
  os.system('clear')
  
# Empate
def empate():
  ordenar = 0
  for i in range(3):
    for j in range(3):
      if velha[i][j] != ' ':
        ordenar += 1
  if ordenar == 9:
    print('Deu velha!')
    return False
  return True
  
# jogo
imprimir_velha(velha)

Y = True
while Y:
    
  jogador_X()
  if not vitoria():
    break
  imprimir_velha(velha)
  if not empate():
    break
  
  computador()
  if not vitoria():
    break
  imprimir_velha(velha)
  if not empate():
    break
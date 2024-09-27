#--> Exercicio 1
'''
1. Crie um programa que peça ao usuário para digitar seu nome e idade e informe se ele é maior de idade.
'''

#--> Solução
print("Informe o seu nome: ")
nome = input()

print("Informe a sua idade: ")
idade = int(input())

if idade >= 18:
  print("Você é maior de idade!")
  
else:
  print("Você é menor de idade!")
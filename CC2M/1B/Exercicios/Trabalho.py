import csv
import os

import pandas as db

#Ler arquivo
arquivo = "Trabalho.csv"

alunos = []

with open(arquivo, mode='r', newline='') as file:
  reader = csv.DictReader(file)
  alunos = list(reader)

#Menu
def exibeMenu():
  os.system('clear')
  print("0 - Sair\n1 - Cadastrar Aluno\n2 - Listar Alunos\n3 - Busca Alnuo\n4 - Remoção Aluno")

#Cadastrar
def cadastro():
  Y = True
  while Y:
    os.system('clear')
    print("Cadastrar")
    try:
      nome = str(input("Por favor digite o nome do aluno para cadastrar: "))
      ID = int(input("Por favor digite o ID do aluno para cadastrar: "))
      turma = input("Por favor digite a turma do aluno para cadastrar: ")

    except Exception:
      print("\nVocê deve escrever o Nome somente com letras, e o ID somente com numeros\n")
      input("Aperte enter para voltar")

    for aluno in alunos:
      if aluno['ID'] == ID:
        print("Esse ID já existe")
        Y = True
        break
      elif aluno['ID'] != ID:
        Y = False
  
  alunos.append({'nome': nome, 'ID': ID, 'turma': turma})
  
  with open(arquivo, mode='w', newline='') as file:
    writter = csv.DictWriter(file, fieldnames=['nome', 'ID', 'turma'])
    writter.writeheader()
    writter.writerows(alunos)
  for aluno in alunos:
    if aluno['ID'] == ID:
      df = db.DataFrame([aluno]).sort_values(by=['ID']).to_string(index=False)
      print(f"\n{df}\n")

#Listar
def listar():
  os.system('clear')
  print("Listar")
  print("1 - ID")
  print("2 - Nome")
  print("3 - Turma")

  try:
    opcao = int(input("\nopção: "))

    if opcao == 1:
      df = db.DataFrame(alunos).sort_values(by=['ID']).to_string(index=False)
      print(f"\n{df}\n")
      input("Aperte enter para continuar")

    elif opcao == 2:
      df = db.DataFrame(alunos).sort_values(by=['nome']).to_string(index=False)
      print(f"\n{df}\n")
      input("Aperte enter para continuar")

    elif opcao == 3:
      df = db.DataFrame(alunos).sort_values(by=['turma']).to_string(index=False)
      print(f"\n{df}\n")
      input("Aperte enter para continuar")
        
  except Exception:
    print("Opção inválida")

#Buscar
def busca():
  os.system('clear')
  print("Busca")
  resultado = []
  try:
    numero = int(input("0 - ID\n1 - Nome\n2 - Turma\n"))
  
    if numero == 0:
      ID_busca = input("Por favor digite o ID do aluno para buscar: ").lower()
      for aluno in alunos:
        if aluno['ID'].lower() == ID_busca:
          resultado.append(aluno)
          
    elif numero == 1:
      nome_busca = input("Por favor digite o Nome do aluno para buscar: ").lower()
      for aluno in alunos:
        if aluno['nome'].lower() == nome_busca:
          resultado.append(aluno)
          
    elif numero == 2:
      turma_busca = input("Por favor digite o Turma do aluno para buscar: ").lower()
      for aluno in alunos:
        if aluno['turma'].lower() == turma_busca:
          resultado.append(aluno)
  
    if resultado != []:
      df = db.DataFrame(resultado).sort_values(by=['ID']).to_string(index=False)
      print(f"\n{df}\n")
      input("Aperte enter para continuar")

    else:
      print("\nNão foi encontrado esse aluno")
      input("Aperte enter para voltar")
      busca()
      
  except Exception:
    print("\nDigite um numero")
    input("Aperte enter para voltar")
    busca()

#Remover
def remover():
  os.system('clear')
  print("Remoção")
  df = db.DataFrame(alunos).sort_values(by=['ID']).to_string(index=False)
  print(f"\n{df}\n")
  ID_remover = input("Por favor digite o ID do aluno para remover: ")
  for aluno in alunos:
    if aluno['ID'] == ID_remover:
      alunos.remove(aluno)
      print(f"Aluno {aluno['nome']} removido com sucesso!")
      with open(arquivo, mode='w', newline='') as file:
        writter = csv.DictWriter(file, fieldnames=['nome', 'ID', 'turma'])
        writter.writeheader()
        writter.writerows(alunos)

while True:
  exibeMenu()
  op = int(input("Escolha uma opção: "))
  if op >= 0 and op <= 4:
    if op == 0:
      break
    elif op == 1:
      cadastro()
    elif op == 2:
      listar()
    elif op == 3:
      busca()
    elif op == 4:
      remover()
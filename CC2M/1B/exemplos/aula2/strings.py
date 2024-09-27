nome = 'Gabriel'
sobrenome = 'Henrique'

texto = 'Renato é um "bom" aluno'

#using escape

texto = "Renato é um \"bom\" aluno \\"

print(texto)

#in operator

print('Renato' in texto)

alunos = "Gabriel, Francisco, Joao, Renato"

if 'Gabriel' in alunos:
  print('Gabriel estava na aula')

#slicing - Recorte de Strings
nome_completo = "Wagner Perin"

print(nome_completo[7:])
print(nome_completo[0:6])
print(nome_completo[-5:])

print(nome_completo.upper())

print(nome_completo.replace('w', 'v'))
print(nome-completo)

nome_completo = nome_completo.replace('w', 'v')
print(nome_completo)


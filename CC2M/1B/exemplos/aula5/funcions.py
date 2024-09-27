'''
Função - É um bloco de código que executa uma tarefa específica.
* Você pode passar dados para uma função e ela pode retornar dados de volta.
'''

def incluir_sobrenome(nome):
  print(nome + " Perin")

incluir_sobrenome("Wagner")
incluir_sobrenome("Eloit")
incluir_sobrenome("Gael")
incluir_sobrenome("Elaine")

def imprime_nome_completo(nome, sobrenome):
  print("Seu nome completo é: " + nome + " " + sobrenome)

imprime_nome_completo("Wagner", "Perin")

def minha_funcao(*args):
  print("Teste: " + args[2])

minha_funcao("Arg 1", "Arg 2", "Arg 3", "Arg 4")

def minha_func2(arg1, arg2, arg3):
  print("Arg 1: " + arg1)
  print("Arg 2: " + arg2)
  print("Arg 3: " + arg3)

minha_func2(arg2="Valor 2", arg1="Valor 1", arg3="Valor 3")

def minha_func3(arg1="", arg2=""):
  print("Arg 1: " + arg1)
  print("Arg 2: " + arg2)

minha_func3(arg2="Teste 1")

def minha_func4(**args):
  print("Seu nome completo é: " + args["nome"] + " " + args["sobrenome"])

minha_func4(nome="Wagner", sobrenome="Perin", idade = 39, profissao = "Professor")
x = 5

try:
  print(x)
  a = 10/0
except NameError as ne:
  print('Ocorreu o seguinte erro: '+ repr(ne))
except ZeroDivisionError as zde:
  print('Ocorreu o seguinte erro: '+ repr(zde))
else:
  print('Deu tudo certo!')
finally:
  print('Essa vai ser a ultima mensagem.')
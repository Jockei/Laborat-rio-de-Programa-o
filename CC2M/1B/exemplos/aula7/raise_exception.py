def check_person(**person):
  if person['age'] < 0:
    raise Exception('Idade invalida')
  else:
    return True

try:
  if check_person(name= "Wagner", surname="Perin", age=-5):
    print('Tudo ok.')
  else:
    print('Tá errado cara.')
except:
  print('Algo de errado aconteceu.')
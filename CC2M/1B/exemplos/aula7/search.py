def is_on_list(list, value):
  el_found = False
  count = 0

  for element in list:
    count = count + 1
    if element == value:
      el_found = True
      break

  print(f'Finalizou com {count} voltas')
  return el_found

students = ['Renato', 'Leo', 'Arthur', 'Gabriel', 'Gustvo']

if is_on_list(students, 'Leo'):
  print('Leo está na lista.')
else:
  print('Não está na lista.')
def func():
  print("Função 1")

def func2():
  print("Função 2")
  func()

func2()

def r_func(n):
  print("Chmada " + str(n))
  if n > 0:
    r_func(n-1)

r_func(100)
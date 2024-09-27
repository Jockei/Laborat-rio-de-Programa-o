'''
DataTypes:
- Text: str
- Numeric: int, float, complex
- Sequence: list, tuple. range
- Mapping: dict
- Set: set, frozenset
- Boolean: bool
- Binary: bytes, bytearray, memoryview
- Nome: NoneType
'''

X = 5
Y = 5.5

print(type(X))
print(type(Y))

nomes = ['Renato', 'Gabriel', 'Arthur']

print(type(nomes))

aluno = {
  'nome': 'Renato',
  'idade': 18,
  'nota': 10
}

print(type(aluno))

vazia = None

print(type(vazia))
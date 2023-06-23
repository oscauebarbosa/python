pessoa = {'Nome':'Duda',
          'Idade':16,
          'Altura':1.50}

for k in pessoa.keys():
    print(k)

for v in pessoa.values():
    print(v)

for k,v in pessoa.items():
    print(f'O item {k} é {v}')
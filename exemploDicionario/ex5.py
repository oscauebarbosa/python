pessoa = {'Nome':'Duda', 'Idade':16, 'Altura':1.50}
idade = int(input('Digite sua idade:'))

if idade in pessoa.values():
    print('Você tem a mesma idade que a Duda')
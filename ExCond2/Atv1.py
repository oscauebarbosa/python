time1= int(input('Insira os pontos do primeiro time: '))
time2= int(input('Insira os pontos do segundo time: '))

if time1 > time2:
    print(f'Vitória do primeiro time')
elif time1 < time2:
    print(f'Vitória do segundo time')
else:
    print('Os times empataram')
from conversor import conversao
tem = int(input("1-Converter de celsius para fahrenheit\n2-Converter de fahrenheit para celsius\nR:"))
num = int(input("Grau que será convertido:"))

if tem == 1:
    cf = conversao.celsius_para_fahrenheit(num)
    print(f"{cf}°F")
elif tem == 1:
    fc = conversao.fahrenheit_para_celsius(num)
    print(f"{fc}°C")
else:
    print("ERRO")
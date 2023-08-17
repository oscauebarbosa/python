import geometria.formas

operacao = int (input("Digite 1 para área do círculo e 2 para a do quadrado: "))
if operacao == 1:
    r = int (input("Digite o raio do círculo: "))
    areac = geometria.formas.area_circulo(r)
    print(areac)
elif operacao== 2:
    l = int (input("Digite o lado do quadrado: "))
    areaq = geometria.formas.area_quadrado(l)
    print(areaq)
import customtkinter as tk

import Modulos as j
valor = 0
def prox():
    global valor
    valor +=0.1
    barra.set(valor)
def antes():
    global valor
    valor -= 0.1
    barra.set(valor)

janela = j.CriarJanela('Opa','300x500',1)
barra = j.CriarProgressBar(janela,200,10,3,6)
barra.set(0)
j.CriarBotão(janela,'Anterior',antes,200,35,4,6,'red')
j.CriarBotão(janela,'Próximo',prox,200,35,5,6,'red')








janela.mainloop()












janela.mainloop()
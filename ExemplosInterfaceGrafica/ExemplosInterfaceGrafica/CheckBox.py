import customtkinter as Tk

from Modulos import *


def clique():
    if check1.get() ==1:
        label1.configure(text="Marcado")
    else:
        label1.configure(text="Desmarcado")



janela = CriarJanela("Mafi","500x400",1)


check1 = Tk.CTkCheckBox(janela, text="Marque")
check1.grid (row=4, column=6)
check1.get()

btn = CriarBotão(janela, "Enviar", clique, 100, 30, 8,6)

label1 = CriarLabel(janela, "", 5, 6)















janela.mainloop()
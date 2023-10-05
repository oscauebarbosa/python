from Modulos import *

def clique():
    if Switch1.get() ==1:
        label1.configure(text="Marcado")
    else:
        label1.configure(text="Desmarcado")


janela = CriarJanela("Mafi","500x400",1)


Switch1 = Tk.CTkSwitch(janela, text="Marque")
Switch1.grid (row=4, column=6)
Switch1.get()

btn = CriarBotão(janela, "Enviar", clique, 8, 6, 100, 30)

label1 = CriarLabel(janela, "", 5, 6)















janela.mainloop()

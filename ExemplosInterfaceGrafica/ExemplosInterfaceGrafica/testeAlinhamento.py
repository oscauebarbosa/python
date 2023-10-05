from Modulos import *

Janela = CriarJanela("Janela do dia 5", "500x500", 1)

frame = CriarFrame(Janela, 0, 0, 500, 100)
frame.configure(fg_color=Janela.cget("bg"), corner_radius=0)
frame.grid(sticky="N", columnspan=13)

label = CriarLabel(frame, "Nome:", 5, 6)
label.grid(sticky="SW")

caixa = CriarCaixaDeTexto(frame, 200, 30, 6, 6, Modo="CPF")
caixa.grid(sticky="NW")










Janela.mainloop()
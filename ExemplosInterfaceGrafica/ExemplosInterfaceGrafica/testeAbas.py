from Modulos import *

Janela = CriarJanela("Janela do dia 5", "500x500", 1)

frame = CriarFrame(Janela, 0, 0, 500, 100)
frame.configure(fg_color=Janela.cget("bg"), corner_radius=0)
frame.grid(sticky="N", columnspan=13)


aba = CriarAbas(Janela, 2, 2, 200, 200,
                "Um", "Dois", "Três")
lb_Um = CriarLabel(aba.tab("Um"),
                   "AOBA BOI", 6, 6)
lb_Dois = CriarLabel(aba.tab("Dois"),
                   "AOBA VACA", 6, 6)
lb_Tres = CriarLabel(aba.tab("Três"),
                   "AOBA BEZERRO", 6, 6)










Janela.mainloop()
import customtkinter as tk
from ModuloIF import *
tk.set_appearance_mode("System")


def Clicar():
    Tela1.withdraw()
    Tela2.deiconify()

def AlterarTema():
    T = Switch_Tela1.get()
    if T == 0:
        tk.set_appearance_mode("Dark")
    else:
        tk.set_appearance_mode("Light")

Tela1 = CriarJanela("Tela 1", "600x600+500+50", 1)
Lb_Tela1 = CriarLabel(Tela1, "Texto 1", 1, 6)
Lb_Tela1.configure(text_color="Gray", font=("arial", 18, "bold"))

Btn_Tela1 = CriarBotao(Tela1, "Clicar", Clicar, 100, 30, 2, 6)
Btn_Tela1.configure(fg_color="Blue", hover_color="Purple")

Caixa_Tela1 = CriarCaixaTexto(Tela1, 200, 30, 4, 6, 'CPF', Modo="CPF")

Switch_Tela1 = CriarSwitch(Tela1, "Alterar Tema", 5, 6, AlterarTema)

ListaNomes = ['Audi', 'Mits', 'Ferrari', 'Chev', 'Nissan']
Combo_Tela1 = CriarComboBox(Tela1, 200, 30, ListaNomes, 6, 6)

Slider_Tela1 = CriarSlider(Tela1, 400, 10, 7, 6)

BarraProgresso = CriarProgressBar(Tela1, 500, 20, 8, 6)

Imagem_Tela1 = CriarImagem(Tela1, "cat.jpg", 9, 6, 250, 250)


#---------------------------TELA 2----------------------------------

Tela2 = CriarJanela("Tela 2", "600x600+500+50", 2)
Tela2.withdraw()






















Tela1.mainloop()
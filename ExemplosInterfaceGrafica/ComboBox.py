import customtkinter as Tk

from ModuloIF import *
tk.set_appearance_mode("System")

janela=CriarJanelaP("Milim sem WIFI","400x300",1)
Lista = ["Item 1", "Item 2", "Item 3", "Item 4"]
combo = CriarComboBox(janela,Lista,100,30,6,6)






janela.mainloop()
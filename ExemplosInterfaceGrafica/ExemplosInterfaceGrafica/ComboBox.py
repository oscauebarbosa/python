import customtkinter as tk

from Modulos import *

janela = CriarJanela("Milim sem WIFI", "400x300", 1)
Lista = ["Item 1", "Item 2", "Item 3", "Item 4"]
combo = CriarComboBox(janela,100,30, Lista, 6, 6)





janela.mainloop()
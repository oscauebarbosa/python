import customtkinter as Tk
from ModuloIF import *
tk .set_appearance_mode("System")



progress = Tk.CTkProgressBar(janela, width=200, height=10)
progress.grid(row=7, columns= 6)
progress.set(0)
progress.set(1)
progress.set(0.2)












janela.mainloop()
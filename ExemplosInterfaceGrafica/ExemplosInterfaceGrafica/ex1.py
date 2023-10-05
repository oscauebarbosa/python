import customtkinter as tk

tk .set_appearance_mode("System")

janela = tk.CTk()
janela.title ("Janela 1")
janela.geometry("400x350")

janela.configure(fg_color="Black")
janela.resizable(width=False, height=False)

colunas = list (range(13))
linhas = list (range(13))
janela.grid_columnconfigure(colunas, weight=1)
janela.grid_rowconfigure(linhas, weight=1)

texto1= tk.CTkLabel(janela, text='CLICA AI RAPAZ')
texto1.grid(row=6, column=6)

texto2= tk.CTkLabel(janela, text='AOBAAA',
                    text_color="White",
                    font=("Arial",15),
                    justify="center")
texto2.grid(row=4, column=6)

def clique():
    texto2.configure(text=caixa1.get())

btn= tk.CTkButton(janela, text="Clique aqui",
                  command= clique,
                  width=50, height=30,
                  fg_color='DarkTurquoise',
                  hover_color='CornflowerBlue',
                  text_color='Black')
btn.grid(row=8, column=6)

caixa1 = tk.CTkEntry(janela, placeholder_text="Digite seu nome",
                     width=200, height=30)
caixa1.grid(row=7, column=6)

















#sempre no final o mainloop
janela.mainloop()
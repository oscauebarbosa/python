#Escreva um programa que pergunte o ano de nascimento de uma pessoa( em uma caixa de texto) e diga se ele é maior de idade(em um label)

import customtkinter as tk
tk.set_appearance_mode("dark")

janela = tk.CTk()
janela.title("Janela 1")
janela.geometry("400x350")
janela.configure(fg_color="black")
janela.resizable(width=False,height=False)
colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas, weight=1)
janela.grid_rowconfigure(linhas, weight=1)



def verificar():
    num1 = int(caixa.get())

    if num1 < 18:
        texto1.configure(text="Você é menor de idade")
    elif 18 < num1:
        texto1.configure(text="Você é maior de idade")



texto = tk.CTkLabel(janela, text="Digite sua idade")
texto.grid(row=6, column=6)

caixa = tk.CTkEntry(janela, placeholder_text="Digite", width=200,height=50)
caixa.grid(row=7, column=6)

texto1 = tk.CTkLabel(janela, text="")
texto1.grid(row=10, column=6)

btn = tk.CTkButton(janela, text="Clique aqui",
                   command = verificar,
                   width=200, height=30,
                   fg_color="blue",
                   hover_color="Navy")
btn.grid(row=9, column=6)




janela.mainloop()
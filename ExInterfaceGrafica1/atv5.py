#Crie um jogo simples em que o computador escolhe um número aleatório e o jogador tenta adivinhar. A janela deve fornecer feedback se o palpite for muito alto ou muito baixo.(Importe o Random e utiilize o RandInt)

import customtkinter as tk
import random

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

num = random.randint(1,100)




def verificar():
    num1 = int(caixa1.get())

    if num1 > num:
        texto1.configure(text="Chute um número mais baixo")
    elif num > num1:
        texto1.configure(text="Chute um número mais alto")
    elif num1 == num:
        texto1.configure(text="Acertou!!!")





texto= tk.CTkLabel(janela, text="Adivinhe o número!")
texto.grid(row=6, column=6)

caixa1=tk.CTkEntry(janela, placeholder_text="Digite",
                   width=200, height=50)
caixa1.grid(row=7, column=6)

btn1= tk.CTkButton(janela, text="Clique aqui",
                   command= verificar,
                   width=100, height=50,
                   fg_color='blue',
                   hover_color="Navy")
btn1.grid (row=9, column=6)

texto1= tk.CTkLabel(janela, text="")
texto1.grid(row=10, column=6)





janela.mainloop()
#Faça um algoritmo que receba um valor de uma compra e receba o numero de prestações, apresente o valor das prestações sem juros. Se o valor for maior da prestação for maior que 500 diga que o usuário não consegue pagar.

import customtkinter as Tk
Tk .set_appearance_mode ("System")

janela = Tk .CTk()
janela.title("Janela 1")
janela.geometry("400x350")
janela.resizable(width=False, height=False)
colunas = list (range(13))
linhas = list (range(13))
janela.grid_columnconfigure(colunas, weight=1)
janela.grid_rowconfigure(linhas, weight=1)



def verificar():
    n1 = int(caixa1.get())
    n2 = int(caixa2.get())

    prest = n1/n2
    if prest > 500 :
        texto1.configure(text="O usuário não consegue pagar")
    else:
        texto1.configure(text="O usuário consegue pagar")




texto1= Tk.CTkLabel(janela, text="Digite...")
texto1.grid(row=6, column=6)


caixa1=Tk.CTkEntry(janela, placeholder_text="Digite o valor",
                   width=200, height=30)
caixa1.grid(row=7, column=6)


caixa2=Tk.CTkEntry(janela, placeholder_text="Digite quantas prestações",
                   width=200, height=30)
caixa2.grid(row=8, column=6)


btn1= Tk.CTkButton(janela, text="Clique aqui",
                   command= verificar,
                   width=100, height=30,
                   fg_color='blue',
                   hover_color="Navy")
btn1.grid (row=9, column=6)




janela.mainloop()
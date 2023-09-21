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

texto1= tk.CTkLabel(janela, text='VEJA QUAL NÚMERO É MAIOR!!!',
                    text_color="White",
                    font=("Arial",15),
                    justify="center")
texto1.grid(row=4, column=6)

texto2= tk.CTkLabel(janela, text='Digite um número em cada caixa de texto!')
texto2.grid(row=6, column=6)



def verificar_maior():
        numero1 = int(num1.get())

        numero2 = int(num2.get())
        if numero1 > numero2:
            resultado_label.configure(text=f"O maior número é {numero1}")
        elif numero2 > numero1:
            resultado_label.configure(text=f"O maior número é {numero2}")
        else:
            resultado_label.configure(text="Os números são iguais")



num1 = tk.CTkEntry(janela, placeholder_text="Primeiro número",width=200, height=30)
num1.grid(row=7, column=6)

num2 = tk.CTkEntry(janela, placeholder_text="Segundo número", width=200, height=30)
num2.grid(row=8, column=6)
resultado_label =tk.CTkLabel(janela,text=" ")
resultado_label.grid(row=10,column =6)

botao = tk.CTkButton(janela, text="Verificar", command=verificar_maior)
botao.grid(row=9,column=6)








#sempre no final o mainloop
janela.mainloop()
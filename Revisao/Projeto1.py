from ModuloIF import *
tk.set_appearance_mode("System")

def Clicar():
    Tela1.withdraw()
    Tela2.deiconify()

def Voltar():
    Tela2.withdraw()
    Tela1.deiconify()

def Cadastrar():
    Tela2.withdraw()
    Tela3.deiconify()





Tela1 = CriarJanela("Tela 1", "600x600+500+50", 1)

def Login():
    L = Email_Tela1.get()
    S = Senha_Tela1.get()
    if Email_Tela1.get() == "Cauê" and Senha_Tela1.get() == "123":
        Tela1.withdraw()
        Tela2.deiconify()
    else:
        LbBranco_Tela1.configure(text="Login e senha incorretos!")


Imagem_Tela1 = CriarImagem(Tela1, "cat.jpg", 1, 6, 250, 250)


Lb_Tela1 = CriarLabel(Tela1, "Login", 2, 6)
Lb_Tela1.configure(text_color="White", font=("arial", 25, "bold"))


LbEmail_Tela1 = CriarLabel(Tela1, "E-mail:", 3, 6)
LbEmail_Tela1.configure(text_color="White", font=("arial", 15, "bold"))
Email_Tela1 = CriarCaixaTexto(Tela1, 200, 30, 4, 6, 'Insira seu e-mail', Modo="")

LbSenha_Tela1 = CriarLabel(Tela1, "Senha:", 5, 6)
LbSenha_Tela1.configure(text_color="White", font=("arial", 15, "bold"))
Senha_Tela1 = CriarCaixaTexto(Tela1, 200, 30, 6, 6, 'Insira sua senha', Modo="Senha")

LbBranco_Tela1 = CriarLabel(Tela1, "", 8, 6)
LbBranco_Tela1.configure(text_color="White", font=("arial", 15, "bold"))



Btn_Tela1 = CriarBotao(Tela1, "Logar", Login, 100, 30, 10, 6)
Btn_Tela1.configure(fg_color="Blue", hover_color="Purple")

Btn_Tela1 = CriarBotao(Tela1, "Cadastrar-se", Clicar, 100, 30, 11, 6)
Btn_Tela1.configure(fg_color="Blue", hover_color="Purple")




#----------------------------------TELA 2----------------------------------


Tela2 = CriarJanela("Tela 2", "600x600+500+50", 2)
Tela2.withdraw()



Imagem_Tela2 = CriarImagem(Tela2, "perfilbloq.jpg", 1, 0, 250, 250)
Imagem_Tela2.grid(columnspan=13)

Lb_Tela2 = CriarLabel(Tela2, "Cadastre-se", 2, 0)
Lb_Tela2.configure(text_color="White", font=("arial", 25, "bold"))
Lb_Tela2.grid(columnspan=13)




LbEmail_Tela2 = CriarLabel(Tela2, "Nome:", 3, 4)
LbEmail_Tela2.configure(text_color="White", font=("arial", 15, "bold"))
Email_Tela2 = CriarCaixaTexto(Tela2, 200, 30, 3, 5, 'Insira seu nome', Modo="")

LbEmail_Tela2 = CriarLabel(Tela2, "E-mail:", 5, 4)
LbEmail_Tela2.configure(text_color="White", font=("arial", 15, "bold"))
Email_Tela2 = CriarCaixaTexto(Tela2, 200, 30, 5, 5, 'Insira seu e-mail', Modo="")

LbEmail_Tela2 = CriarLabel(Tela2, "Senha:", 6, 4)
LbEmail_Tela2.configure(text_color="White", font=("arial", 15, "bold"))
Email_Tela2 = CriarCaixaTexto(Tela2, 200, 30, 6, 5, 'Insira sua senha', Modo="Senha")

LbBranco_Tela2 = CriarLabel(Tela2, "", 8, 6)
LbBranco_Tela2.configure(text_color="White", font=("arial", 15, "bold"))



Btn1_Tela2 = CriarBotao(Tela2, "Cadastrar-se", Cadastrar, 100, 30, 11, 0)
Btn1_Tela2.configure(fg_color="Blue", hover_color="Purple")
Btn1_Tela2.grid(columnspan=13)



Btn2_Tela2 = CriarBotao(Tela2, "Voltar", Voltar, 100, 30, 12, 0)
Btn2_Tela2.configure(fg_color="Blue", hover_color="Purple")
Btn2_Tela2.grid(columnspan=13)



#----------------------------------TELA 3---------------------------------------


Tela3 = CriarJanela("Tela 3", "600x600+500+50", 2)
Tela3.withdraw()


Lb_Tela3 = CriarLabel(Tela3, "LOGADO COM SUCESSO!!!", 2, 6)
Lb_Tela3.configure(text_color="White", font=("arial", 25, "bold"))


Btn_Tela2 = CriarBotao(Tela3, "Voltar", Voltar, 100, 30, 5, 6)
Btn_Tela2.configure(fg_color="Blue", hover_color="Purple")





















Tela1.mainloop()
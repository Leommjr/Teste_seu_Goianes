from tkinter import *
acertos = ["a"]
class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master, bg="black")  #construindo um bloco interativo
        self.widget1.pack(side=TOP) #dando "forma"
        self.widget2 = Frame(master, bg="black")      
        self.widget2.pack(side=TOP)
        self.widget3 = Frame(master, bg="black")
        self.widget3.pack()
        self.widget4 = Frame(master, bg="black")
        self.widget4["height"] = 200
        self.widget4.pack()
        self.msg = Label(self.widget2, text='Teste seu "goianês!"', fg="white", bg="black") #mensagem dentro da caixa
        self.msg["font"] = ("Calibri", "26", "italic")  # a fonte
        self.msg["width"] = 60
        self.widget3["height"] = 200        
        self.msg.pack()
        self.widget5 = Frame(master, bg="black")
        self.widget5["height"] = 100
        self.widget5.pack(side=BOTTOM)   
        self.sair = Button(self.widget5, fg="red")
        self.sair["text"] = "Continuar"
        self.sair["font"] = ("Calibri", "9")
        self.sair.bind("<Button-1>", self.mudarwidget1)
        self.sair.pack()
        
        
        
    def mudarwidget1(self, event):
        self.msg["text"] = 'Primeira Pergunta: O que significa "Dar Trela"?'
        self.sair["text"] = "Nao sei"
        self.op1 = Button(self.widget3, text="  A) Ataque de risos", fg="blue")
        self.op1["width"] = 25
        self.op1.bind("<Button-1>", self.mudarwidget3)
        self.op1.pack()
        self.op2 = Button(self.widget4, text="B) Ajudar", fg="blue")
        self.op2["width"] = 25
        self.op2.bind("<Button-1>", self.mudarwidget4)
        self.op2.pack()
        self.op3 = Button(self.widget4, text="D) Xavecar", fg="blue")
        self.op4 = Button(self.widget4, text="C) Dar Continuidade", fg="blue")
        self.op4.bind("<Button-1>", self.mudarwidget6)
        self.op4.pack(side=LEFT)
        self.op3.bind("<Button-1>", self.mudarwidget5)
        self.op3.pack(side=LEFT)
        self.sair.bind("<Button-1>", self.mudarwidget2)
        self.op3["width"] = 25
        self.op4["width"] = 25

        
        
    def mudarwidget2(self, event):
        self.msg["text"] = 'Segunda Pergunta: O que significa "Queijinho"?'
        self.sair.bind("<Button-1>", self.mudarwidget7)
        self.op1["text"] = "A) Queijo Pequeno"
        self.op2["text"] = "B) Pessoa Que Come Muito Queijo"
        self.op3["text"] = "D) Rua Estreita"
        self.op4["text"] = "C) Rotatória de trânsito"
        self.op1.bind("<Button-1>", self.mudarwidget8)
        self.op2.bind("<Button-1>", self.mudarwidget9)
        self.op3.bind("<Button-1>", self.mudarwidget10)
        self.op4.bind("<Button-1>", self.mudarwidget11)
                
    def mudarwidget3(self, event):
        self.msg["text"] = 'Segunda Pergunta: O que significa "Queijinho"?'
        self.sair.bind("<Button-1>", self.mudarwidget7)
        self.op1["text"] = "A) Queijo Pequeno"
        self.op2["text"] = "B) Pessoa Que Come Muito Queijo"
        self.op3["text"] = "D) Rua Estreita"
        self.op4["text"] = "C) Rotatória de trânsito"
        self.op1.bind("<Button-1>", self.mudarwidget8)
        self.op2.bind("<Button-1>", self.mudarwidget9)
        self.op3.bind("<Button-1>", self.mudarwidget10)
        self.op4.bind("<Button-1>", self.mudarwidget11)
        acertos.append("a")
        print(acertos)
        
               
    def mudarwidget4(self, event):
        self.msg["text"] = 'Segunda Pergunta: O que significa "Queijinho"?'
        self.sair.bind("<Button-1>", self.mudarwidget7)
        self.op1["text"] = "A) Queijo Pequeno"
        self.op2["text"] = "B) Pessoa Que Come Muito Queijo"
        self.op3["text"] = "D) Rua Estreita"
        self.op4["text"] = "C) Rotatória de trânsito"
        self.op1.bind("<Button-1>", self.mudarwidget8)
        self.op2.bind("<Button-1>", self.mudarwidget9)
        self.op3.bind("<Button-1>", self.mudarwidget10)
        self.op4.bind("<Button-1>", self.mudarwidget11)

    def mudarwidget5(self, event):
        self.msg["text"] = 'Segunda Pergunta: O que significa "Queijinho"?'
        self.sair.bind("<Button-1>", self.mudarwidget7)
        self.op1["text"] = "A) Queijo Pequeno"
        self.op2["text"] = "B) Pessoa Que Come Muito Queijo"
        self.op3["text"] = "D) Rua Estreita"
        self.op4["text"] = "C) Rotatória de trânsito"
        self.op1.bind("<Button-1>", self.mudarwidget8)
        self.op2.bind("<Button-1>", self.mudarwidget9)
        self.op3.bind("<Button-1>", self.mudarwidget10)
        self.op4.bind("<Button-1>", self.mudarwidget11)


    def mudarwidget6(self, event):
        self.msg["text"] = 'Segunda Pergunta: O que significa "Queijinho"?'
        self.sair.bind("<Button-1>", self.mudarwidget7)
        self.op1["text"] = "A) Queijo Pequeno"
        self.op2["text"] = "B) Pessoa Que Come Muito Queijo"
        self.op3["text"] = "D) Rua Estreita"
        self.op4["text"] = "C) Rotatória de trânsito"
        self.op1.bind("<Button-1>", self.mudarwidget8)
        self.op2.bind("<Button-1>", self.mudarwidget9)
        self.op3.bind("<Button-1>", self.mudarwidget10)
        self.op4.bind("<Button-1>", self.mudarwidget11)
        
    def mudarwidget7(self, event):
        self.msg["text"] = 'Terceira Pergunta: O que significa "Catilanga"?'
        self.sair.bind("<Button-1>", self.mudarwidget12)
        self.op1["text"] = "A) Fedor"
        self.op2["text"] = "B) Mulher Feia"
        self.op3["text"] = "D) Kombi"
        self.op4["text"] = "C) Mulher Alta"
        self.op1.bind("<Button-1>", self.mudarwidget13)
        self.op2.bind("<Button-1>", self.mudarwidget14)
        self.op3.bind("<Button-1>", self.mudarwidget15)
        self.op4.bind("<Button-1>", self.mudarwidget16)

    
    def mudarwidget8(self, event):
        self.msg["text"] = 'Terceira Pergunta: O que significa "Catilanga"?'
        self.sair.bind("<Button-1>", self.mudarwidget12)
        self.op1["text"] = "A) Fedor"
        self.op2["text"] = "B) Mulher Feia"
        self.op3["text"] = "D) Kombi"
        self.op4["text"] = "C) Mulher Alta"
        self.op1.bind("<Button-1>", self.mudarwidget13)
        self.op2.bind("<Button-1>", self.mudarwidget14)
        self.op3.bind("<Button-1>", self.mudarwidget15)
        self.op4.bind("<Button-1>", self.mudarwidget16)


    def mudarwidget9(self, event):
        self.msg["text"] = 'Terceira Pergunta: O que significa "Catilanga"?'
        self.sair.bind("<Button-1>", self.mudarwidget12)
        self.op1["text"] = "A) Fedor"
        self.op2["text"] = "B) Mulher Feia"
        self.op3["text"] = "D) Kombi"
        self.op4["text"] = "C) Mulher Alta"
        self.op1.bind("<Button-1>", self.mudarwidget13)
        self.op2.bind("<Button-1>", self.mudarwidget14)
        self.op3.bind("<Button-1>", self.mudarwidget15)
        self.op4.bind("<Button-1>", self.mudarwidget16)


    def mudarwidget10(self, event):
        self.msg["text"] = 'Terceira Pergunta: O que significa "Catilanga"?'
        self.sair.bind("<Button-1>", self.mudarwidget12)
        self.op1["text"] = "A) Fedor"
        self.op2["text"] = "B) Mulher Feia"
        self.op3["text"] = "D) Kombi"
        self.op4["text"] = "C) Mulher Alta"
        self.op1.bind("<Button-1>", self.mudarwidget13)
        self.op2.bind("<Button-1>", self.mudarwidget14)
        self.op3.bind("<Button-1>", self.mudarwidget15)
        self.op4.bind("<Button-1>", self.mudarwidget16)


    def mudarwidget11(self, event):
        self.msg["text"] = 'Terceira Pergunta: O que significa "Catilanga"?'
        self.sair.bind("<Button-1>", self.mudarwidget12)
        self.op1["text"] = "A) Fedor"
        self.op2["text"] = "B) Mulher Feia"
        self.op3["text"] = "D) Kombi"
        self.op4["text"] = "C) Mulher Alta"
        self.op1.bind("<Button-1>", self.mudarwidget13)
        self.op2.bind("<Button-1>", self.mudarwidget14)
        self.op3.bind("<Button-1>", self.mudarwidget15)
        self.op4.bind("<Button-1>", self.mudarwidget16)
        acertos.append("a")
        print(acertos)        

        

    def mudarwidget12(self, event):
        self.msg["text"] = 'Quarta Pergunta: O que significa "Maria Izabel"?'
        self.sair.bind("<Button-1>", self.mudarwidget17)
        self.op1["text"] = "A) Mulher Velha "
        self.op2["text"] = "B) Mulher Alta"
        self.op3["text"] = "D) Mulher Interesseira"
        self.op4["text"] = "C) Arroz com Carne de Sol"
        self.op1.bind("<Button-1>", self.mudarwidget18)
        self.op2.bind("<Button-1>", self.mudarwidget19)
        self.op3.bind("<Button-1>", self.mudarwidget20)
        self.op4.bind("<Button-1>", self.mudarwidget21)        


    def mudarwidget13(self, event):
        self.msg["text"] = 'Quarta Pergunta: O que significa "Maria Izabel"?'
        self.sair.bind("<Button-1>", self.mudarwidget17)
        self.op1["text"] = "A) Mulher Velha "
        self.op2["text"] = "B) Mulher Alta"
        self.op3["text"] = "D) Mulher Interesseira"
        self.op4["text"] = "C) Arroz com Carne de Sol"
        self.op1.bind("<Button-1>", self.mudarwidget18)
        self.op2.bind("<Button-1>", self.mudarwidget19)
        self.op3.bind("<Button-1>", self.mudarwidget20)
        self.op4.bind("<Button-1>", self.mudarwidget21)   


    def mudarwidget14(self, event):
        self.msg["text"] = 'Quarta Pergunta: O que significa "Maria Izabel"?'
        self.sair.bind("<Button-1>", self.mudarwidget17)
        self.op1["text"] = "A) Mulher Velha "
        self.op2["text"] = "B) Mulher Alta"
        self.op3["text"] = "D) Mulher Interesseira"
        self.op4["text"] = "C) Arroz com Carne de Sol"
        self.op1.bind("<Button-1>", self.mudarwidget18)
        self.op2.bind("<Button-1>", self.mudarwidget19)
        self.op3.bind("<Button-1>", self.mudarwidget20)
        self.op4.bind("<Button-1>", self.mudarwidget21)   
        acertos.append("a")
        print(acertos)        


    def mudarwidget15(self, event):
        self.msg["text"] = 'Quarta Pergunta: O que significa "Maria Izabel"?'
        self.sair.bind("<Button-1>", self.mudarwidget17)
        self.op1["text"] = "A) Mulher Velha "
        self.op2["text"] = "B) Mulher Alta"
        self.op3["text"] = "D) Mulher Interesseira"
        self.op4["text"] = "C) Arroz com Carne de Sol"
        self.op1.bind("<Button-1>", self.mudarwidget18)
        self.op2.bind("<Button-1>", self.mudarwidget19)
        self.op3.bind("<Button-1>", self.mudarwidget20)
        self.op4.bind("<Button-1>", self.mudarwidget21)   

    def mudarwidget16(self, event):
        self.msg["text"] = 'Quarta Pergunta: O que significa "Maria Izabel"?'
        self.sair.bind("<Button-1>", self.mudarwidget17)
        self.op1["text"] = "A) Mulher Velha "
        self.op2["text"] = "B) Mulher Alta"
        self.op3["text"] = "D) Mulher Interesseira"
        self.op4["text"] = "C) Arroz com Carne de Sol"
        self.op1.bind("<Button-1>", self.mudarwidget18)
        self.op2.bind("<Button-1>", self.mudarwidget19)
        self.op3.bind("<Button-1>", self.mudarwidget20)
        self.op4.bind("<Button-1>", self.mudarwidget21)   
        

    def mudarwidget17(self, event):
        self.msg["text"] = 'Quinta Pergunta: O que significa "Pulá o Corguim"?'
        self.sair.bind("<Button-1>", self.mudarwidget22)
        self.op1["text"] = "A) Passar dos limites "
        self.op2["text"] = "B) Pular o Córrego "
        self.op3["text"] = "D) Experimentar Algo Novo"
        self.op4["text"] = "C) Estar Muito Feliz"
        self.op1.bind("<Button-1>", self.mudarwidget23)
        self.op2.bind("<Button-1>", self.mudarwidget24)
        self.op3.bind("<Button-1>", self.mudarwidget25)
        self.op4.bind("<Button-1>", self.mudarwidget26)


    def mudarwidget18(self, event):
        self.msg["text"] = 'Quinta Pergunta: O que significa "Pulá o Corguim"?'
        self.sair.bind("<Button-1>", self.mudarwidget22)
        self.op1["text"] = "A) Passar dos limites "
        self.op2["text"] = "B) Pular o Córrego "
        self.op3["text"] = "D) Experimentar Algo Novo"
        self.op4["text"] = "C) Estar Muito Feliz"
        self.op1.bind("<Button-1>", self.mudarwidget23)
        self.op2.bind("<Button-1>", self.mudarwidget24)
        self.op3.bind("<Button-1>", self.mudarwidget25)
        self.op4.bind("<Button-1>", self.mudarwidget26)

    def mudarwidget19(self, event):
        self.msg["text"] = 'Quinta Pergunta: O que significa "Pulá o Corguim"?'
        self.sair.bind("<Button-1>", self.mudarwidget22)
        self.op1["text"] = "A) Passar dos limites "
        self.op2["text"] = "B) Pular o Córrego "
        self.op3["text"] = "D) Experimentar Algo Novo"
        self.op4["text"] = "C) Estar Muito Feliz"
        self.op1.bind("<Button-1>", self.mudarwidget23)
        self.op2.bind("<Button-1>", self.mudarwidget24)
        self.op3.bind("<Button-1>", self.mudarwidget26)
        self.op4.bind("<Button-1>", self.mudarwidget27)

    def mudarwidget20(self, event):
        self.msg["text"] = 'Quinta Pergunta: O que significa "Pulá o Corguim"?'
        self.sair.bind("<Button-1>", self.mudarwidget22)
        self.op1["text"] = "A) Passar dos limites "
        self.op2["text"] = "B) Pular o Córrego "
        self.op3["text"] = "D) Experimentar Algo Novo"
        self.op4["text"] = "C) Estar Muito Feliz"
        self.op1.bind("<Button-1>", self.mudarwidget23)
        self.op2.bind("<Button-1>", self.mudarwidget24)
        self.op3.bind("<Button-1>", self.mudarwidget25)
        self.op4.bind("<Button-1>", self.mudarwidget26)

    def mudarwidget21(self, event):
        self.msg["text"] = 'Quinta Pergunta: O que significa "Pulá o Corguim"?'
        self.sair.bind("<Button-1>", self.mudarwidget22)
        self.op1["text"] = "A) Passar dos limites "
        self.op2["text"] = "B) Pular o Córrego "
        self.op3["text"] = "D) Experimentar Algo Novo"
        self.op4["text"] = "C) Estar Muito Feliz"
        self.op1.bind("<Button-1>", self.mudarwidget23)
        self.op2.bind("<Button-1>", self.mudarwidget24)
        self.op3.bind("<Button-1>", self.mudarwidget25)
        self.op4.bind("<Button-1>", self.mudarwidget26)
        acertos.append("a")
        print(acertos)

    def mudarwidget22(self, event):
        self.msg["text"] = 'Sexta Pergunta: O que significa "Esturdia"?'
        self.sair.bind("<Button-1>", self.mudarwidget27)
        self.op1["text"] = "A) Burrice "
        self.op2["text"] = "B) Dia Tranquilo "
        self.op3["text"] = "D) Hoje de Tarde"
        self.op4["text"] = "C) Esses Dias"
        self.op1.bind("<Button-1>", self.mudarwidget28)
        self.op2.bind("<Button-1>", self.mudarwidget29)
        self.op3.bind("<Button-1>", self.mudarwidget30)
        self.op4.bind("<Button-1>", self.mudarwidget31)

    def mudarwidget23(self, event):
        self.msg["text"] = 'Sexta Pergunta: O que significa "Esturdia"?'
        self.sair.bind("<Button-1>", self.mudarwidget27)
        self.op1["text"] = "A) Burrice "
        self.op2["text"] = "B) Dia Tranquilo "
        self.op3["text"] = "D) Hoje de Tarde"
        self.op4["text"] = "C) Esses Dias"
        self.op1.bind("<Button-1>", self.mudarwidget28)
        self.op2.bind("<Button-1>", self.mudarwidget29)
        self.op3.bind("<Button-1>", self.mudarwidget30)
        self.op4.bind("<Button-1>", self.mudarwidget31)
        acertos.append("a")
        print(acertos)


    def mudarwidget24(self, event):
        self.msg["text"] = 'Sexta Pergunta: O que significa "Esturdia"?'
        self.sair.bind("<Button-1>", self.mudarwidget27)
        self.op1["text"] = "A) Burrice "
        self.op2["text"] = "B) Dia Tranquilo "
        self.op3["text"] = "D) Hoje de Tarde"
        self.op4["text"] = "C) Esses Dias"
        self.op1.bind("<Button-1>", self.mudarwidget28)
        self.op2.bind("<Button-1>", self.mudarwidget29)
        self.op3.bind("<Button-1>", self.mudarwidget30)
        self.op4.bind("<Button-1>", self.mudarwidget31)

    def mudarwidget25(self, event):
        self.msg["text"] = 'Sexta Pergunta: O que significa "Esturdia"?'
        self.sair.bind("<Button-1>", self.mudarwidget27)
        self.op1["text"] = "A) Burrice "
        self.op2["text"] = "B) Dia Tranquilo "
        self.op3["text"] = "D) Hoje de Tarde"
        self.op4["text"] = "C) Esses Dias"
        self.op1.bind("<Button-1>", self.mudarwidget28)
        self.op2.bind("<Button-1>", self.mudarwidget29)
        self.op3.bind("<Button-1>", self.mudarwidget30)
        self.op4.bind("<Button-1>", self.mudarwidget31)
    def mudarwidget26(self, event):
        self.msg["text"] = 'Sexta Pergunta: O que significa "Esturdia"?'
        self.sair.bind("<Button-1>", self.mudarwidget27)
        self.op1["text"] = "A) Burrice "
        self.op2["text"] = "B) Dia Tranquilo "
        self.op3["text"] = "D) Hoje de Tarde"
        self.op4["text"] = "C) Esses Dias"
        self.op1.bind("<Button-1>", self.mudarwidget28)
        self.op2.bind("<Button-1>", self.mudarwidget29)
        self.op3.bind("<Button-1>", self.mudarwidget30)
        self.op4.bind("<Button-1>", self.mudarwidget31)

    def mudarwidget27(self, event):
        self.msg["text"] = 'Sétima Pergunta: O que significa "Fera"?'
        self.sair.bind("<Button-1>", self.mudarwidget32)
        self.op1["text"] = "A) Animal Selvagem "
        self.op2["text"] = "B) Pessoa Brava "
        self.op3["text"] = "D) Bom"
        self.op4["text"] = "C) Pessoa Veloz"
        self.op1.bind("<Button-1>", self.mudarwidget33)
        self.op2.bind("<Button-1>", self.mudarwidget34)
        self.op3.bind("<Button-1>", self.mudarwidget35)
        self.op4.bind("<Button-1>", self.mudarwidget36)

    def mudarwidget28(self, event):
        self.msg["text"] = 'Sétima Pergunta: O que significa "Fera"?'
        self.sair.bind("<Button-1>", self.mudarwidget32)
        self.op1["text"] = "A) Animal Selvagem "
        self.op2["text"] = "B) Pessoa Brava "
        self.op3["text"] = "D) Bom"
        self.op4["text"] = "C) Pessoa Veloz"
        self.op1.bind("<Button-1>", self.mudarwidget33)
        self.op2.bind("<Button-1>", self.mudarwidget34)
        self.op3.bind("<Button-1>", self.mudarwidget35)
        self.op4.bind("<Button-1>", self.mudarwidget36)


    def mudarwidget29(self, event):
        self.msg["text"] = 'Sétima Pergunta: O que significa "Fera"?'
        self.sair.bind("<Button-1>", self.mudarwidget32)
        self.op1["text"] = "A) Animal Selvagem "
        self.op2["text"] = "B) Pessoa Brava "
        self.op3["text"] = "D) Bom"
        self.op4["text"] = "C) Pessoa Veloz"
        self.op1.bind("<Button-1>", self.mudarwidget33)
        self.op2.bind("<Button-1>", self.mudarwidget34)
        self.op3.bind("<Button-1>", self.mudarwidget35)
        self.op4.bind("<Button-1>", self.mudarwidget36)


    def mudarwidget30(self, event):
        self.msg["text"] = 'Sétima Pergunta: O que significa "Fera"?'
        self.sair.bind("<Button-1>", self.mudarwidget32)
        self.op1["text"] = "A) Animal Selvagem "
        self.op2["text"] = "B) Pessoa Brava "
        self.op3["text"] = "D) Bom"
        self.op4["text"] = "C) Pessoa Veloz"
        self.op1.bind("<Button-1>", self.mudarwidget33)
        self.op2.bind("<Button-1>", self.mudarwidget34)
        self.op3.bind("<Button-1>", self.mudarwidget35)
        self.op4.bind("<Button-1>", self.mudarwidget36)


    def mudarwidget31(self, event):
        self.msg["text"] = 'Sétima Pergunta: O que significa "Fera"?'
        self.sair.bind("<Button-1>", self.mudarwidget32)
        self.op1["text"] = "A) Animal Selvagem "
        self.op2["text"] = "B) Pessoa Brava "
        self.op3["text"] = "D) Bom"
        self.op4["text"] = "C) Pessoa Veloz"
        self.op1.bind("<Button-1>", self.mudarwidget33)
        self.op2.bind("<Button-1>", self.mudarwidget34)
        self.op3.bind("<Button-1>", self.mudarwidget35)
        self.op4.bind("<Button-1>", self.mudarwidget36)
        acertos.append("a")
        print(acertos)

    def mudarwidget32(self, event):
        self.msg["text"] = 'Oitava Pergunta: O que significa "Rebuçar"?'
        self.sair.bind("<Button-1>", self.mudarwidget37)
        self.op1["text"] = "A) Cobrir "
        self.op2["text"] = "B) Ajudar "
        self.op3["text"] = "D) Assustar"
        self.op4["text"] = "C) Supreender"
        self.op1.bind("<Button-1>", self.mudarwidget38)
        self.op2.bind("<Button-1>", self.mudarwidget39)
        self.op3.bind("<Button-1>", self.mudarwidget40)
        self.op4.bind("<Button-1>", self.mudarwidget41)

    def mudarwidget33(self, event):
        self.msg["text"] = 'Oitava Pergunta: O que significa "Rebuçar"?'
        self.sair.bind("<Button-1>", self.mudarwidget37)
        self.op1["text"] = "A) Cobrir "
        self.op2["text"] = "B) Ajudar "
        self.op3["text"] = "D) Assustar"
        self.op4["text"] = "C) Supreender"
        self.op1.bind("<Button-1>", self.mudarwidget38)
        self.op2.bind("<Button-1>", self.mudarwidget39)
        self.op3.bind("<Button-1>", self.mudarwidget40)
        self.op4.bind("<Button-1>", self.mudarwidget41)

    def mudarwidget34(self, event):
        self.msg["text"] = 'Oitava Pergunta: O que significa "Rebuçar"?'
        self.sair.bind("<Button-1>", self.mudarwidget37)
        self.op1["text"] = "A) Cobrir "
        self.op2["text"] = "B) Ajudar "
        self.op3["text"] = "D) Assustar"
        self.op4["text"] = "C) Supreender"
        self.op1.bind("<Button-1>", self.mudarwidget38)
        self.op2.bind("<Button-1>", self.mudarwidget39)
        self.op3.bind("<Button-1>", self.mudarwidget40)
        self.op4.bind("<Button-1>", self.mudarwidget41)

    def mudarwidget35(self, event):
        self.msg["text"] = 'Oitava Pergunta: O que significa "Rebuçar"?'
        self.sair.bind("<Button-1>", self.mudarwidget37)
        self.op1["text"] = "A) Cobrir "
        self.op2["text"] = "B) Ajudar "
        self.op3["text"] = "D) Assustar"
        self.op4["text"] = "C) Supreender"
        self.op1.bind("<Button-1>", self.mudarwidget38)
        self.op2.bind("<Button-1>", self.mudarwidget39)
        self.op3.bind("<Button-1>", self.mudarwidget40)
        self.op4.bind("<Button-1>", self.mudarwidget41)
        acertos.append("a")
        print(acertos)

    def mudarwidget36(self, event):
        self.msg["text"] = 'Oitava Pergunta: O que significa "Rebuçar"?'
        self.sair.bind("<Button-1>", self.mudarwidget37)
        self.op1["text"] = "A) Cobrir "
        self.op2["text"] = "B) Ajudar "
        self.op3["text"] = "D) Assustar"
        self.op4["text"] = "C) Supreender"
        self.op1.bind("<Button-1>", self.mudarwidget38)
        self.op2.bind("<Button-1>", self.mudarwidget39)
        self.op3.bind("<Button-1>", self.mudarwidget40)
        self.op4.bind("<Button-1>", self.mudarwidget41)

    def mudarwidget37(self, event):
        self.msg["text"] = 'Nona Pergunta: O que significa "Di Rocha"?'
        self.sair.bind("<Button-1>", self.mudarwidget42)
        self.op1["text"] = "A) Advindo da Rocha "
        self.op2["text"] = "B) Confirmar Algo "
        self.op3["text"] = "D) Negar Algo"
        self.op4["text"] = "C) Propor um Assunto"
        self.op1.bind("<Button-1>", self.mudarwidget43)
        self.op2.bind("<Button-1>", self.mudarwidget44)
        self.op3.bind("<Button-1>", self.mudarwidget45)
        self.op4.bind("<Button-1>", self.mudarwidget46)

    def mudarwidget38(self, event):
        self.msg["text"] = 'Nona Pergunta: O que significa "Di Rocha"?'
        self.sair.bind("<Button-1>", self.mudarwidget42)
        self.op1["text"] = "A) Advindo da Rocha "
        self.op2["text"] = "B) Confirmar Algo "
        self.op3["text"] = "D) Negar Algo"
        self.op4["text"] = "C) Propor um Assunto"
        self.op1.bind("<Button-1>", self.mudarwidget43)
        self.op2.bind("<Button-1>", self.mudarwidget44)
        self.op3.bind("<Button-1>", self.mudarwidget45)
        self.op4.bind("<Button-1>", self.mudarwidget46)
        acertos.append("a")
        print(acertos)

    def mudarwidget39(self, event):
        self.msg["text"] = 'Nona Pergunta: O que significa "Di Rocha"?'
        self.sair.bind("<Button-1>", self.mudarwidget42)
        self.op1["text"] = "A) Advindo da Rocha "
        self.op2["text"] = "B) Confirmar Algo "
        self.op3["text"] = "D) Negar Algo"
        self.op4["text"] = "C) Propor um Assunto"
        self.op1.bind("<Button-1>", self.mudarwidget43)
        self.op2.bind("<Button-1>", self.mudarwidget44)
        self.op3.bind("<Button-1>", self.mudarwidget45)
        self.op4.bind("<Button-1>", self.mudarwidget46)

    def mudarwidget40(self, event):
        self.msg["text"] = 'Nona Pergunta: O que significa "Di Rocha"?'
        self.sair.bind("<Button-1>", self.mudarwidget42)
        self.op1["text"] = "A) Advindo da Rocha "
        self.op2["text"] = "B) Confirmar Algo "
        self.op3["text"] = "D) Negar Algo"
        self.op4["text"] = "C) Propor um Assunto"
        self.op1.bind("<Button-1>", self.mudarwidget43)
        self.op2.bind("<Button-1>", self.mudarwidget44)
        self.op3.bind("<Button-1>", self.mudarwidget45)
        self.op4.bind("<Button-1>", self.mudarwidget46)

    def mudarwidget41(self, event):
        self.msg["text"] = 'Nona Pergunta: O que significa "Di Rocha"?'
        self.sair.bind("<Button-1>", self.mudarwidget42)
        self.op1["text"] = "A) Advindo da Rocha "
        self.op2["text"] = "B) Confirmar Algo "
        self.op3["text"] = "D) Negar Algo"
        self.op4["text"] = "C) Propor um Assunto"
        self.op1.bind("<Button-1>", self.mudarwidget43)
        self.op2.bind("<Button-1>", self.mudarwidget44)
        self.op3.bind("<Button-1>", self.mudarwidget45)
        self.op4.bind("<Button-1>", self.mudarwidget46)

    def mudarwidget42(self, event):
        self.msg["text"] = 'Décima Pergunta: O que significa "Esbaforido(a)"?'
        self.sair.bind("<Button-1>", self.mudarwidget47)
        self.op1["text"] = "A) Transtornado "
        self.op2["text"] = "B) Cançado "
        self.op3["text"] = "D) Estressado"
        self.op4["text"] = "C) Entediado"
        self.op1.bind("<Button-1>", self.mudarwidget48)
        self.op2.bind("<Button-1>", self.mudarwidget49)
        self.op3.bind("<Button-1>", self.mudarwidget50)
        self.op4.bind("<Button-1>", self.mudarwidget51)

    def mudarwidget43(self, event):
        self.msg["text"] = 'Décima Pergunta: O que significa "Esbaforido(a)"?'
        self.sair.bind("<Button-1>", self.mudarwidget47)
        self.op1["text"] = "A) Transtornado "
        self.op2["text"] = "B) Cançado "
        self.op3["text"] = "D) Estressado"
        self.op4["text"] = "C) Entediado"
        self.op1.bind("<Button-1>", self.mudarwidget48)
        self.op2.bind("<Button-1>", self.mudarwidget49)
        self.op3.bind("<Button-1>", self.mudarwidget50)
        self.op4.bind("<Button-1>", self.mudarwidget51)


    def mudarwidget44(self, event):
        self.msg["text"] = 'Décima Pergunta: O que significa "Esbaforido(a)"?'
        self.sair.bind("<Button-1>", self.mudarwidget47)
        self.op1["text"] = "A) Transtornado "
        self.op2["text"] = "B) Cançado "
        self.op3["text"] = "D) Estressado"
        self.op4["text"] = "C) Entediado"
        self.op1.bind("<Button-1>", self.mudarwidget48)
        self.op2.bind("<Button-1>", self.mudarwidget49)
        self.op3.bind("<Button-1>", self.mudarwidget50)
        self.op4.bind("<Button-1>", self.mudarwidget51)
        acertos.append("a")
        print(acertos)

    def mudarwidget45(self, event):
        self.msg["text"] = 'Décima Pergunta: O que significa "Esbaforido(a)"?'
        self.sair.bind("<Button-1>", self.mudarwidget47)
        self.op1["text"] = "A) Transtornado "
        self.op2["text"] = "B) Cançado "
        self.op3["text"] = "D) Estressado"
        self.op4["text"] = "C) Entediado"
        self.op1.bind("<Button-1>", self.mudarwidget48)
        self.op2.bind("<Button-1>", self.mudarwidget49)
        self.op3.bind("<Button-1>", self.mudarwidget50)
        self.op4.bind("<Button-1>", self.mudarwidget51)

    def mudarwidget46(self, event):
        self.msg["text"] = 'Décima Pergunta: O que significa "Esbaforido(a)"?'
        self.sair.bind("<Button-1>", self.mudarwidget47)
        self.op1["text"] = "A) Transtornado "
        self.op2["text"] = "B) Cançado "
        self.op3["text"] = "D) Estressado"
        self.op4["text"] = "C) Entediado"
        self.op1.bind("<Button-1>", self.mudarwidget48)
        self.op2.bind("<Button-1>", self.mudarwidget49)
        self.op3.bind("<Button-1>", self.mudarwidget50)
        self.op4.bind("<Button-1>", self.mudarwidget51)

    def mudarwidget47(self, event):
        self.msg["text"] = 'Décima Primeira Pergunta: O que significa "Invinha"?'
        self.sair.bind("<Button-1>", self.mudarwidget52)
        self.op1["text"] = "A) Uva Pequena "
        self.op2["text"] = "B) Tipo de árvore "
        self.op3["text"] = "D) Enviado"
        self.op4["text"] = "C) Algo vindo"
        self.op1.bind("<Button-1>", self.mudarwidget53)
        self.op2.bind("<Button-1>", self.mudarwidget54)
        self.op3.bind("<Button-1>", self.mudarwidget55)
        self.op4.bind("<Button-1>", self.mudarwidget56)

    def mudarwidget48(self, event):
        self.msg["text"] = 'Décima Primeira Pergunta: O que significa "Invinha"?'
        self.sair.bind("<Button-1>", self.mudarwidget52)
        self.op1["text"] = "A) Uva Pequena "
        self.op2["text"] = "B) Tipo de árvore "
        self.op3["text"] = "D) Enviado"
        self.op4["text"] = "C) Algo vindo"
        self.op1.bind("<Button-1>", self.mudarwidget53)
        self.op2.bind("<Button-1>", self.mudarwidget54)
        self.op3.bind("<Button-1>", self.mudarwidget55)
        self.op4.bind("<Button-1>", self.mudarwidget56)

    def mudarwidget49(self, event):
        self.msg["text"] = 'Décima Primeira Pergunta: O que significa "Invinha"?'
        self.sair.bind("<Button-1>", self.mudarwidget52)
        self.op1["text"] = "A) Uva Pequena "
        self.op2["text"] = "B) Tipo de árvore "
        self.op3["text"] = "D) Enviado"
        self.op4["text"] = "C) Algo vindo"
        self.op1.bind("<Button-1>", self.mudarwidget53)
        self.op2.bind("<Button-1>", self.mudarwidget54)
        self.op3.bind("<Button-1>", self.mudarwidget55)
        self.op4.bind("<Button-1>", self.mudarwidget56)
        acertos.append("a")
        print(acertos)

    def mudarwidget50(self, event):
        self.msg["text"] = 'Décima Primeira Pergunta: O que significa "Invinha"?'
        self.sair.bind("<Button-1>", self.mudarwidget52)
        self.op1["text"] = "A) Uva Pequena "
        self.op2["text"] = "B) Tipo de árvore "
        self.op3["text"] = "D) Enviado"
        self.op4["text"] = "C) Algo vindo"
        self.op1.bind("<Button-1>", self.mudarwidget53)
        self.op2.bind("<Button-1>", self.mudarwidget54)
        self.op3.bind("<Button-1>", self.mudarwidget55)
        self.op4.bind("<Button-1>", self.mudarwidget56)
    def mudarwidget51(self, event):
        self.msg["text"] = 'Décima Primeira Pergunta: O que significa "Invinha"?'
        self.sair.bind("<Button-1>", self.mudarwidget52)
        self.op1["text"] = "A) Uva Pequena "
        self.op2["text"] = "B) Tipo de árvore "
        self.op3["text"] = "D) Enviado"
        self.op4["text"] = "C) Algo vindo"
        self.op1.bind("<Button-1>", self.mudarwidget53)
        self.op2.bind("<Button-1>", self.mudarwidget54)
        self.op3.bind("<Button-1>", self.mudarwidget55)
        self.op4.bind("<Button-1>", self.mudarwidget56)

    def mudarwidget52(self, event):
        self.msg["text"] = 'Décima Segunda Pergunta: O que significa "Pizêro"?'
        self.sair.bind("<Button-1>", self.mudarwidget57)
        self.op1["text"] = "A) Um Animal "
        self.op2["text"] = "B) Vacilo "
        self.op3["text"] = "D) Bagunça"
        self.op4["text"] = "C) Pier"
        self.op1.bind("<Button-1>", self.mudarwidget58)
        self.op2.bind("<Button-1>", self.mudarwidget59)
        self.op3.bind("<Button-1>", self.mudarwidget60)
        self.op4.bind("<Button-1>", self.mudarwidget61)

    def mudarwidget53(self, event):
        self.msg["text"] = 'Décima Segunda Pergunta: O que significa "Pizêro"?'
        self.sair.bind("<Button-1>", self.mudarwidget57)
        self.op1["text"] = "A) Um Animal "
        self.op2["text"] = "B) Vacilo "
        self.op3["text"] = "D) Bagunça"
        self.op4["text"] = "C) Pier"
        self.op1.bind("<Button-1>", self.mudarwidget58)
        self.op2.bind("<Button-1>", self.mudarwidget59)
        self.op3.bind("<Button-1>", self.mudarwidget60)
        self.op4.bind("<Button-1>", self.mudarwidget61)

    def mudarwidget54(self, event):
        self.msg["text"] = 'Décima Segunda Pergunta: O que significa "Pizêro"?'
        self.sair.bind("<Button-1>", self.mudarwidget57)
        self.op1["text"] = "A) Um Animal "
        self.op2["text"] = "B) Vacilo "
        self.op3["text"] = "D) Bagunça"
        self.op4["text"] = "C) Pier"
        self.op1.bind("<Button-1>", self.mudarwidget58)
        self.op2.bind("<Button-1>", self.mudarwidget59)
        self.op3.bind("<Button-1>", self.mudarwidget60)
        self.op4.bind("<Button-1>", self.mudarwidget61)

    def mudarwidget55(self, event):
        self.msg["text"] = 'Décima Segunda Pergunta: O que significa "Pizêro"?'
        self.sair.bind("<Button-1>", self.mudarwidget57)
        self.op1["text"] = "A) Um Animal "
        self.op2["text"] = "B) Vacilo "
        self.op3["text"] = "D) Bagunça"
        self.op4["text"] = "C) Pier"
        self.op1.bind("<Button-1>", self.mudarwidget58)
        self.op2.bind("<Button-1>", self.mudarwidget59)
        self.op3.bind("<Button-1>", self.mudarwidget60)
        self.op4.bind("<Button-1>", self.mudarwidget61)

    def mudarwidget56(self, event):
        self.msg["text"] = 'Décima Segunda Pergunta: O que significa "Pizêro"?'
        acertos.append("a")
        print(acertos)
        self.sair.bind("<Button-1>", self.mudarwidget57)
        self.op1["text"] = "A) Um Animal "
        self.op2["text"] = "B) Vacilo "
        self.op3["text"] = "D) Bagunça"
        self.op4["text"] = "C) Pier"
        self.op1.bind("<Button-1>", self.mudarwidget58)
        self.op2.bind("<Button-1>", self.mudarwidget59)
        self.op3.bind("<Button-1>", self.mudarwidget60)
        self.op4.bind("<Button-1>", self.mudarwidget61)

    def mudarwidget57(self, event):
        self.msg["text"] = 'Décima Terceira Pergunta: O que significa "Tunda"?'
        self.sair.bind("<Button-1>", self.mudarwidgetx1)
        self.op1["text"] = "A) Tipo de Fruta "
        self.op2["text"] = "B) Surra "
        self.op3["text"] = "D) Mata Selvagem"
        self.op4["text"] = "C) Planta do Cerrado"
        self.op1.bind("<Button-1>", self.mudarwidgetx2)
        self.op2.bind("<Button-1>", self.mudarwidgetx3)
        self.op3.bind("<Button-1>", self.mudarwidgetx4)
        self.op4.bind("<Button-1>", self.mudarwidgetx5)

    def mudarwidget58(self, event):
        self.msg["text"] = 'Décima Terceira Pergunta: O que significa "Tunda"?'
        self.sair.bind("<Button-1>", self.mudarwidgetx1)
        self.op1["text"] = "A) Tipo de Fruta "
        self.op2["text"] = "B) Surra "
        self.op3["text"] = "D) Mata Selvagem"
        self.op4["text"] = "C) Planta do Cerrado"
        self.op1.bind("<Button-1>", self.mudarwidgetx2)
        self.op2.bind("<Button-1>", self.mudarwidgetx3)
        self.op3.bind("<Button-1>", self.mudarwidgetx4)
        self.op4.bind("<Button-1>", self.mudarwidgetx5)

    def mudarwidget59(self, event):
        self.msg["text"] = 'Décima Terceira Pergunta: O que significa "Tunda"?'
        self.sair.bind("<Button-1>", self.mudarwidgetx1)
        self.op1["text"] = "A) Tipo de Fruta "
        self.op2["text"] = "B) Surra "
        self.op3["text"] = "D) Mata Selvagem"
        self.op4["text"] = "C) Planta do Cerrado"
        self.op1.bind("<Button-1>", self.mudarwidgetx2)
        self.op2.bind("<Button-1>", self.mudarwidgetx3)
        self.op3.bind("<Button-1>", self.mudarwidgetx4)
        self.op4.bind("<Button-1>", self.mudarwidgetx5)

    def mudarwidget60(self, event):
        self.msg["text"] = 'Décima Terceira Pergunta: O que significa "Tunda"?'
        acertos.append("a")
        print(acertos)
        self.sair.bind("<Button-1>", self.mudarwidgetx1)
        self.op1["text"] = "A) Tipo de Fruta "
        self.op2["text"] = "B) Surra "
        self.op3["text"] = "D) Mata Selvagem"
        self.op4["text"] = "C) Planta do Cerrado"
        self.op1.bind("<Button-1>", self.mudarwidgetx2)
        self.op2.bind("<Button-1>", self.mudarwidgetx3)
        self.op3.bind("<Button-1>", self.mudarwidgetx4)
        self.op4.bind("<Button-1>", self.mudarwidgetx5)

    def mudarwidget61(self, event):
        self.msg["text"] = 'Décima Terceira Pergunta: O que significa "Tunda"?'
        self.sair.bind("<Button-1>", self.mudarwidgetx1)
        self.op1["text"] = "A) Tipo de Fruta "
        self.op2["text"] = "B) Surra "
        self.op3["text"] = "D) Mata Selvagem"
        self.op4["text"] = "C) Planta do Cerrado"
        self.op1.bind("<Button-1>", self.mudarwidgetx2)
        self.op2.bind("<Button-1>", self.mudarwidgetx3)
        self.op3.bind("<Button-1>", self.mudarwidgetx4)
        self.op4.bind("<Button-1>", self.mudarwidgetx5)
    

    def mudarwidgetx1(self, event):
        self.msg.destroy()
        self.op1.destroy()
        self.op2.destroy()
        self.op3.destroy()
        self.op4.destroy()
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "9")
        self.sair.bind("<Button-1>", self.fimdofio)
        self.op3 = Label(self.widget4, text=len(acertos)-1, fg="white", bg="black")
        self.op4 = Label(self.widget4, text="Muito Bom!! Sua Quantidade de Acertos Foi:", fg="white", bg="black")
        self.op4["font"] = ("Calibri", "20")
        self.op3["font"] = ("Calibri", "20")
        self.op4.pack(side=LEFT)
        self.op3.pack(side=LEFT)
        self.op3["width"] = 2
        self.op4["width"] = 40
        self.op3["height"] = 10
        self.op4["height"] = 10

    def mudarwidgetx2(self, event):
        self.msg.destroy()
        self.op1.destroy()
        self.op2.destroy()
        self.op3.destroy()
        self.op4.destroy()
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "9")
        self.sair.bind("<Button-1>", self.fimdofio)
        self.op3 = Label(self.widget4, text=len(acertos)-1, fg="white", bg="black")
        self.op4 = Label(self.widget4, text="Muito Bom!! Sua Quantidade de Acertos Foi:", fg="white", bg="black")
        self.op4["font"] = ("Calibri", "20")
        self.op3["font"] = ("Calibri", "20")
        self.op4.pack(side=LEFT)
        self.op3.pack(side=LEFT)
        self.op3["width"] = 2
        self.op4["width"] = 40
        self.op3["height"] = 10
        self.op4["height"] = 10



         
    def mudarwidgetx3(self, event):
        acertos.append("a")
        print(acertos)
        self.op1.destroy()
        self.op2.destroy()
        self.op3.destroy()
        self.op4.destroy()
        self.msg.destroy()
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "9")
        self.sair.bind("<Button-1>", self.fimdofio)
        self.op3 = Label(self.widget4, text=len(acertos)-1, fg="white", bg="black")
        self.op4 = Label(self.widget4, text="Muito Bom!! Sua Quantidade de Acertos Foi:", fg="white", bg="black")
        self.op4["font"] = ("Calibri", "20")
        self.op3["font"] = ("Calibri", "20")
        self.op4.pack(side=LEFT)
        self.op3.pack(side=LEFT)
        self.op3["width"] = 2
        self.op4["width"] = 40
        self.op3["height"] = 10
        self.op4["height"] = 10




    def mudarwidgetx4(self, event):
        self.msg.destroy()
        self.op1.destroy()
        self.op2.destroy()
        self.op3.destroy()
        self.op4.destroy()
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "9")
        self.sair.bind("<Button-1>", self.fimdofio)
        self.op3 = Label(self.widget4, text=len(acertos)-1, fg="white", bg="black")
        self.op4 = Label(self.widget4, text="Muito Bom!! Sua Quantidade de Acertos Foi:", fg="white", bg="black")
        self.op4["font"] = ("Calibri", "20")
        self.op3["font"] = ("Calibri", "20")
        self.op4.pack(side=LEFT)
        self.op3.pack(side=LEFT)
        self.op3["width"] = 2
        self.op4["width"] = 40
        self.op3["height"] = 10
        self.op4["height"] = 10




    def mudarwidgetx5(self, event):
        self.msg.destroy()
        self.op1.destroy()
        self.op2.destroy()
        self.op3.destroy()
        self.op4.destroy()
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "9")
        self.sair.bind("<Button-1>", self.fimdofio)
        self.op3 = Label(self.widget4, text=len(acertos)-1, fg="white", bg="black")
        self.op4 = Label(self.widget4, text="Muito Bom!! Sua Quantidade de Acertos Foi:", fg="white", bg="black")
        self.op4["font"] = ("Calibri", "20")
        self.op3["font"] = ("Calibri", "20")
        self.op4.pack(side=LEFT)
        self.op3.pack(side=LEFT)
        self.op3["width"] = 2
        self.op4["width"] = 40
        self.op3["height"] = 10
        self.op4["height"] = 10

    def fimdofio(self, event):
        root.quit()
        import feira2






root = Tk()
root.geometry("1250x680")
root["bg"] = "black"
Application(root)
root.mainloop()



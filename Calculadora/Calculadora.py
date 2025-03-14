from tkinter import *
from tkinter import ttk

# cores
co1 = "#feffff"  # white/branca
co2 = "#38576b"  
co3 = "#ECEFF1"
co4 = '#FFAB40'  # Orange/laranja
fundo = "#3b3b3b"  # black/preta

# criando a janela principal
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.configure(bg=co1)

################# Frames ####################
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame_tela = Frame(janela, width=300, height=56, bg=co2, pady=0, padx=0, relief="flat")
frame_tela.grid(row=1, column=0, sticky=NW)

frame_quadros = Frame(janela, width=300, height=340, bg=fundo, pady=0, padx=0, relief="flat")
frame_quadros.grid(row=2, column=0, sticky=NW)

################# Funções ####################
todos_valores = ""  # Armazena as expressões que serão avaliadas
valor_texto = StringVar()

def entrar_valor(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    try:
        resultado = str(eval(todos_valores))
        valor_texto.set(resultado)
        todos_valores = resultado  # Mantém o resultado na tela para operações adicionais
    except Exception as e:
        valor_texto.set("Erro")
        todos_valores = ""
        print(f"Erro: {e}")  # Adicione esta linha para depuração

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

################# Label ####################
app_scream = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief="flat", anchor="e", bd=0, justify=RIGHT, font=('Ivy 18'), bg='#37474F', fg=co1)
app_scream.place(x=0, y=0)

################# Botões ####################
# Primeira linha
b_1 = Button(frame_quadros, command=limpar_tela, text="C", width=11, height=2, bg=co3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_quadros, command=lambda: entrar_valor('%'), text="%", width=5, height=2, bg=co3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_quadros, command=lambda: entrar_valor('/'), text="/", width=5, height=2, bg=co4, fg=co1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

# segunda linha
b_4 = Button(frame_quadros, command=lambda: entrar_valor('7'), text="7", width=5, height=2, bg=co3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frame_quadros, command=lambda: entrar_valor('8'), text="8", width=5, height=2, bg=co3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(frame_quadros, command=lambda: entrar_valor('9'), text="9", width=5, height=2, bg=co3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frame_quadros, command=lambda: entrar_valor('*'), text="*", width=5, height=2, bg=co4, fg=co1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

# terceira coluna
b_8 = Button(frame_quadros, command=lambda: entrar_valor('4'), text="4", width=5, height=2, bg=co3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9 = Button(frame_quadros, command=lambda: entrar_valor('5'), text="5", width=5, height=2, bg=co3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)

b_10 = Button(frame_quadros, command=lambda: entrar_valor('6'), text="6", width=5, height=2, bg=co3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)

b_11 = Button(frame_quadros, command=lambda: entrar_valor('-'), text="-", width=5, height=2, bg=co4, fg=co1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

# quarta coluna
b_12 = Button(frame_quadros, command=lambda: entrar_valor('1'), text="1", width=5, height=2, bg=co3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frame_quadros, command=lambda: entrar_valor('2'), text="2", width=5, height=2, bg=co3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)

b_14 = Button(frame_quadros, command=lambda: entrar_valor('3'), text="3", width=5, height=2, bg=co3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)

b_15 = Button(frame_quadros, command=lambda: entrar_valor('+'), text="+", width=5, height=2, bg=co4, fg=co1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

# quinta coluna
b_16 = Button(frame_quadros, command=lambda: entrar_valor('0'), text="0", width=11, height=2, bg=co3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)

b_17 = Button(frame_quadros, command=lambda: entrar_valor('.'), text=".", width=5, height=2, bg=co3, fg=fundo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)

b_18 = Button(frame_quadros, command=calcular, text="=", width=5, height=2, bg=co4, fg=co1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


janela.mainloop()

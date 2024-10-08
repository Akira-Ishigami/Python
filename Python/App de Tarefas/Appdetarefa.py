import tkinter as tk
from tkinter import ttk, font as tkFont, messagebox
from tkinter import PhotoImage

#  Funções 

def adicionar_tarefas():
    global frame_em_edicao

    tarefa = entrada_tarefa.get().strip()
    if tarefa and tarefa != "Escreva sua tarefa aqui":
        if frame_em_edicao is not None:
            atualizar_tarefa(tarefa)
            frame_em_edicao = None
        else:
            adicionar_item_tarefa(tarefa)
            entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, insira uma tarefa")

def adicionar_item_tarefa(tarefa):
    frame_tarefa = tk.Frame(canvas_interior, bg="white", bd=1, relief=tk.SOLID)

    label_tarefa = tk.Label(frame_tarefa, font=("Garamond", 16), bg="white", width=25, height=2, anchor="w", text=tarefa)
    label_tarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

    botao_editar = tk.Button(frame_tarefa, image=icon_editar, command=lambda f=frame_tarefa, L=label_tarefa: preparar_edicao(f, L), bg="white", relief=tk.FLAT)
    botao_editar.pack(side=tk.RIGHT, padx=5)

    botao_delete = tk.Button(frame_tarefa, image=icon_delete, command=lambda f=frame_tarefa: deletar_tarefa(f), bg="white", relief=tk.FLAT)
    botao_delete.pack(side=tk.RIGHT, padx=5)

    checkbutton = ttk.Checkbutton(frame_tarefa, command=lambda label=label_tarefa: alterar_taxado(label))
    checkbutton.pack(side=tk.RIGHT, padx=5)

    frame_tarefa.pack(fill=tk.X, padx=5, pady=5)

    sublinhado_estado[label_tarefa] = False

    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def preparar_edicao(frame_tarefa, label_tarefa):
    global frame_em_edicao
    frame_em_edicao = frame_tarefa
    entrada_tarefa.delete(0, tk.END)
    entrada_tarefa.insert(0, label_tarefa.cget("text"))

def atualizar_tarefa(nova_tarefa):
    global frame_em_edicao
    for widget in frame_em_edicao.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text=nova_tarefa)

def deletar_tarefa(frame_tarefa):
    frame_tarefa.destroy()
    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def alterar_taxado(label):
    fonte_atual = tkFont.Font(font=label.cget("font"))
    sublinhado_estado[label] = not sublinhado_estado[label]
    if sublinhado_estado[label]:
        nova_font = fonte_atual.copy()
        nova_font.config(overstrike=1)
    else:
        nova_font = fonte_atual.copy()
        nova_font.config(overstrike=0)
    label.config(font=nova_font)

# Atualização para a entrada de tarefas
def focar_entrada(event):
    if entrada_tarefa.get() == "Escreva sua tarefa aqui":
        entrada_tarefa.delete(0, tk.END)
        entrada_tarefa.config(fg="black")

def desfocar_entrada(event):
    if entrada_tarefa.get().strip() == "":
        entrada_tarefa.insert(0, "Escreva sua tarefa aqui")
        entrada_tarefa.config(fg="grey")

#  Configuração da Janela Principal 

# Criando a janela
janela = tk.Tk()
janela.title("ToDo!")
janela.configure(bg="#F0F0F0")
janela.geometry("500x600")

# Fonte e rótulo
fonte_cabecalho = tkFont.Font(family="Garamond", size=24, weight="bold")
rotulo_cabecalho = tk.Label(janela, text="Adicione suas tarefas", font=fonte_cabecalho, bg="#F0F0F0", fg="#333")
rotulo_cabecalho.pack(pady=20)

# Variável global para a tarefa em edição
frame_em_edicao = None
sublinhado_estado = {}  # Dicionário para armazenar o estado do texto tachado

#  Configuração dos Ícones 

icon_editar = PhotoImage(file="editar.png").subsample(20, 20)
icon_delete = PhotoImage(file="excluir.png").subsample(20, 20)

#  Layout e Widgets

# Frame para entrada de tarefa e botão
frame = tk.Frame(janela, bg="#F0F0F0")
frame.pack(pady=10)

entrada_tarefa = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg="white", fg="grey", width=30)
entrada_tarefa.pack(side=tk.LEFT, padx=10)
entrada_tarefa.insert(0, "Escreva sua tarefa aqui")

# Adiciona os eventos de foco
entrada_tarefa.bind("<FocusIn>", focar_entrada)
entrada_tarefa.bind("<FocusOut>", desfocar_entrada)

botao_adicionar = tk.Button(frame, command=adicionar_tarefas, text="Adicionar Tarefa", bg="#4CAF50", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=10)

# Cria um frame para a lista de tarefas com rolagem
frame_lista_tarefas = tk.Frame(janela, bg="white")
frame_lista_tarefas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_lista_tarefas, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame_lista_tarefas, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

# Cria um frame interior no canvas
canvas_interior = tk.Frame(canvas, bg="white")

# Adiciona o frame interior ao canvas
canvas.create_window((0, 0), window=canvas_interior, anchor="nw")

# Atualiza a região de rolagem quando o frame interior é configurado
canvas_interior.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

# Inicia o loop da interface gráfica
janela.mainloop()

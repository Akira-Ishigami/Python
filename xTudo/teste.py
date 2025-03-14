import tkinter as tk
from tkinter import messagebox

# Criar janela
janela = tk.Tk()
janela.title('Lista de Compra')
janela.geometry('300x355')

# Lista para armazenar os itens
lista_compra = []

# Campo de entrada
label_item = tk.Label(janela, text='Item:')
label_item.pack(pady=5)

entry_item = tk.Entry(janela, width=30)
entry_item.pack(pady=5)

# Listbox para exibir os itens
listbox_itens = tk.Listbox(janela, width=30)
listbox_itens.pack(pady=10)

# Função para adicionar item
def adicionar_item():
    item = entry_item.get().strip()
    if item:
        lista_compra.append(item)
        listbox_itens.insert(tk.END, item)
        entry_item.delete(0, tk.END)
    else:
        messagebox.showerror('Erro', 'Digite um item para adicionar')

# Função para remover item
def remover_item():
    try:
        indice = listbox_itens.curselection()[0]
        listbox_itens.delete(indice)
        lista_compra.pop(indice)
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item para remover')

# Função para mostrar a lista
def mostrar_lista():
    if lista_compra:
        messagebox.showinfo('Lista de Compra', '\n'.join(lista_compra))
    else:
        messagebox.showerror('Erro', 'Lista de compra vazia')

# Botões
botao_adicionar = tk.Button(janela, text="Adicionar Item", command=adicionar_item)
botao_adicionar.pack(pady=5)

botao_remover = tk.Button(janela, text="Remover Item Selecionado", command=remover_item)
botao_remover.pack(pady=5)

botao_mostrar = tk.Button(janela, text="Mostrar Lista", command=mostrar_lista)
botao_mostrar.pack(pady=5)

# Iniciar o loop da interface gráfica
janela.mainloop()
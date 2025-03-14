import tkinter as tk
from tkinter import messagebox

# Criamos uma variável global para armazenar a referência ao listbox e ao campo de entrada
lista_compra = []
listbox_itens = None
entry_item = None

def adicionar_item():
    global entry_item, listbox_itens
    item = entry_item.get().strip()
    if item:
        lista_compra.append(item)
        listbox_itens.insert(tk.END, item)
        entry_item.delete(0, tk.END)
    else:
        messagebox.showerror('Erro', 'Digite um item para adicionar')

def remover_item():
    global listbox_itens
    try:
        indice = listbox_itens.curselection()[0]
        lista_compra.pop(indice)
        listbox_itens.delete(indice)
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item para remover')

def mostrar_lista():
    if lista_compra:
        messagebox.showinfo('Lista de Compra', '\\n'.join(lista_compra))
    else:
        messagebox.showerror('Erro', 'Lista de compra vazia')

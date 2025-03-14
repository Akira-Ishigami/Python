import tkinter as tk
from tkinter import messagebox

# Função para adicionar item à lista
def adicionar_item(entry_item, listbox_itens, lista_compra):
    item = entry_item.get().strip()
    if item:
        lista_compra.append(item)
        listbox_itens.insert(tk.END, item)
        entry_item.delete(0, tk.END)
    else:
        messagebox.showerror('Erro', 'Digite um item para adicionar')

# Função para remover item da lista
def remover_item(listbox_itens, lista_compra):
    try:
        indice = listbox_itens.curselection()[0]
        lista_compra.pop(indice)
        listbox_itens.delete(indice)
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item para remover')

# Função para mostrar a lista
def mostrar_lista(lista_compra):
    if lista_compra:
        messagebox.showinfo('Lista de Compra', '\n'.join(lista_compra))
    else:
        messagebox.showerror('Erro', 'Lista de compra vazia')

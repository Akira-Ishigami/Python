import tkinter as tk
from tkinter import messagebox
import funcaoMercado as funcaoMercado

# Configuração da janela principal
janela = tk.Tk()
janela.title('Lista de Compra')
janela.geometry('300x350')

# Campo de entrada para adicionar itens
label_item = tk.Label(janela, text='Item: ')
label_item.pack(pady=5)

entry_item = tk.Entry(janela, width=30)
entry_item.pack(pady=5)

# Lista para exibir os itens
listbox_itens = tk.Listbox(janela, width=30)
listbox_itens.pack(pady=10)

# Lista para armazenar os itens
lista_compra = []

# Botões com chamadas corrigidas
botao_adicionar = tk.Button(janela, text="Adicionar Item",
                            command=lambda: funcaoMercado.adicionar_item(entry_item, listbox_itens, lista_compra))
botao_adicionar.pack(pady=5)

botao_remover = tk.Button(janela, text="Remover Item Selecionado",
                          command=lambda: funcaoMercado.remover_item(listbox_itens, lista_compra))
botao_remover.pack(pady=5)

botao_mostrar = tk.Button(janela, text="Mostrar Lista",
                          command=lambda: funcaoMercado.mostrar_lista(lista_compra))
botao_mostrar.pack(pady=5)

# Iniciar a interface gráfica
janela.mainloop()

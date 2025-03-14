import tkinter as tk
import funcaoMercado

janela = tk.Tk()
janela.title('Lista de Compra')
janela.geometry('300x350')

# Configuramos os componentes para que 'funcaoMercado' possa usá-los
funcaoMercado.listbox_itens = tk.Listbox(janela, width=30)
funcaoMercado.entry_item = tk.Entry(janela, width=30)

label_item = tk.Label(janela, text='Item:')
label_item.pack(pady=5)

funcaoMercado.entry_item.pack(pady=5)

botao_adicionar = tk.Button(janela, text="Adicionar Item", command=funcaoMercado.adicionar_item)
botao_adicionar.pack(pady=5)

funcaoMercado.listbox_itens.pack(pady=10)

botao_remover = tk.Button(janela, text="Remover Item Selecionado", command=funcaoMercado.remover_item)
botao_remover.pack(pady=5)

botao_mostrar = tk.Button(janela, text="Mostrar Lista", command=funcaoMercado.mostrar_lista)
botao_mostrar.pack(pady=5)

janela.mainloop()

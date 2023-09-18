import tkinter as tk

def acao_do_botao():
    print("Você clicou no botão!")

janela = tk.Tk()
janela.title("Minha Primeira Janela")

botao = tk.Button(janela, text="Clique em Mim", command=acao_do_botao)
botao.pack()

janela.mainloop()

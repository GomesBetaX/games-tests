import tkinter as tk

window = tk.Tk()
window.title("Exemplo Dropdown")

# Variável que armazena a opção selecionada
opcao = tk.StringVar()
opcao.set("Escolha uma opção")  # valor inicial

# Dropdown
dropdown = tk.OptionMenu(window, opcao, "Opção 1", "Opção 2", "Opção 3")
dropdown.config(width=20)  # largura opcional
dropdown.pack(pady=10)

# Botão para exibir valor selecionado
def mostrar_opcao():
    print("Selecionado:", opcao.get())

btn = tk.Button(window, text="Confirmar", command=mostrar_opcao)
btn.pack()

window.mainloop()

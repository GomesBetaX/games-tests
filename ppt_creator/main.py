import tkinter as tk
import creator as ct

# constantes
TITLE_FONT = ("Roboto", 18, "bold")
TEMA_FONT = ("Roboto", 12)
BG_COLOR = "#2E2E2E"
FG_COLOR = "#FFFFFF"
BTN_COLOR = "#007BFF"



# create windo
window = tk.Tk()
window.title("Criador de Slides")
window.config(padx=50, pady=20, bg=BG_COLOR)

# Label
title = tk.Label(text="Criador de Slide", font=TITLE_FONT, pady=10, highlightthickness=0, bg=BG_COLOR, fg=FG_COLOR)
title.grid(column=0, row=0)

# Tema and Entry
tema_label = tk.Label(text="Tema da aula", font=TEMA_FONT, pady=5, highlightthickness=0, bg=BG_COLOR, fg=FG_COLOR)
tema_label.grid(column=0, row=1, sticky="w")
tema_entry = tk.Text(width=30, height=1)
tema_entry.grid(column=0, row=2)

# Atividades
actv_label = tk.Label(text="Atividades da aula", font=TEMA_FONT, pady=10, highlightthickness=0, bg=BG_COLOR, fg=FG_COLOR)
actv_label.grid(column=0, row=3, sticky="w")
actv_entry = tk.Text(width=30, height=5)
actv_entry.grid(column=0, row=4)

# button
create_btn = tk.Button(text="Criar slide", font=("Arial", 12, "bold"), width=20, bg=BTN_COLOR, fg=FG_COLOR, highlightthickness=0, borderwidth=0)
create_btn.grid(column=0, row=5, pady=5)


# loop
window.mainloop()
import customtkinter as ctk
import creator as ct
import slide

# constantes
TITLE_FONT = ("Roboto", 18, "bold")
TEMA_FONT = ("Roboto", 12)
BG_COLOR = "#2E2E2E"
FG_COLOR = "#FFFFFF"
BTN_COLOR = "#007BFF"

gpt = ct.GPT()
ppt = slide.Preencher()

classe = {}
def create_class():
    global classe
    gpt.theme = tema_entry.get("1.0", "end").strip()
    gpt.extra = actv_entry.get("1.0", "end").strip()
    classe = gpt.fetch_lesson_plan()
    ppt.preencher_template(classe)

# Configurações iniciais do customtkinter
ctk.set_appearance_mode("dark")  # ou "light" para modo claro
ctk.set_default_color_theme("blue")  # você pode mudar para outro tema se quiser

# Create window
window = ctk.CTk()  # Criar a janela principal
window.title("Criador de Slides")
# window.geometry("600x500")
window.config(padx=50, pady=20, bg=BG_COLOR)

# Title Label
title = ctk.CTkLabel(window, text="Criador de Slide", font=TITLE_FONT, pady=10, bg_color=BG_COLOR)
title.grid(column=0, row=0)

# Tema and Entry
tema_label = ctk.CTkLabel(window, text="Tema da aula", font=TEMA_FONT, pady=5, bg_color=BG_COLOR)
tema_label.grid(column=0, row=1, sticky="w")
tema_entry = ctk.CTkTextbox(window, width=300, height=1)
tema_entry.grid(column=0, row=2)

# Atividades
actv_label = ctk.CTkLabel(window, text="Atividades da aula", font=TEMA_FONT, pady=10, bg_color=BG_COLOR)
actv_label.grid(column=0, row=3, sticky="w")
actv_entry = ctk.CTkTextbox(window, width=300, height=100)
actv_entry.grid(column=0, row=4)

# Dropdown
opcao = ctk.StringVar(value="Esquema de cores: ")  # valor inicial

dropdown = ctk.CTkOptionMenu(window, variable=opcao, values=["Enérgico", "Calma", "Neutro"])
dropdown.grid(column=0, row=5, pady=10)

# Button
create_btn = ctk.CTkButton(window, text="Criar slide", command=create_class, font=("Arial", 12, "bold"), width=20)
create_btn.grid(column=0, row=6, pady=5)

# Loop
window.mainloop()

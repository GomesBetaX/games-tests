import tkinter as tk
from tkinter import messagebox
import pyperclip
import random
import string

ALPHABET = string.ascii_letters
NUMEROS = string.digits
CARACTERES_ESPECIAIS = string.punctuation


# ---------------------------- PASSWORD GENERATOR -------------------------- #
def generate_password():
    # creates a new variable
    new_pass = ""

    # creates an 10-digit password with letters, numbers and special characters
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    # new_list = [NEW_ITEM_EXPRESSION for ITEM in LIST]
    password_list += [random.choice(ALPHABET) for i in range(nr_letters)]
    password_list += [random.choice(CARACTERES_ESPECIAIS) for i in range(nr_symbols)]
    password_list += [random.choice(NUMEROS) for i in range(nr_symbols)]
    random.shuffle(password_list)

    #turn list to a string
    new_pass = "".join(password_list)

    #copy the password
    pyperclip.copy(new_pass)

    # check to see if password field is empty or not
    if not entry_pass.get() == "":
        entry_pass.delete(0, tk.END)    
    entry_pass.insert(0, new_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # gets info
    info = {
        "website": entry_web.get(),
        "email": entry_email.get(),
        "password": entry_pass.get(),
    }

    # validação dos dados
    for key, value in info.items():
        if value == "":
            messagebox.showwarning(title="Campos vazios", message=f"O campo '{key}' está vazio.")
            return 0
    
    # asks for user confirmation
    answer = messagebox.askokcancel(title=info["website"], message=f"Email: {info['email']}\nSenha: {info['password']}\nDeseja salvar esses dados?")

    if answer == True:
        # adds data to a file
        with open("data.txt", "a") as file:
            file.write(f"{info["email"]} | {info["password"]} | {info['website']}\n")

            #deletes info
            entry_pass.delete(0, tk.END)
            entry_web.delete(0, tk.END)

            #shows confirmation that it was saved
            messagebox.showinfo(title="Confirmação", message="Dados salvos com sucesso!✅")

# ---------------------------- UI SETUP ------------------------------- #

#constants
FONTE = ("Arial", 12, "bold")

# creates window and its attribute
window = tk.Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)

# creates canvas and add images to idd
img = tk.PhotoImage(file="logo.png")
img_position = (100, 100) # metade do valor do canva
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# creates labels and entry for websites
label_web = tk.Label(text="Website:", font=FONTE)
label_web.grid(column=0, row=1, sticky="e")
entry_web = tk.Entry(width=35)
entry_web.focus()
entry_web.grid(column=1, row=1, columnspan=2, sticky="ew", ipady=2)


# creates labels and entry for email/username
label_user = tk.Label(text="Email/Username:", font=FONTE)
label_user.grid(column=0, row=2, sticky="e")
entry_email = tk.Entry(width=35)
entry_email.insert(0, "your_email@gmail.com")
entry_email.grid(column=1, row=2, columnspan=2, sticky="ew", ipady=2)

# creates labels and entry for password field and generate button
label_pass = tk.Label(text="Password:", font=FONTE)
label_pass.grid(column=0, row=3, sticky="e")
entry_pass = tk.Entry(width=21)
entry_pass.grid(column=1, row=3, sticky="ew", ipady=2)
btn_gen = tk.Button(text="Generate Password", command=generate_password)
btn_gen.grid(column=2, row=3)

# creates a button called "add"
btn_add = tk.Button(text="Add", command=save_password)
btn_add.grid(pady=5,column=1, row=4, columnspan=2, sticky="ew")

# ends the program
window.mainloop()
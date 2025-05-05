import tkinter as tk
import turtle as t

window = tk.Tk()
window.title("My first GUI program")
window.minsize(600, 400)


# Label
my_label = tk.Label(text="This is a label", font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0)

# way to change attribute of label
my_label["text"] = "New Text"
my_label.config(text="New Text")
tim = t.Turtle()
tim.write("Hello World")


# Button
def button_clicked(label, input_text):
    label.config(text=input_text.get())

button = tk.Button(text="Click me", command=lambda: button_clicked(my_label, input))
button.grid(column=0, row=2)

# Entry
input = tk.Entry()
input.grid(column=0, row=1)

window.mainloop()
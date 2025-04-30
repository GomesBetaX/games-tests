import tkinter as tk

window = tk.Tk()
window.title("My first GUI program")
window.minsize(300, 200)


# Label
my_label = tk.Label(text="This is a label", font=("Arial", 24, "italic"))
my_label.pack()

window.mainloop()
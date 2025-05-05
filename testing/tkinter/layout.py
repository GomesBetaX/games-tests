import tkinter as tk

window = tk.Tk()
window.minsize(500, 500)
window.config(padx=20, pady=20)

label = tk.Label(text="New Label", font=("Arial", 24, "italic"))
label.grid(column=0, row=0)

button1 = tk.Button(text="Click Me", width=10)
button1.grid(column=1, row=1)

button2 = tk.Button(text="Click Me", width=10)
button2.grid(column=2, row=0)

entry = tk.Entry(width=10)
entry.grid(column=3, row=2)

window.mainloop()
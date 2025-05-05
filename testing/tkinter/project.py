import tkinter as tk

window = tk.Tk()
window.title("Mile to KM Converter")
# window.minsize(400, 200)
window.config(padx=50, pady=40)

# functions
def calculate_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    result.config(text=f"{km:.2f}")

# entry box and label for miles
miles_input = tk.Entry(width=20, font=("Arial", 15), justify="center")
miles_input.grid(column=1, row=0)
miles_label = tk.Label(text="Miles", font=("Arial", 20))
miles_label.config(padx=10)
miles_label.grid(column=2, row=0)

# label for "is equal to", result, and km
equal = tk.Label(text="is equal to", font=("Arial", 20))
equal.grid(column=0, row=1)

result = tk.Label(text="0", font=("Arial", 20))
result.grid(column=1, row= 1)

km = tk.Label(text="Km", font=("Arial", 20))
km.grid(column=2, row=1)

# button 
calculate = tk.Button(text="Calculate", command=calculate_km,width=10, height=1, font=("Arial", 15, "bold"))
calculate.grid(column=1, row= 2)







window.mainloop()
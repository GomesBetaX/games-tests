import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ----------------------------- # 
def reset_timer():
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60 #1st, 3rd, 5th, 7th
    short_break_sec = SHORT_BREAK_MIN * 60 #2nd, 4th, 6th
    long_break_sec = LONG_BREAK_MIN * 60 #8th

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
        
    elif reps == 2 or reps == 4 or reps == 6:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    elif reps == 8:
        timer_label.config(text="Rest", fg=RED)
        count_down(long_break_sec)
        reset_timer()


# ---------------------------- COUNTDOWN MECHANISM --------------------- # 
def count_down(counter):
    count_min = int(counter / 60)
    count_sec = counter % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if counter > 0:
        window.after(1000, count_down, counter - 1)
    else:
        if reps < 8:
            start_timer()


# ---------------------------- UI SETUP -------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

# canvas
canvas = tk.Canvas(width=200, height=224, highlightthickness=0)
# to add a photo to the canvas
photo = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.config(bg=YELLOW)
canvas.grid(column=1, row=1)

# checkmarks
checkmark =  tk.Label(text="✅", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark.grid(column=1, row=3)

# buttons
start_button = tk.Button(text="Start", command=start_timer, width=7, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = tk.Button(text="Reset", command=print("Does something"), width=7, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
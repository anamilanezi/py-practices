import tkinter as tk
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Fixedsys"
WORK_MIN = 25 # 25
SHORT_BREAK_MIN = 5 # 5
LONG_BREAK_MIN = 20 # 20
reps = 0
checks = []
pomos = []
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    try:
        window.after_cancel(timer)
        timer_label.config(text="Timer", fg=GREEN)
        canvas.itemconfig(timer_text, text="00:00")
        checks_label.config(text="")
        global reps
        reps = 0
    except ValueError:
        pass


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60 # 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count = long_break_sec
        winsound.Beep(350, 1000)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        winsound.Beep(400, 500)
        count = short_break_sec
        timer_label.config(text="Break", fg=PINK)

    else:
        count = work_sec
        winsound.Beep(450, 500)
        timer_label.config(text="Work", fg=GREEN)

    count_down(count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = count // 60
    count_seg = count % 60
    if count_seg < 10:
        count_seg = f"0{count_seg}"

    # To change the content of a text from canvas, first it has to be assigned to a variable to use itemconfig with
    # the canvas object
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seg}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global checks
        global pomos
        if reps % 2 == 0:
            checks.append("✓")
            check_text = "".join(checks)
            checks_label.config(text=check_text)
        if len(checks) == 4 and reps % 8 == 0:
            checks = []
            pomos.append("🍅")
            pomo_text = "".join(pomos)
            checks_label.config(text="")
            cycle_label.config(text=pomo_text)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=25, bg=YELLOW)

timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

# Adding images
canvas = tk.Canvas(width=208, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(104, 120, image=tomato_img)

timer_text = canvas.create_text(104, 140, text="00:00", fill="white", font=('Consolas', 32, 'bold'))
canvas.grid(column=1, row=1)

start_bt = tk.Button(text="Start", width=5, font=(FONT_NAME, 9), bg='white', fg=RED, borderwidth=1,
                     highlightthickness=0, command=start_timer)

start_bt.grid(column=0, row=2)

reset_bt = tk.Button(text="Reset", width=5, font=(FONT_NAME, 9), bg='white', fg=RED, borderwidth=1,
                     highlightthickness=0, command=reset_timer)
reset_bt.grid(column=2, row=2)


checks_label = tk.Label(text="", fg=GREEN, bg=YELLOW, font=("Courier", 18))
checks_label.grid(column=1, row=3)

cycle_label = tk.Label(text="", fg=RED, bg=YELLOW, font=("Courier", 18))
cycle_label.grid(column=1, row=2)

window.mainloop()

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# Check mark ✔ ✓
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    REPS = 0
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    check_marks.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

    # If 8th rep:
    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Break', fg=RED)
    # If 2nd/4th/6th rep:
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='Break', fg=PINK)
    # If 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        title_label.config(text='Work', fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        global REPS
        start_timer()
        marks = ''
        if REPS % 2 == 0:
            global checks
            work_sessions = math.floor(REPS / 2)
            for _ in range(work_sessions):
                marks += '✓'
            check_marks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


title_label = Label(text="Timer", font=(FONT_NAME, 50), highlightthickness=0, bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)


check_marks = Label(highlightthickness=0, bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)

start_button = Button(text='Start', font=(FONT_NAME, 8), command=start_timer)
start_button.grid(row=2, column=0)


reset_button = Button(text='Reset', font=(FONT_NAME, 8), command=reset_timer)
reset_button.grid(row=2, column=2)



window.mainloop()

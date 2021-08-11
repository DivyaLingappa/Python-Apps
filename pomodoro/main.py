import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f2f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
REPS = 0
TIMER = None

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=100, bg=YELLOW)


def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    canvas.itemconfig(canvas_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    tick_label.config(text='')
    REPS = 0


def start_timer():
    global REPS
    REPS += 1
    if REPS % 2 != 0:
        timer_label.config(text='WORK', fg=GREEN)
        tick_label.config(text='')
        count_down(WORK_MIN * 60)
    else:
        if REPS % 8 == 0:
            timer_label.config(text='BREAK', fg=RED)
            tick_label.config(text='✅' * math.floor(REPS / 2))
            count_down(LONG_BREAK_MIN * 60)
        else:
            timer_label.config(text='BREAK', fg=PINK)
            tick_label.config(text='✅' * math.floor(REPS / 2))
            count_down(SHORT_BREAK_MIN * 60)


def count_down(count):
    global TIMER
    count_min = math.floor(count / 60)  # or int(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(canvas_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()


timer_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'normal'))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) 
tomato_img = PhotoImage(file="tomato.png")
canvas_image = canvas.create_image(100, 112, image=tomato_img)  
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text='Start', activebackground='blue', highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', activebackground='blue', highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

tick_label = Label(text="", bg=YELLOW)
tick_label.grid(row=3, column=1)

window.mainloop()

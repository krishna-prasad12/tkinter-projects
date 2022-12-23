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
rep=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text1, text="00:00")
    lable1.config(text="Timer")
    check_marks.config(text="")
    global rep
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global rep
    rep+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN

    if rep%8==0:
        count_start(long_break_sec)
        lable1.config(text='Break',fg=RED)
    elif rep%2==0:
        count_start(short_break_sec)
        lable1.config(text='Break', fg=PINK)
    else:
        count_start(work_sec)
        lable1.config(text='Work', fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_start(count):
    min=math.floor(count/60)
    sec=count%60
    if count <10:
        sec=f"0{sec}"
    canvas.itemconfig(text1,text=f'{min}:{sec}')
    if count>0:
        global timer
        timer=window.after(1000,count_start,count-1)
    else:
        start_time()
        marks = ""
        work_sessions = math.floor(rep / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('pomodoro')
window.config(pady=100,padx=100,bg=YELLOW)
lable1=Label(text='TIMER',fg=GREEN,font=(FONT_NAME,35,),bg=YELLOW)
lable1.grid(column=1,row=0)
canvas=Canvas(width=270,height=252,bg=YELLOW,highlightcolor=YELLOW,highlightthickness=0)
img=PhotoImage(file='tomato.png')
canvas.create_image(120,122,image=img)
text1=canvas.create_text(120,130,text='00:00',fill='White',font=(FONT_NAME,30,'bold'))
canvas.grid(column=1,row=1)

start_but=Button(text='Start',command=start_time,highlightcolor=YELLOW,highlightthickness=0)
start_but.grid(column=0,row=2,)

reset_but=Button(text='Reset',highlightcolor=YELLOW,highlightthickness=0,command=reset_timer)
reset_but.grid(column=2,row=2)
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
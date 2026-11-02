from tkinter import *

window = Tk()
window.title("The Most Dangerous Writing App")
window.geometry("1000x750")
window.config(bg="#F5F0E8", padx=50, pady=35)
window.resizable(True, True)

title_label = Label(
    text="The Most Dangerous Writing App",
    font=("Georgia", 26, "bold"),
    bg="#F5F0E8",
    fg="#292725",
)
title_label.pack(pady=(10, 5))

subtitle_label = Label(
    text="Keep writing. Don't stop. Don't lose your words.",
    font=("Arial", 11),
    bg="#F5F0E8",
    fg="#82786D",
)
subtitle_label.pack(pady=(0, 25))

timer_label = Label(
    text="00:05", font=("Arial", 20, "bold"), bg="#F5F0E8", fg="#A58B70"
)

timer_label.pack(pady=(0, 15))

warning_label = Label(
    text="⚠ Stop typing for 5 seconds and your work will disappear.",
    font=("Arial", 10),
    bg="#F5F0E8",
    fg="#A58B70",
)

warning_label.pack(pady=15)

text_box = Text(
    width=80,
    height=25,
    font=("Georgia", 14),
    wrap="word",
    bg="#FFFFFF",
    fg="#292725",
    insertbackground="#292725",
    relief="flat",
    padx=25,
    pady=25,
    borderwidth=0,
)

text_box.pack(fill="both", expand=True, pady=10)

timer = None
time_left = 5


def delete_text():
    global timer, time_left

    text_box.delete("1.0", END)
    timer = None
    time_left = 5

    timer_label.config(text="00:05", fg="#A58B70")


def countdown():
    global time_left, timer

    time_left -= 1

    timer_label.config(text=f"00:{time_left:02d}")

    if time_left <= 2:
        timer_label.config(fg="#C0392B")
    else:
        timer_label.config(fg="#A58B70")

    if time_left > 0:
        timer = window.after(1000, countdown)
    else:
        delete_text()


def reset_timer(event):
    global timer, time_left

    if timer:
        window.after_cancel(timer)

    time_left = 5
    timer_label.config(text="00:05")
    timer_label.config(fg="#A58B70")

    timer = window.after(1000, countdown)


text_box.bind("<Key>", reset_timer)

window.mainloop()

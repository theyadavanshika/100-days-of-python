import tkinter as tk
import time

start_time = None

window = tk.Tk()
window.title("Typing Speed Test")
window.geometry("600x500")


def start_timer(event):
    global start_time

    if start_time is None:
        start_time = time.time()


def calculate_speed():
    if start_time is None:
        print("Please start typing first!")
        return

    end_time = time.time()
    elapsed_time = (end_time - start_time) / 60

    typed_text = typing_box.get("1.0", "end-1c")

    correct_chars = 0
    for i in range(min(len(typed_text), len(sample_text))):
        if typed_text[i] == sample_text[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(sample_text)) * 100

    words = len(typed_text.split())

    if elapsed_time > 0:
        wpm = words / elapsed_time
        result_label.config(text=f"Speed: {wpm:.2f} WPM | Accuracy: {accuracy:.2f}%")


def restart_test():
    global start_time

    start_time = None
    typing_box.delete("1.0", tk.END)
    result_label.config(text="")
    typing_box.focus_set()


sample_text = (
    "Python is a powerful programming language. "
    "Practice makes you better at coding every day."
)

text_label = tk.Label(
    window, text=sample_text, wraplength=500, font=("Arial", 14), justify="left"
)
text_label.pack(pady=30, padx=20)


typing_box = tk.Text(
    window,
    height=6,
    width=55,
    font=("Arial", 13),
    wrap="word",
    relief="solid",
    borderwidth=2,
)
typing_box.pack(pady=20, padx=20)

finish_button = tk.Button(window, text="Finish Test", command=calculate_speed)
finish_button.pack(pady=10)


restart_button = tk.Button(window, text="Restart Test", command=restart_test)
restart_button.pack(pady=5)


typing_box.bind("<KeyPress>", start_timer)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

window.mainloop()

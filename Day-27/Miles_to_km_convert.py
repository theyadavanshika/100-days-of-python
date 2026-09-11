from tkinter import *

def miles_to_km_convert():
    miles = float(miles_entry.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=300, height=200)
window.config(padx=40, pady=40)

miles_entry = Entry(width=8)
miles_entry.grid(column=1,row=0)

miles_label =Label(text = "Miles")
miles_label.grid(column=2,row=0)

equals_to_label = Label(text="is equals to")
equals_to_label.grid(column=0,row=1)

km_result_label = Label(text = "0")
km_result_label.grid(column=1,row=1)

km_label = Label(text="km")
km_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate", command=miles_to_km_convert)
calculate_button.grid(column=1,row=2)

window.mainloop() 
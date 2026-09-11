from tkinter import *

window = Tk()
window.title("Learn GUI")
window.minsize(width = 500, height = 300) 

#Label
my_label = Label(text = "this is a label", font = ("Arial", 30, "italic")) #Label is a class
my_label.pack() #To lay out the component : To pack your label onto the screen
# my_label.pack(side="left") : all of this work

# my_label.config(text = "new text")
# my_label["text"] = "Button got clicked"

#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label["text"] = new_text
    
button = Button(text = "Click Me", command = button_clicked)
button.pack()

#Entry
input = Entry(width = 10)
input.pack()

#Keeps the window open and listens what user will interact with it
window.mainloop()  





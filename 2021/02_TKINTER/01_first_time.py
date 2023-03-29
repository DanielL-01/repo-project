from tkinter import Tk, Label, Entry, Button

window =Tk()

label = Label(window, text="I love you 3000")
label.grid()

entry = Entry(window)
entry.grid()

button = Button(window, text="Submit!!")
button.grid()

window.mainloop()
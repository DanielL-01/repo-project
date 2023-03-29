from tkinter import Tk, Frame

window = Tk()
window.title("Belajar grid configure")
window.geometry("300x400")

frame0 = Frame(window, bg="yellow")
frame0.grid(row=0, column=0, columnspan=2, sticky="nswe")


frame1 = Frame(window, bg="red")
frame1.grid(row=1, column=0,  sticky="nswe")

frame2 = Frame(window, bg="orange")
frame2.grid(row=1, column=1, rowspan=2, sticky="nswe")

frame3 = Frame(window, bg="purple")
frame3.grid(row=2, column=0, sticky="nswe")

window.grid_rowconfigure(0, weight=2)
window.grid_rowconfigure(1, weight=3)
window.grid_rowconfigure(2, weight=1)

window.grid_columnconfigure(0, weight=2)
window.grid_columnconfigure(1, weight=1)

window.mainloop()
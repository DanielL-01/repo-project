from tkinter import Tk, Frame

window = Tk()
window.title("Belajar grid configure")
window.geometry("300x400")

frame0 = Frame(window, bg="blue")
frame0.grid(row=0, column=0, sticky="nswe")

frame5 = Frame(window, bg="black")
frame5.grid(row=0, column=1, sticky="nswe")

frame1 = Frame(window, bg="purple")
frame1.grid(row=1, column=0, columnspan=2, sticky="nswe")

frame2 = Frame(window, bg="yellow")
frame2.grid(row=2, column=0, columnspan=2, sticky="nswe")

frame3 = Frame(window, bg="red")
frame3.grid(row=3, column=0, columnspan=2, sticky="nswe")

frame4 = Frame(window, bg="green")
frame4.grid(row=4, column=0, columnspan=2, sticky="nswe")

window.grid_rowconfigure(0, weight=2)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.mainloop()
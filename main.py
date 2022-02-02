import tkinter

window = tkinter.Tk()

c = tkinter.Canvas(window, width=600, height=600, bg='white')
c.pack()

c.create_rectangle(100, 100, 200, 200, fill="red")

window.mainloop()
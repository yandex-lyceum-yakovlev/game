import tkinter

window = tkinter.Tk()

width = height = 600  # ширина и высота игрового поля в пикселях
c = tkinter.Canvas(window, width=width, height=height, bg='white')
c.pack()

n = m = 10  # количество строк и столбцов
cell_width = width // n  # ширина ячейки
cell_height = height // m  # высота ячейки
for i in range(n):
    for j in range(m):
        c.create_rectangle(i * cell_width, j * cell_height,
                           (i + 1) * cell_width, (j + 1) * cell_height, fill="red")

window.mainloop()

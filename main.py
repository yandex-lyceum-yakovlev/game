import tkinter
from random import randint


def draw(board):  # отображает внутреннее представление игрового поля на канвас
    for i in range(n):
        for j in range(m):
            c.create_rectangle(i * cell_width, j * cell_height,
                               (i + 1) * cell_width, (j + 1) * cell_height, fill=board[i][j])


def update():
    board[randint(0, n - 1)][randint(0, m - 1)] = "green"
    draw(board)
    window.after(1000, update)


window = tkinter.Tk()

width = height = 600  # ширина и высота игрового поля в пикселях
c = tkinter.Canvas(window, width=width, height=height, bg='white')
c.pack()

n = m = 10  # количество строк и столбцов
cell_width = width // n  # ширина ячейки
cell_height = height // m  # высота ячейки

board = [["red"] * n for i in range(m)]
board[2][5] = "green"
board[3][0] = "blue"
draw(board)
window.after(1000, update)

window.mainloop()

import tkinter
from random import randint


class Snake:
    dx = 0
    dy = 1
    segments = [[2, 3], [3, 3], [4, 3]]

    def move(self):
        for p in self.segments:
            p[0] += self.dx
            p[1] += self.dy

    def key_pressed(self, event):
        if event.keysym == "Right":
            self.dx, self.dy = 1, 0
        if event.keysym == "Left":
            self.dx, self.dy = -1, 0
        if event.keysym == "Down":
            self.dx, self.dy = 0, 1
        if event.keysym == "Up":
            self.dx, self.dy = 0, -1


def draw(board, snake):  # отображает внутреннее представление игрового поля на канвас
    for i in range(n):
        for j in range(m):
            c.create_rectangle(i * cell_width, j * cell_height,
                               (i + 1) * cell_width, (j + 1) * cell_height, fill=board[i][j])
    for i, j in snake.segments[:-1]:
        c.create_rectangle(i * cell_width, j * cell_height,
                           (i + 1) * cell_width, (j + 1) * cell_height, fill="green")
    i, j = snake.segments[-1]
    c.create_rectangle(i * cell_width, j * cell_height,
                       (i + 1) * cell_width, (j + 1) * cell_height, fill="red")


def update():
    # board[randint(0, n - 1)][randint(0, m - 1)] = "green"
    snake.move()
    draw(board, snake)
    window.after(1000, update)


window = tkinter.Tk()

width = height = 600  # ширина и высота игрового поля в пикселях
c = tkinter.Canvas(window, width=width, height=height, bg='white')
c.pack()

n = m = 10  # количество строк и столбцов
cell_width = width // n  # ширина ячейки
cell_height = height // m  # высота ячейки

board = [["silver"] * n for i in range(m)]
board[3][0] = "blue"
snake = Snake()
draw(board, snake)
window.bind("<KeyPress>", snake.key_pressed)
window.after(1000, update)

window.mainloop()

import tkinter
from random import randint


class Snake:
    dx = 1
    dy = 0
    segments = [[2, 3], [3, 3], [4, 3]]

    def move(self):
        global end_game
        if board[self.segments[-1][0]][self.segments[-1][1]] != "yellow":
            del self.segments[0]
        else:
            board[self.segments[-1][0]][self.segments[-1][1]] = "silver"
            board[randint(0, n - 1)][randint(0, m - 1)] = "yellow"
        self.segments.append([self.segments[-1][0] + self.dx, self.segments[-1][1] + self.dy])
        if not(0 <= self.segments[-1][0] < n) or not(0 <= self.segments[-1][1] < m):
            end_game = True
        if self.segments[-1] in self.segments[:-1]:
            end_game = True


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
    if end_game:
        c.create_rectangle(0, 0, 600, 600, fill="blue")
    else:
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
board[randint(0, n - 1)][randint(0, m - 1)] = "yellow"
snake = Snake()
draw(board, snake)
window.bind("<KeyPress>", snake.key_pressed)
end_game = False
window.after(1000, update)

window.mainloop()

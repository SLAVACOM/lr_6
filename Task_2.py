import tkinter as tk
import random

WIDTH = 16*50
HEIGHT = 9*50

RECTANGLE_WIDTH = 150
RECTANGLE_HEIGHT = 90

x = random.randint(0, WIDTH - 50)
y = random.randint(0, HEIGHT - 30)

dx = 5
dy = 5

window = tk.Tk()
window.title("Аналог DVD Logo")
window.resizable(False, False)

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF"]

fill = 0
def change_color():
    global fill
    fill = (fill+1)%len(colors)

def draw_logo(x, y):#808080
    canvas.create_rectangle(x, y, x + RECTANGLE_WIDTH, y + RECTANGLE_HEIGHT, fill =colors[fill])
def update():
    global x, y, dx, dy
    canvas.delete("all")
    x += dx
    y += dy

    draw_logo(x, y)
    if x >= WIDTH - RECTANGLE_WIDTH or x <= 0:
        dx *= -1
        change_color()
    if y >= HEIGHT - RECTANGLE_HEIGHT or y <= 0:
        dy *= -1
        change_color()
    canvas.after(50, update)

draw_logo(x, y)
update()
window.mainloop()
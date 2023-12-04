from tkinter import *
import time

WIDTH = 350
HEIGHT = 25 * 50
size = 20
green_yes = 1
time = [5, 1, 5]


def change_color():
    canvas.itemconfigure(red, fill='red')
    canvas.itemconfigure(yellow, fill='black')
    canvas.itemconfigure(green, fill='black')
    canvas.after(time[0] * 1000, change_color_yellow)


def change_color_yellow():
    global green_yes
    canvas.itemconfigure(yellow, fill='yellow')
    canvas.itemconfigure(green, fill='black')
    if green_yes == 1:
        canvas.after(time[1] * 1000, change_color_green)
    else:
        canvas.after(time[1] * 1000, change_color)
    green_yes *= -1


def change_color_green():
    canvas.itemconfigure(red, fill='black')
    canvas.itemconfigure(yellow, fill='black')
    canvas.itemconfigure(green, fill='green')
    canvas.after(time[2] * 1000, change_color_yellow)


root = Tk()
root.title("Светофор")

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="#808080")
canvas.pack()

red = canvas.create_oval(size, size, size + 310, 330, fill="red")
yellow = canvas.create_oval(size, size * 2 + 310, size + 310, 350 + 310, fill="yellow")
green = canvas.create_oval(size, size * 3 + 2 * 310, size + 310, 350 * 2 + 310, fill="green")

change_color()

root.mainloop()

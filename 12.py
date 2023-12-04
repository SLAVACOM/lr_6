from tkinter import *

def change_color():
    canvas.itemconfigure(red_light, fill='red')
    canvas.itemconfigure(yellow_light, fill='black')
    canvas.itemconfigure(green_light, fill='black')
    canvas.after(3000, change_color_yellow)

def change_color_yellow():
    canvas.itemconfigure(red_light, fill='black')
    canvas.itemconfigure(yellow_light, fill='yellow')
    canvas.itemconfigure(green_light, fill='black')
    canvas.after(1000, change_color_green)

def change_color_green():
    canvas.itemconfigure(red_light, fill='black')
    canvas.itemconfigure(yellow_light, fill='black')
    canvas.itemconfigure(green_light, fill='green')
    canvas.after(2000, change_color)

root = Tk()
canvas = Canvas(root, width=200, height=400)
canvas.pack()

red_light = canvas.create_oval(50, 50, 150, 150, fill='black')
yellow_light = canvas.create_oval(50, 175, 150, 275, fill='black')
green_light = canvas.create_oval(50, 300, 150, 400, fill='black')

change_color()

root.mainloop()
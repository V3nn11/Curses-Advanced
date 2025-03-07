
"""def sum_digits(x,y):
     x = 1
     y = 2
     z = x + y
     print(z)
command = sum_digits(1,2)
"""

"""""import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Click to create a line")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

def create_line(event):
    canvas.create_line(0, 0, event.x, event.y, fill="blue")

canvas.bind("<Button-1>", create_line)

root.mainloop()
"""
"""import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
root.title("Pirate Flag")

canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()

def draw_pirate_flag(event):
    # Draw lines from corner to corner
    canvas.create_line(0, 0, 600, 400, fill="white", width=5)
    canvas.create_line(0, 400, 600, 0, fill="white", width=5)

canvas.bind("<Button-1>", draw_pirate_flag)

root.mainloop()
"""

"""import tkinter as tk
import random

root = tk.Tk()
root.geometry("600x600")
root.title("sky")

canvas = tk.Canvas(root, width=600, height=600, bg="black")
canvas.pack()

def draw_sky(event):
    for _ in range(1000):
        x = random.randint(0, 600)
        y = random.randint(0, 600)
        canvas.create_oval(x, y, x+1, y+1, fill="white", outline="white")

canvas.bind("<Button-3>", draw_sky)

root.mainloop()"""

"""import tkinter as tk
import random

root = tk.Tk()
root.geometry("600x600")
root.title("expansiunea bulelor..*sunete de gojo*")
canvas = tk.Canvas(root, width=600, height=600, bg="black")
canvas.pack()

colors = ('#00ffff', 'blue', '#ff00ff', 'green', 'maroon', 'orange',
          'pink', 'purple', 'red', 'yellow', 'violet', '#4b0082', 'chartreuse', '#00ff00', '#f55c4b')

def draw_bubbles(event):
    for _ in range(1000):
        diameter = random.randint(30, 120)
        x = random.randint(0, 600 - diameter)
        y = random.randint(0, 600 - diameter)
        color = random.choice(colors)
        canvas.create_oval(x, y, x + diameter, y + diameter, fill=color, outline=color)

canvas.bind("<Button-2>", draw_bubbles)

root.mainloop()
"""

import tkinter as tk

root = tk.Tk()
root.geometry("600x600")
root.title("Cilindru")
root.configure(bg="light blue")

canvas = tk.Canvas(root, width=600, height=600, bg="light blue")
canvas.pack()

def draw_cylinder(event):
    # Top ellipse
    canvas.create_oval(200, 100, 400, 200, fill="", outline="black")
    # Bottom ellipse
    canvas.create_oval(200, 300, 400, 400, fill="", outline="black")
    # Left line
    canvas.create_line(200, 150, 200, 350, fill="black")
    # Right line
    canvas.create_line(400, 150, 400, 350, fill="black")

canvas.bind("<Double-Button-1>", draw_cylinder)

root.mainloop()
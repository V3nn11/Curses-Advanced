import tkinter as tk
import random
w = 600
h = 400

master = tk.Tk()
master.title("Ceva fulgi care cad")
canvas = tk.Canvas(master, width = w, height= h, bg ="black")

list_fg = []
for i in range(100):
     sz = random.randint(5, 15)
     x = random.randint(0, w)
     z = random.randint(0, h)
     fg = canvas.create_oval(x, z, x+sz, z+sz, fill = "white")
     list_fg.append(fg)

def move_fg():
     for i in list_fg:
          canvas.move(i, 0, 3)
          x, y, x1, y1 = canvas.coords(i)
          if y1 > h:
               canvas.move(i, 0, -h)
     canvas.after(25, move_fg)
          
canvas.pack()
move_fg()
master.mainloop()

     

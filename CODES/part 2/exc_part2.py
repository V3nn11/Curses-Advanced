#Trebuie sa cream o caramida care este centrata la mijloc si in partea de sus a ecranului nostru.

import tkinter as tk

root = tk.Tk()
root.title("Caramida")

canvas = tk.Canvas(root, width= 600, height = 600, bg = "black")
canvas.pack()

#acum, trebuie sa cream caramida

brick = (300, 100)
brick_color = "red"

#acuma, vom crea o functie care va desena caramida noastra pe ecran sus de tot la mijloc

def draw_brick():
    x, y = brick
    canvas.create_rectangle(x- 30, y, x+30, y+20, fill=brick_color)
    canvas.create_oval(0,0,200,200,fill="red")

draw_brick()

#acuma, vom crea o functie care va misca caramida noastra in jos cu viteza de 6 pixeli pe frame

def move_brick():
    x1, y1, x2, y2 = canvas.coords(1)
    if y2 < 600:
        canvas.move(1, 0, 6)
        root.after(6, move_brick)

move_brick()

#trebuie sa facem in asa fel incat caramida se opreste daca width = 600
#pentru asta, trebuie sa facem o functie care verifica daca caramida a ajuns la marginea de jos a ecranului
#si daca a ajuns, atunci sa o opreasca
#(canvas.coords()) returneaza coordonatele unui obiect de pe canvas
#(canvas.coords(1)) returneaza coordonatele caramizii noastre

def check_collision():
    x1, y1, x2, y2 = canvas.coords(2)
    if y2 < 600:
        root.after(6, check_collision)

check_collision()

root.mainloop()
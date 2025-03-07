import tkinter as tk

root = tk.Tk()
root.title("Caramida")

canvas = tk.Canvas(root, width= 600, height = 600, bg = "black")
canvas.pack()

#acum, trebuie sa cream caramida

brick = (300, 100)
brick_color = "red"

def key(event):
   key_name = event.keysym
   root.title(key_name)
root.bind("<Key>", key)

#acuma, vom crea o functie care va desena caramida noastra pe ecran sus de tot la mijloc

def draw_brick():
    x, y = brick
    canvas.create_rectangle(x- 30, y, x+30, y+20, fill=brick_color)

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
    x1, y1, x2, y2 = canvas.coords(1)
    if y2 < 600:
        root.after(6, check_collision)

check_collision()

root.mainloop()```
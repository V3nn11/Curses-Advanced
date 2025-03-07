#Trebuie sa cream o caramida care este centrata la mijloc si in partea de sus a ecranului nostru.

import tkinter as tk

root = tk.Tk()
root.title("Caramida")

canvas = tk.Canvas(root, width=600, height=600, bg="black")
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
    canvas.create_rectangle(x - 30, y, x + 30, y + 20, fill=brick_color, tags="brick")

draw_brick()

#acuma, vom crea o functie care va misca caramida noastra in jos cu viteza de 6 pixeli pe frame

def move_brick():
    x1, y1, x2, y2 = canvas.coords("brick")
    if y2 < 600:
        canvas.move("brick", 0, 6)
        root.after(6, move_brick)

move_brick()

#trebuie sa facem in asa fel incat caramida se opreste daca width = 600
#pentru asta, trebuie sa facem o functie care verifica daca caramida a ajuns la marginea de jos a ecranului
#si daca a ajuns, atunci sa o opreasca
#(canvas.coords()) returneaza coordonatele unui obiect de pe canvas
#(canvas.coords("brick")) returneaza coordonatele caramizii noastre

def check_collision():
    x1, y1, x2, y2 = canvas.coords("brick")
    if y2 < 600:
        root.after(6, check_collision)

check_collision()

# Functie pentru a controla caramida folosind tastatura
def control_brick(event):
    x1, y1, x2, y2 = canvas.coords("brick")
    if event.keysym == "Left" and x1 > 0:
        canvas.move("brick", -30, 0)
    elif event.keysym == "Right" and x2 < 600:
        canvas.move("brick", 30, 0)
    elif event.keysym == "Up" and y1 > 0:
        canvas.move("brick", 0, -30)
    elif event.keysym == "Down" and y2 < 600:
        canvas.move("brick", 0, 30)
    elif event.keysym == "Home" and x1 > 0 and y1 > 0:
        canvas.move("brick", -30, -30)
    elif event.keysym == "End" and x1 > 0 and y2 < 600:
        canvas.move("brick", -30, 30)
    elif event.keysym == "Prior" and x2 < 600 and y1 > 0:
        canvas.move("brick", 30, -30)
        root.title("Prior")
    elif event.keysym == "Next" and x2 < 600 and y2 < 600:
        canvas.move("brick", 30, 30)
        root.title("Next")

# Legam evenimentele de tastatura la functia de control
root.bind("<Left>", control_brick)
root.bind("<Right>", control_brick)
root.bind("<Up>", control_brick)
root.bind("<Down>", control_brick)
root.bind("<Home>", control_brick)
root.bind("<End>", control_brick)
root.bind("<Prior>", control_brick)
root.bind("<Next>", control_brick)

root.mainloop()
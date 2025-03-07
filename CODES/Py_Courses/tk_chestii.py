"""

import tkinter

master = tkinter.Tk()
master.title('Steagul piraților')

canvas = tkinter.Canvas(master, width=600, height=400, bg='black')

canvas.create_line(0, 0, 600, 400, fill='white')

canvas.create_line(0, 400, 600, 0, fill='white')

canvas.pack()

master.mainloop()
"""

"""import tkinter

# Create the main window
master = tkinter.Tk()
master.title('Cilindru Galben')

# Create a canvas with a white background
canvas = tkinter.Canvas(master, width=400, height=400, bg='white')

# Define the coordinates for the top ellipse
top_ellipse = canvas.create_oval(100, 50, 300, 100, fill='yellow', outline='yellow')

# Define the coordinates for the bottom ellipse
bottom_ellipse = canvas.create_oval(100, 250, 300, 300, fill='yellow', outline='yellow')

# Define the coordinates for the left rectangle (side of the cylinder)
left_rectangle = canvas.create_rectangle(100, 75, 100, 275, fill='yellow', outline='yellow')

# Define the coordinates for the right rectangle (side of the cylinder)
right_rectangle = canvas.create_rectangle(300, 75, 300, 275, fill='yellow', outline='yellow')

# Pack the canvas into the window
canvas.pack()

# Run the main loop
master.mainloop()"""

"""import tkinter as tk

master = tk.Tk()
master.title("cilindru")
master.geometry("800x800")

canvas = tk.Canvas(master, width = 600, height = 600, bg = "lightblue")
canvas.create_oval((200,400),(400,500), fill = "yellow", width = 3)
canvas.create_rectangle((200,150), (400,450), fill = "yellow", width = 3)
canvas.create_line((202,450), (400-1,450), fill ="white", width = 5)
canvas.create_oval((200,100), (400,200), fill = "yellow", width = 3)


canvas.pack()
master.mainloop()"""

import tkinter
cercuri = 10
master = tkinter.Tk()
master.title('Babah!')
canvas = tkinter.Canvas(master, width=500, height= 500, bg = "black")
d = 500
pas = 500//cercuri//2
c=0
culoare_curenta = "green"
while d>0:
     if culoare_curenta == "green":
          culuoare_curenta = "red"
     elif culoare_curenta =="red":
          culoare_curenta = "blue"
     else:
          culoare_curenta = "green"
     canvas.create_oval(c,c,c+d,c+d, fill = culoare_curenta)
     d -= pas*2
     c += pas
canvas.pack()
master.mainloop()
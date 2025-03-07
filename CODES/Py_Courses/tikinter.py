import tkinter as tk
import random

root = tk.Tk()
root.title("balon")
root.geometry("600x600")

canvas = tk.Canvas(root, width=600, height=600)  # Create the canvas
canvas.pack()

# List of colors
colors = ('#00ffff', 'blue', '#ff00ff', 'green', 'maroon', 'orange', 'pink', 'purple', 'red', 'yellow', 'violet', '#4b0082', 'chartreuse', '#00ff00', '#f55c4b')

balloons = []

def create_balloon():
    lat_0 = random.randint(30, 60)
    inal_0 = random.randint(40, 80)

    # Generate a random x-coordinate ensuring the ball stays within the canvas
    x_0 = random.randint(lat_0 // 2, 600 - lat_0 // 2)
    y_0 = 400

    # Select a random color for the ball
    ball_color = random.choice(colors)

    # Draw the oval (ball) on the canvas
    ball = canvas.create_oval(x_0 - lat_0 // 2, y_0 - inal_0 // 2, x_0 + lat_0 // 2, y_0 + inal_0 // 2, fill=ball_color)

    # Draw the string
    string_length = 30
    string = canvas.create_line(x_0, y_0 - inal_0 // 2, x_0, y_0 - inal_0 // 2 - string_length, fill="black")

    # Draw the triangle at the end of the string
    triangle_height = 10
    triangle_base = 10
    triangle = canvas.create_polygon(
        x_0, y_0 - inal_0 // 2 - string_length,
        x_0 - triangle_base // 2, y_0 - inal_0 // 2 - string_length - triangle_height,
        x_0 + triangle_base // 2, y_0 - inal_0 // 2 - string_length - triangle_height,
        fill="black"
    )

    balloons.append((ball, string, triangle))

def move_balloons_up():
    for ball, string, triangle in balloons:
        canvas.move(ball, 0, -1)  # Move the ball up by 1 pixel
        canvas.move(string, 0, -1)  # Move the string up by 1 pixel
        canvas.move(triangle, 0, -1)  # Move the triangle up by 1 pixel
        y1, y2 = canvas.coords(ball)[1], canvas.coords(ball)[3]
        if y2 <= 0:  # Check if the ball is still within the canvas
            canvas.coords(ball, -100, -100, -100, -100)  # Move the ball out of the canvas
            canvas.coords(string, -100, -100, -100, -100)  # Move the string out of the canvas
            canvas.coords(triangle, -100, -100, -100, -100, -100, -100)  # Move the triangle out of the canvas
    root.after(30, move_balloons_up)  # Repeat the animation after 30 milliseconds

# Create multiple balloons
for _ in range(10):
    create_balloon()

move_balloons_up()  # Start the animation

root.mainloop()
"""def bullseye(a):
    if a > 50:
        return "Bullseye"
    elif a > 0:
        return "Hit"
    elif a == 0:
        return "missed"
    
print(bullseye(60))
print(f"ai marcat peste 50 puncte")
print(bullseye(10))
print(f"ai marcat peste 10 puncte")
print(bullseye(0))
print(f"ai marcat 0 puncte")"""

"""total_points = 0

def bullseye(a):
    if a > 50:
        return "Bullseye"
    elif a > 0:
        return "Hit"
    elif a == 0:
        return "missed"
    
def shot(points):
    global total_points
    if points == "Bullseye":
        points = 50
    total_points += points
    return f"Ai marcat {points} puncte. Total {total_points} puncte."

print(shot("Bullseye"))
print(shot(18))
print(shot(10))
print(shot(0))"""

"""total_points = 0
shots_taken = 0

def bullseye(a):
    if a > 50:
        return "Bullseye"
    elif a > 0:
        return "Hit"
    elif a == 0:
        return "missed"

def shot(points):
    global total_points, shots_taken
    if shots_taken >= 3:
        return "Game Over"
    shots_taken += 1
    if points == "Bullseye":
        points = 50
    total_points += points
    return f"Ai marcat {points} puncte. Total {total_points} puncte."

print(shot("Bullseye"))
print(shot(18))
print(shot(10))
print(shot("Bullseye"))"""

total_points = 0
shots_taken = 0

def bullseye(a):
    if a > 50:
        return "Bullseye"
    elif a > 0:
        return "Hit"
    elif a == 0:
        return "missed"

def shot(points, circle=0):
    global total_points, shots_taken
    if shots_taken >= 3:
        return "Game Over"
    shots_taken += 1
    if points == "Bullseye":
        points = 50
    if circle == 1:
        points *= 2
    elif circle == 2:
        points *= 3
    total_points += points
    return f"Ai marcat {points} puncte. Total {total_points} puncte."

print(shot("Bullseye"))
print(shot(18, 1))
print(shot(10, 2))
print(shot(20))
print(shot("Bullseye"))




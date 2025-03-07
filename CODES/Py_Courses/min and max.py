x = 0
z = 0

min_value = 9999
max_value = -9999

if x < min_value:
    min_value = x
    x += 1

if z < max_value:
    max_value = z
    z += 1

print("minimul este:", x)
print("maximul este:", z)
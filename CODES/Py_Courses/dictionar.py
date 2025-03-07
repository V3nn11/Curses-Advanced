"""
portofel = {    }
while True:
     b  =  input("introduceti bancnota: ")
     if b == "0":
          break
     if b in portofel:
          portofel[b] += 1
     else:
          portofel[b] = 1
     for bancnota in portofel:
          print("{} - {}".format(bancnota, portofel[bancnota]))
"""
"""
fraza = input("introduceti o bancnota: ")
litere = {}
for l in fraza:
     if l != "":
          if l in litere:
               litere[l] += 1
          else:
               litere[l] =1

     for litera in litere:
          print("{} - {}".format(litera, litere[litera]))
"""


import random

x = [random.randint(0,9) for i in range(10)]
print(x)
y= {}
for i in x:
     if i in y:
          y[i] += 1
     else:
          y[i] = 1
print(y)
key_max = -1
max_value = 0

for i in y:
     if y[i] > max_value:
          max_value = y[i]
          key_max = i

print("Cel mai frecvent numar este: " ,key_max)
print("numere castigatoare: ")
for i in y:
     if y[i] == max_value:
          print(i)

          
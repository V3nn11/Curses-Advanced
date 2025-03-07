"""def pret_bilet(a):
     if a <=4 and a>0:
          return "500 lei"
     
     return "Nu exiista bilet pentru randul {}".format(a)

rand = int(input("intdoceti randul: "))
print(pret_bilet(rand))"""


"""def pret_bilet(a):
    if a <= 4 and a > 0:
        return "500 lei"
    elif a > 4 and a <= 10:
        return "350 lei"
    return "Nu exista bilet pentru randul {}".format(a)

rand = int(input("Introduceti randul: "))
print(pret_bilet(rand))"""

"""def pret_bilet(a):
    if a <= 4 and a > 0:
        return "500 lei"
    elif a > 4 and a <= 10:
        return "350 lei"
    elif a > 10 and a <= 15:
        return "200 lei"
    return "Nu exista bilet pentru randul {}".format(a)"""


"""def pret(*args):
    cost_total = 0
    for pret in args:
        if pret <4 and pret > 0:
            cost_total += 500
        elif pret > 4 and pret <= 10:
            cost_total += 350
        elif pret > 10 and pret <= 15:
            cost_total += 200
        else:
            return cost_total
print(pret(100,1200,500))"""

def pret(*a):
    suma = 0
    for i in a:
        suma_de_mii = i // 1000
        pret_mod = i - 100 * suma_de_mii
        suma += pret_mod

    return suma

print(pret(1000, 1200, 500))


    
"""def cash(x):
    list = x.split(" ")
    return list

print(cash('100 50 100 200 10 5 10'))"""

"""def cash_sum(x):
    list = x.split(" ")
    suma = 0
    for i in list:
        suma += int(i)
    
    return suma

print(cash_sum('100 50 100 200 10 5 10'))"""

"""def portofel(x,n):
    lista = x.split(" ")
    exits = False
    for i in lista:
        if n == int(i):
            exits = True
            break
        
    return exits

print(portofel('100 50 100 200 10 5 10', 20))
print(portofel('100 50 100 200 10 5 10', 10))"""


def xd(x):
    lista = x.split(" ")
    portofel = {}
    for i in lista:
        if i not in portofel:
            portofel[i] = 1
        else:
            portofel[i] += 1
        return portofel
    

print(xd('100 50 100 200 10 5 10'))
    



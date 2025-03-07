"""def superprint():
     print("MANUAL")
command = superprint()
"""
"""def superprint(x):
     y = x.upper()
     print(y)
     
superprint("salut")
"""
"""def hi():
     print("hi!")
command = hi()
"""

"""def suma(a,b):
     print(a+b)
suma(5,5)
"""

"""def show_price(m):
     cost = m * 3.5
     print("pepenele verde costa : {} lei".format(cost))
show_price(2)"""

def show_price(nume, g):
     lei_per_kg = 0

     if nume == "Pepene verde":
          lei_per_kg = 3.5
     elif nume == "pepene galben":
          lei_per_kg = 5
     elif nume == "nuca de cocos":
          lei_per_kg =  10
     total_g = 0
     _max = 0
     for i in g:
          total_g += i

          if i > _max:
               _max = i
     cost = total_g * lei_per_kg
     print(" {}: produsul cu greutate cea mai mare: {},  greutate totala {}, costul {} lei".format(nume , _max,total_g, cost))

show_price("pepene galben", [10,20,30])
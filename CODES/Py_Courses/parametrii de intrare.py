"""def fun1( a=5):
     for i in range(1, a+1):
          print(i)
     print("am invatat sa numar!")
fun1()"""

"""def fun1( a =5):
     for i in range(1, a+1):
          print(i, end = "")
     print(" am invatat sa numar!")
fun1()"""

"""def fun1(a):
    pret_final = a - a * 0.9
    return pret_final

print(fun1(100))"""

"""def fun1(a):
    numarul_de_mii = a // 1000
    pretul_final = a - 100*numarul_de_mii
    return pretul_final

print(fun1(500))
print(fun1(1000))
print(fun1(1500))
print(fun1(2000))
print(fun1(2500))"""

def pret(*args):
    total_cost = 0
    for a in args:
        numarul_de_mii = a // 1000
        pretul_final = a - 100 * numarul_de_mii
        total_cost += pretul_final
    return total_cost

# Test cases
print(pret(100, 900))  
print(pret(500, 1000))  
print(pret(500, 2500, 500))  

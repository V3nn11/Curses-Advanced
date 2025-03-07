x = ("Introduceti denumirea orasului: ") #oras 1

while True:
     z = x #ultimul oras 
     last_char = x[-1]
     x = input("introduceti denumirea orasului incepand cu litera" + last_char + ":") #oras 2
     if last_char.lower != x[0].lower(): # oras 3
          print("stop joc")
          break
     


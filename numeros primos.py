print("Cuando un numero es primo")
x=int(input("Ingresar Numero N"))
a=2
m=True
while a<x:
    try:
        x=int(input("ingresar numero N"))
    except ValueError:
    
        if x%a==0:
            print("0")
            m=False
            break
            print("-1")
        a=a+1

if m==True:
    print("1")
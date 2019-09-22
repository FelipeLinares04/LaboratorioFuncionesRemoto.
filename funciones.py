def a_power_b(a,b):
    x=1
    for i in range(b):
        x=x*a
    return x


n1 = int(input("dijite primer numero"))
n2 = int(input("dijite exponente"))
result=a_power_b(n1,n2)
print(result)

while True:
    if a==0:
        break
  
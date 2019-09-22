def Perfect_number(x):
    v=x//2
    NP=0
    for i in range(1,v+1):
        if x%i==0:
            NP=NP+i

    if(NP==x+3) or (NP==x+2) or (NP==x+1) or (NP==x-3) or (NP==x-2) or (NP==x-1):
        print("es casi perfecto")

w=int(input("Determine su numero para saber si es Perfecto"))
Perfect_number(w)
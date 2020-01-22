

def fac(x):
    y=x-1
    s=x*y
    x=y
    while y>1:      
        y=x-1
        s=s*y
        x=y
    print("Das Ergebnis ist:",s)


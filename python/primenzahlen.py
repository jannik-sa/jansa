
x=2
y=3
for i in range(1000):
    n=y/x

    if int(n)==n:
        y=y+1
        x=2
    elif int(n)!=n:
        x=x+1

    if x==y:
        print(y)

    

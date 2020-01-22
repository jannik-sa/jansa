
for i in range(10):
    x=int(input("Gib eine zahl an von der du die   wissen willst? "))

    y=x-1
    s=x*y
    x=y

    while y>1:
            
        y=x-1
        s=s*y
        x=y

            

    print(s)



'''rechner'''
w=1
s=1
x = int(input("Mit wie vielen Zahlen willst du rechnen \n "))

if x == 1:
    x = int(input("Also willst du Quatrieren/Wurzen?(1/2/3(Nein))\n"))
    if x == 2:
        print("Wurzelberechnung mit einer Zahl")
        w = float(input("Welche Zahl ?\n"))
        s=w / 2 
        c=s * s      
        g=s/2
     
        while c!=w:
                
            if w>c:
                
                d=s/4
                s=s+d
                c=s*s
                g=s
                print(s)
            elif w<c:
                
                d=s/4     
                s=s-d
                c=s*s
                g=s
                print(s)       
 
        print("Das Ergebnis:",s)
        
if x==0:
    y=int(input("Rechnung:"))
    print(y)
       

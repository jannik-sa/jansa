
class Poketmoney():

    def __init__(self, name):
        #self.data = {'name' : name,"amount" : 0 }
        self.name = name
        self.amount = 0
        
        
    def setAmount(self, value):
        self.amount=value
            
    def getAmount(self):
        return self.amount
        
    def rename(self, name):
        self.name = name
    
            
    def getName(self):
        return self.name
        
    def ausgabe(self):
        return self.getName()
        
    def __str__(self):
        return "Name=%s, Betrag=%s" % (self.name, self.amount)
 
       
    
        
    
        
    
obj = Poketmoney("Jannik")
obj2 = Poketmoney("susi")

obj.rename("Jannik Erwin")

obj2.setAmount(20)
obj.setAmount(100)

print(obj)
print(obj2)


print("%s\n%s" % (obj, obj2))
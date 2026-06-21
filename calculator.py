work=input("add/sub/mul/div:")
c=int(input("Entre a number:"))
d=int(input("Entre a number:"))

class calculator:
    def __init__(self,f,g):
        self.a=f
        self.b=g
    def calculate(self):
        if(work=="add"):
             print("add:",self.a + self.b)
        elif(work=="sub"):
             print("sub:",self.a - self.b)
        elif(work=="mul"):
             print("mul:",self.a * self.b)
        elif(work=="div"):
             print("div:",self.a / self.b)
        else:
            print("invalid data")

        
   
object=calculator(c,d)
object.calculate()

    

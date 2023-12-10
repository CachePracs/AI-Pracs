class WaterJug:
    def __init__(self,am,bm,a,b,g):
        self.a_max=am
        self.b_max=bm
        self.a = a
        self.b=b
        self.goal=g
    
    def fillA(self):
        self.a=self.a_max
        print(self.a,self.b)
    
    def emptyB(self):
        self.b=0
        print(self.a,self.b)

    def transferAtoB(self):
        if self.a+self.b>self.b_max:
            self.a = self.a - (self.b_max - self.b)
            self.b = self.b_max
        else:
            self.b=self.a+self.b
            self.a=0
        print(self.a,self.b)
    
    def main(self):
        while(True):
            if self.a==self.goal or self.b==self.goal:
                break
            elif self.a==0:
                self.fillA()
            elif self.a>0 and self.b < self.b_max:
                self.transferAtoB()
            elif self.a>0 and self.b == self.b_max:
                self.emptyB()

waterjug = WaterJug(4,3,0,0,2)
waterjug.main()

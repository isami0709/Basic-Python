class Dice:
    def __init__(self,a,b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    
    def roll(self,direct):
        if direct == 'N' :
            self.a,self.b,self.c,self.d,self.e,self.f = self.b,self.f,self.c,self.d,self.a,self.e
        if direct == 'S':
            self.a,self.b,self.c,self.d,self.e,self.f = self.e,self.a,self.c,self.d,self.f,self.b
        if direct == 'W':
            self.a,self.b,self.c,self.d,self.e,self.f = self.c,self.b,self.f,self.a,self.e,self.d
        if direct == 'E':
            self.a,self.b,self.c,self.d,self.e,self.f = self.d,self.b,self.a,self.f,self.e,self.c


a,b,c,d,e,f = input().split()
dice = Dice(a,b,c,d,e,f)
for i in input():
    dice.roll(i)

print(dice.a)

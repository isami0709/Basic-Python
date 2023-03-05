class Dice:
    def __init__(self,a,b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def judge(self,u,v,w,x,y,z):
        if u == self.b:
            self.a,self.b,self.c,self.d,self.e,self.f = self.b,self.f,self.c,self.d,self.a,self.e
        if u == self.c:
            self.a,self.b,self.c,self.d,self.e,self.f = self.c,self.b,self.f,self.a,self.e,self.d
        if u == self.d:
            self.a,self.b,self.c,self.d,self.e,self.f = self.d,self.b,self.a,self.f,self.e,self.c
        if u == self.e:
            self.a,self.b,self.c,self.d,self.e,self.f = self.e,self.a,self.c,self.d,self.f,self.b
        if u == self.f:
            self.a,self.b,self.c,self.d,self.e,self.f = self.f,self.e,self.c,self.d,self.b,self.a
        if v == self.c:
            self.a,self.b,self.c,self.d,self.e,self.f = self.a,self.c,self.e,self.b,self.d,self.f
        if v == self.d:
            self.a,self.b,self.c,self.d,self.e,self.f = self.a,self.d,self.b,self.e,self.c,self.f
        if v == self.e:
            self.a,self.b,self.c,self.d,self.e,self.f = self.a,self.e,self.d,self.c,self.b,self.f
        if u == self.a and v == self.b and w == self.c and x == self.d and y == self.e and z == self.f:
            print('Yes')
        else:
            print('No')

u,v,w,x,y,z = input().split()
a,b,c,d,e,f = input().split()
dice1 = Dice(u,v,w,x,y,z)
dice2 = Dice(a,b,c,d,e,f)
dice2.judge(u,v,w,x,y,z)

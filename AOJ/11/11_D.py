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
            conc_list.append('y')
        else:
            None

n = int(input())
dice_list = [input().split() for _ in range(n)]
conc_list = []
for i in range(n):
    for j in range(n):
        if i != j:
            dice1 = Dice(dice_list[i][0],dice_list[i][1],dice_list[i][2],dice_list[i][3],dice_list[i][4],dice_list[i][5])
            dice2 = Dice(dice_list[j][0],dice_list[j][1],dice_list[j][2],dice_list[j][3],dice_list[j][4],dice_list[j][5])
            dice1.judge(dice_list[j][0],dice_list[j][1],dice_list[j][2],dice_list[j][3],dice_list[j][4],dice_list[j][5])

if 'y' in conc_list:
  print('No')
else:
  print('Yes')

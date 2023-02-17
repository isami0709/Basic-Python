u,v,w,x,y,z = input().split()
a,b,c,d,e,f = input().split()
if u == b:
    a,b,c,d,e,f = b,f,c,d,a,e
if u == c:
    a,b,c,d,e,f = c,b,f,a,e,d
if u == d:
    a,b,c,d,e,f = d,b,a,f,e,c
if u == e:
    a,b,c,d,e,f = e,a,c,d,f,b
if u == f:
    a,b,c,d,e,f = f,e,c,d,b,a
if v == c:
    a,b,c,d,e,f = a,c,e,b,d,f
if v == d:
    a,b,c,d,e,f = a,d,b,e,c,f
if v == e:
    a,b,c,d,e,f = a,e,d,c,b,f
if u == a and v == b and w == c and x == d and y == e and z == f:
    print('Yes')
else:
    print('No')
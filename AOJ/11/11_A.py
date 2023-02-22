a,b,c,d,e,f = input().split()
vector = input()
vector_list = []
for i in vector:
    vector_list.append(i)

for v in vector_list:
    if v == 'N' :
        a,b,c,d,e,f = b,f,c,d,a,e
    if v == 'S':
        a,b,c,d,e,f = e,a,c,d,f,b
    if v == 'W':
        a,b,c,d,e,f = c,b,f,a,e,d
    if v == 'E':
        a,b,c,d,e,f = d,b,a,f,e,c
print(a)

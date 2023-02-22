n = int(input())
dice_list = [input().split() for _ in range(n)]
judge_list = []
for dice1 in dice_list:
    for dice2 in dice_list:
        if dice1 != dice2:
            a = dice1[0]
            b = dice1[1]
            c = dice1[2]
            d = dice1[3]
            e = dice1[4]
            f = dice1[5]
            u = dice2[0]
            v = dice2[1]
            w = dice2[2]
            x = dice2[3]
            y = dice2[4]
            z = dice2[5]
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
                judge_list.append('No')
            else:
                judge_list.append('Yes')

if 'No' in judge_list:
    print('No')
else:
    print('Yes')
                        
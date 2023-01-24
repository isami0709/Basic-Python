sum = 0
while True:
    n,x = map(int,input().split())
    if n == 0 and x == 0:
        break
    else:
        for i in range(1,n + 1):
            for j in range(1,n + 1):
                for k in range(1,n + 1):
                    if i + j + k == x and i < j < k:
                        sum += 1
        print(sum)
    sum = 0
    
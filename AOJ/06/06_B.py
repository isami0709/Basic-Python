n = int(input())
N = 0
rank = ["S", "H", "C", "D"]
cards= [[0,0,0,0,0,0,0,0,0,0,0,0,0]for i in range(4)]
while True:
    if N != n:
        mark, num = input().split()
        if mark == "S":
            cards[0][int(num) -1] = num
        elif mark == "H":
            cards[1][int(num) -1] = num
        elif mark == "C":
            cards[2][int(num) -1] = num
        elif mark == "D":
            cards[3][int(num) -1] = num
        N += 1               
    elif N == n:
        break
while n <= 52:
    if n != 52:
        for k in range(4):
            for i in range(13):
                if cards[k][i] == 0:
                    print(f'{rank[k]} {i + 1}')
                    n += 1
    if n == 52:
        break

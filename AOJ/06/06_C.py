n = int(input())
N = 0
residence = [[[0 for rooms in range(10)]for floors in range(3)]for buildings in range(4)]
while True:
    if N != n:
        b, f, r, v = input().split()
        residence[int(b)-1][int(f)-1][int(r)-1] += int(v)
        N += 1
    if N == n:
        res = [[[str(v) for v in residence[b][r]]for r in range(3)]for b in range(4)]
        for i in range(3):
                for k in range(4):
                    if k != 3:
                        print(f' {" ".join(res[i][k])}')
                    if k ==3:
                        print("#" * 20)
        for l in range(3):
            print(f' {" ".join(res[3][l])}')
        break

W, H, x, y, r = map(int, input().split())
if x + r <= W and x - r >= 0 and y - r >= 0 and y + r <= H:
    print("Yes")
else:
    print("No")

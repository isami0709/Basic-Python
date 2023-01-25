while True:
    num = 0
    n = input()
    if n == '0':
        break
    else:
        for d in n:
           num += int(d)
        print(num)

while True:
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    if op == '+':
        print(f'{a + b}')
    elif op == '-':
        print(f'{a - b}')
    elif op == '*':
        print(f'{a * b}')
    elif op == '/':
        print(f'{a//b}')
    elif op == '?':
        break
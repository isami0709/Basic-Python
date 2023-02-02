string = input().lower()
numlist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
alplist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for s in string: 
    if 97 <= ord(s) <= 97 + 25 :
        num = ord(s) - ord('a')
        numlist[num] += 1
for i in range(len(numlist)):
    numb = str(97 + i)
    print(f'{alplist[i]} : {numlist[i]}')
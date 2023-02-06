numlist = [0] * 26
alplist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
    try:
        string = input().lower()
    except:
        break
    for s in string: 
        if 97 <= ord(s) <= 97 + 25 :
            numlist[ord(s) - ord('a')] += 1
for i in range(len(numlist)):
    print(f'{alplist[i]} : {numlist[i]}')
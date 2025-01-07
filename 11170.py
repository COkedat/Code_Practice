def getZeroCnt(a, b):
    zero=0
    for i in range(a,b+1):
        quest = list(str(i))
        for j in quest:
            if (j=='0'):
                zero+=1
    return zero

cnt = int(input())
for i in range(cnt):
    inp = input().split(' ')
    a = int(inp[0])
    b = int(inp[1])
    print(getZeroCnt(a, b))

    



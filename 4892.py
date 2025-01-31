cnt = 1
while True:
    N = int(input())
    if(N==0):
        break
    print(cnt,end="")
    print(". ",end="")
    cnt+=1
    n1 = N * 3
    if(n1 % 2 == 1): # 홀수
        print("odd ",end="")
        n2 = n1//2
    else:
        print("even ",end="")
        n2 = (n1+1)//2
    n3 = 3*n2
    n4 = n3//9
    print(n4)
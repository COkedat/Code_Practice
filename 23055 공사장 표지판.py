N=int(input())
if(N==1):
    print("*", end="")
else:
    for i in range(N):
        for j in range(N):
            panel=" "
            if((i==0 or i==N-1) or (j==0 or j==N-1)):
                panel="*"
            if(i==j):
                panel="*"
            if(i==N-j-1):
                panel="*"
            print(panel, end="")
        if(i!=N-1):
            print()
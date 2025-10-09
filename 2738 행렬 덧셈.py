N, M = map(int,input().split(" "))
A = []
B = []
for i in range(N):
    tmp = list(map(int,input().split(" ")))
    A.append(tmp)
for i in range(N):
    tmp = list(map(int,input().split(" ")))
    B.append(tmp)
for i in range(N):
    for j in range(M):
        print(f"{A[i][j]+B[i][j]} ",end="")
    print()
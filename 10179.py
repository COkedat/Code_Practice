N=int(input())
for _ in range(N):
    tmp = float(input())
    print("${:.2f}".format(round(tmp*0.8,2)))